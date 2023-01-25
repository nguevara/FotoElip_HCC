from astropy.table import QTable
from astropy.io import ascii
from photutils.isophote import IsophoteList, Isophote
from photutils.isophote import EllipseSample#, EllipseFitter
from photutils.isophote import EllipseGeometry
import numpy as np

#%%
def isosave(isolist,namef='isolist.dat',path='.'):
    tabla=isolist.to_table(isolist.get_names())
    ascii.write(tabla,path + '/' + namef,overwrite=True)
    
    
def to_iso(namef,ref,path='data/'):
    # paso el archivo a un QTable
    data = QTable.read(path+'/'+namef,format='ascii')
    
    # lista de isofotas
    isolist=[]
    for i in range(len(data)):

        ## leo la tabla para generar un objeto geometry
        geometry = EllipseGeometry(x0  = data['x0'][i],
                                   y0  = data['y0'][i],
                                   sma = data['sma'][i],
                                   eps = data['eps'][i],
                                   pa  = data['pa'][i],
                                   fix_center = True,
                                   fix_pa     = True,
                                   fix_eps    = True,
                                   astep=0.)
        ### genero un sample con fixed parameters
        sample= EllipseSample(ref,
                              data['sma'][i],
                              geometry=geometry
                              )
        # si no, me da error
        sample.update(fixed_parameters=np.array([True,True,True,True]))
            
        isophote = Isophote(sample, 0, True, 0)
        isolist.append(isophote)
    return(IsophoteList(isolist))


#%%

### dada una Qtable, le agrega el radio equivalente como columna,
### si le doy la escala lo agrega en arcominutos o arcosegundos
def addreq(isotabla,E=None,arcmin=False):
    req= isotabla['sma'] * np.sqrt(1.- isotabla['eps']) 
    if ~(E==None):
        req=req*E
        if arcmin==True:
            req=req/60.
    isotabla['req']=req

### dada una Qtable, le agrega el brillo sup como columna
## si tengo el punto cero es estandar si no es instrumental
        # mus[flt]=c0[flt] - 2.5 * np.log10( (dfs[flt]['INTENS']-B[flt]) / (t[flt]
        #                                                                   * E**2 ))
def addmu(isotabla,E,texp,B,mu0=None):
    mu= -2.5 * np.log10( (isotabla['intens'] - B) / (texp * E**2))
    if mu0!=None:
        mu=mu0+mu
    isotabla['mu']=mu
