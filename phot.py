from photutils.isophote import EllipseGeometry
from photutils.isophote import Ellipse
from photutils.isophote import IsophoteList, Isophote
from photutils.isophote import EllipseSample, EllipseFitter

import numpy as np
from tqdm import tqdm
from aux.graf import graf_1ellip,graf_all_ellip

from astropy.table import QTable

#%%


def ellip1(ref,ellipse0,pmts=None):
    
    if pmts==None:  ## set default
        pmts={
            'sclip' : 3.0,
            'nclip' : 5,
            'fflag' : 1.,
            'integrmode' : 'median',
            'cut' : 250.,
            'maxs' : 900.,
            'fix' : True,
            'step0' : 0.1,
            'step1' : 5,
            'conver' : 0.1,
            'minsma' : 0.,
            'linear' : False
            }

    
    ## aprox inicial a una isofota
    geometry0 = EllipseGeometry(x0=ellipse0['x0'],
                               y0=ellipse0['y0'],
                               sma=ellipse0['sma'],
                               eps=ellipse0['ellip'],
                               pa= np.deg2rad(180-ellipse0['pa']))
    
    
    
    geometry0.find_center(ref)
   
    
    plot1=graf_1ellip(geometry0,ref,
                title='Isofota inicial')
    
    
    ellipse0 = Ellipse(ref, geometry0)
    isolist0 = ellipse0.fit_image(integrmode=pmts['integrmode'],
                                  sclip=pmts['sclip'],
                                  nclip=pmts['nclip'],
                                  fflag=pmts['fflag'],
                                  maxsma=pmts['cut'],
                                  minsma=pmts['minsma'],
                                  step=pmts['step0'],
                                  linear=False,
                                  #linear=pmts['linear'],
                                  conver=pmts['conver']                
                                  )
    if pmts['fix']:
        n=-1
        geometry0_ =EllipseGeometry(
                                    x0  = isolist0.x0[n],
                                    y0  = isolist0.y0[n],
                                    sma = isolist0.sma.max(),
                                    eps = isolist0.eps[n],
                                    pa  = isolist0.pa[n],
                                    fix_pa     = True,
                                    fix_center = True,
                                    fix_eps    = True
                                    )  ## tomo la geometría de la ultima isofota
        isolist=[]
        
        ## del corte al maximo, con paso step1
        var_=np.arange(pmts['cut'], pmts['maxs'],pmts['step1'])
        
        j=0
        
        with tqdm(total=len(var_)) as pgba:  # en su momento le puse una progres bar
            for sma in var_:
                if sma==pmts['cut']:  
                    j=j+1
                    pgba.update()
                else:
                    sample= EllipseSample(ref,
                                          sma,
                                          geometry=geometry0_,
                                          integrmode='median')
                    sample.update()
                    isophote = Isophote(sample, 0, True, 0)
                   
                    isolist.append(isophote)
                   
                    j=j+1
                    
                    pgba.update()
                   
                    
                    
            
            pgba.close()
     
        for iso in isolist:
            isolist0.append(iso)
        
        isolist0.sort()

    plot2=graf_all_ellip(geometry0, ref, isolist0,
                   title='Todas las isofotas')
    # print('all done')
    return(isolist0,plot1,plot2)
#%%


def inellip( namef , ref,path=None):  
    if path==None:
        _ = namef
    else:
        _ = path + '/' + namef
    
    # paso el archivo a un QTable
    data = QTable.read( _ ,format='ascii')
    
    
    ## tomo el indice con el fwhm 
    n=abs(data['intens'] - data['intens'].max()/2).argmin()
    
    #con esto tomo una isofota masomenos representativa de la galaxia
    # se usa despues para graficar
    
    geometry_n = EllipseGeometry(x0  = data['x0'][n],
                                y0  = data['y0'][n],
                                sma = data['sma'][n],
                                eps = data['eps'][n],
                                pa  = np.deg2rad(data['pa'][n]) ## pues en el file esta en grados
                                )
    
    # graf_1ellip(geometry_n, ref)
    
    # lista de isofotas
    isolist=[]
    
    
    
    ## se supone que cada isofota es independiente de la otra,
    for i in range(len(data)):
        ## leo la tabla para generar un objeto geometry
        geometry = EllipseGeometry(x0  = data['x0'][i],
                                   y0  = data['y0'][i],
                                   sma = data['sma'][i],
                                   eps = data['eps'][i],
                                   pa  = np.deg2rad(data['pa'][n]),
                                   fix_center = True,
                                   fix_pa     = True,
                                   fix_eps    = True,
                                   astep=0.1
                                   )
        
        # print(i,data['x0'][i],geometry.x0)
        geometry.find_center(ref,verbose=False)
        
        ### genero un sample con fixed parameters
        sample= EllipseSample(ref*1e3, ## para que no tenga errores por grad bajo 
                              data['sma'][i],
                              geometry=geometry,
                              integrmode='median'
                              )
        # hace un update del sample, 
        # escanea la imagen a traves del camino eliptico de ref y calcula parametros estadisticos
        sample.update(fixed_parameters=np.array([True,True,True,True]))

        
        isophote = Isophote(sample, 0, True, 0)
        
      
        isolist.append(isophote)
        
    isolist = IsophoteList(isolist) 
    
    plot=graf_all_ellip(geometry_n, ref, isolist,
                   title='Isofotas')
    
    return(isolist,plot)
