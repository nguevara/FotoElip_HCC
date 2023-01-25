#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:41:02 2022

@author: nati
"""

# =============================================================================
#  Importar paquetes
# =============================================================================



from astropy.io import  fits

import numpy.ma as ma

import time

from aux.graf import graffit,param_plot,muplot

from bkg import bkg

from bkg.mask import masking

from phot import ellip1, inellip

from residue import model

from aux import isosave


import parameters as pmt
#%%


def main():
    
    ### open image
    nfile_ref=pmt.fname['ref']['path']+'/'+pmt.fname['ref']['name']
    with fits.open( nfile_ref, mode='readonly' ) as ref_hdu :
        ref_data = ref_hdu[0].data
        ref_hed  = ref_hdu[0].header   
    
    
    grafs=[]
    
    
    ## set timer
    st = time.time()
    
    
    if pmt.bkg['bkg']==None: ### if there is no sky level, 
        cielo=bkg(ref_data)  ### makes an estimation
    else:
        cielo=pmt.bkg['bkg'] ### or uses input
           
    ## masking
    if pmt.mask['calc'] : ### makes a mask for other sources
        aux_isolist,a,b= ellip1(ref_data,
                            pmt.ellipse_incial_0,
                            pmt.fit_ell_par_0)
        grafs.append(a)
        grafs.append(b)
            
        ## uses residue of 1st approx to detect sources
        aux_model,aux_residual,a=model(ref_data,aux_isolist,cielo,save=False)
        
        grafs.append(a)
        
        ## generates mask using the residual
        ref_m,a=masking(ref_data,
                      aux_residual,
                      cielo,
                      nthr=pmt.mask['nthr'],
                      fwhm=pmt.mask['fwhm'],
                      sharp=pmt.mask['sharp'],
                      roundlim=pmt.mask['roundlim'],
                      threshold=pmt.mask['threshold'],
                      outf='mask.fits'
                      )
        grafs.append(a)
    else: ## given a .fits image that has a mask 
        with fits.open(pmt.mask['path']+'/'+pmt.mask['file'], mode='readonly') as mask_hdu :
            mask_data = mask_hdu[0].data
        # apply mask
        ref_m = ma.masked_where(mask_data>0, ref_data, copy=True)
        a = graffit(ref_m,cbar=True,title='Máscara dada por input')
        grafs.append(a)
        
        
        
    ### do photometry 
    isolist,a,b = ellip1(ref_m,
           pmt.ellipse_incial,
           pmt.fit_ell_par)
    
    grafs.append(a)
    grafs.append(b)
    
    
    
   # # # # # #
  
        
    ### shows reside of model
    
    
    model_image,residual,a=model(ref_data,
                                 isolist,
                                 cielo,
                                 pmt.guardar['residue'],
                               pmt.fname['out']['residue']['name'],
                               pmt.fname['out']['residue']['path'],
                               ref_hed)
    grafs.append(a)
    
    grafs2=[None,None]
    
    if pmt.plots['param_plot']:
        grafs2[0]= param_plot(isolist,
                   req=pmt.plots['req'],
                   n=pmt.plots['n_par'],
                   E=pmt.plots['E'],
                   arcmin=pmt.plots['arcmin'])
    if pmt.plots['mu_plot'] :
        grafs2[1]=muplot(isolist,
               E = pmt.plots['E'],
               texp = pmt.plots['texp'],
               B = cielo,
               mu0 = pmt.plots['mu0'],
               n = pmt.plots['n_mu'],
               arcmin = pmt.plots['arcmin'])



      
    if pmt.guardar['save_iso']: ## save isophote list as file
        isosave(isolist,
                path=pmt.fname['out']['table']['path'],
                namef=pmt.fname['out']['table']['name'])

        
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


    

    return(grafs,grafs2,cielo)

#%%
if __name__== "__main__":
    main()

#%%
# =============================================================================
# hay algo malito aun,sospecho que la determinacion del bkg !
## si no, probar de nuevo jugando a dejar todo libre, o ++ step adentro?
# =============================================================================
# =============================================================================
# puede ser tamb que no logre enmascarar bien esa galaxia, entonces hayq ue
#  probar con el segmentations de photutils !!
# =============================================================================
 
