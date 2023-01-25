#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:59:55 2022

@author: nati
"""
from photutils.detection import DAOStarFinder
from photutils.aperture import CircularAperture
import numpy as np
import numpy.ma as ma
import pandas as pd

from astropy.io import  fits

import sys
sys.path.append("..") 
from aux.graf import graffit


from photutils.segmentation import detect_sources
#%%
# daophot mask 
def dfmask(ref,residual,bkg,nthr=5.,fwhm=2.0,sharp=[0.2,1.0],roundlim=[-1.,1.],
           silent=True):
    daofind = DAOStarFinder(fwhm=fwhm, threshold=nthr*bkg,
                            sharplo=sharp[0],
                            sharphi=sharp[1],
                            roundlo=roundlim[0],
                            roundhi=roundlim[1])  
    
    sources = daofind(residual)  
    
    positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
    
    apertures = CircularAperture(positions, r=4.)
    
    ref_m = ma.masked_equal(ref,False)

    masked0=apertures.to_mask(method='center')
    
    ttable=pd.DataFrame()
    A,B,C,D=[],[],[],[]
    # tomo los limites en x-y de cada apertura
    for mask in masked0:
        a,b,c,d=( int(x) for x in mask.bbox.extent)
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    ## agrego columnas
    ttable['xmin']=A
    ttable['xmax']=B
    ttable['ymin']=C
    ttable['ymax']=D
    ttable['mask']=np.array(masked0)
    
    # ttable=ttable.set_index('mask')
    
    # limites de la imagen
    ylim=ref.shape[0]
    xlim=ref.shape[1]
    
    masking= np.array([[False]*xlim]*ylim)

    for i in range(len(ttable)):
        xs=range(ttable.xmin[i],ttable.xmax[i])
        ys=range(ttable.ymin[i],ttable.ymax[i])
        
        n=0
        for x in xs:
            m=0
            for y in ys:
                if (y<ylim and x<xlim):
                    value=ttable['mask'][i].data[n][m]
                    if value>0 :
                        masking[y][x]=True
                m=m+1
            n=n+1
                    
    ref_m.mask= masking
    plot=None
    if silent==False:
        plot=graffit(ref_m, 0,0,size=0 ,cbar=True)
        plot.title('mascara daofind aplicada a g')
    # plt.legend()
    return(ref_m,plot)
    # return(ttable,ref_m)

# segmentation mask
def segmask(ref,residual,threshold=1.,silent=True):
    segment_map = detect_sources(residual, threshold, npixels=10,connectivity=8)
    
    ref_m = ma.masked_equal(ref,False)
    ref_m.mask=segment_map.data
    plot=None
    if silent==False:
        plot=graffit(ref_m, 0, 0,size=0,cbar=True)
        plot.title('mascara segment aplicada a g')
    return ref_m,plot

#%%
# join both methods?

def masking(ref,residual,bkg,
            nthr=5.,
            fwhm=2.0,
            sharp=[0.2,1.0],
            roundlim=[-1.,1.],
            threshold=1.,
            outf='mask.fits'
            ):
    silent=True
    mask_df,_ = dfmask(ref, residual, bkg,nthr,fwhm,sharp,roundlim,silent)
    mask_sg,_ = segmask(ref,residual,threshold,silent)
    mascara = ma.mask_or(mask_df.mask,mask_sg.mask)
    
    
    if ~(outf == None):
        hdu = fits.PrimaryHDU(mascara.astype(int))
        hdul = fits.HDUList([hdu])
        hdul.writeto(outf,overwrite=True)
            
            
    
    ref_m = ma.masked_equal(ref,False)
    ref_m.mask=mascara
    
    plot =graffit(ref_m,cbar=True,title='Máscara generada por script')
    
    return ref_m,plot

