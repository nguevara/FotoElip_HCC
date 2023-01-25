#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:47:35 2022

@author: nati
"""

import matplotlib.pyplot as plt
from matplotlib import style
from photutils.aperture import EllipticalAperture
from astropy.visualization import ImageNormalize, ZScaleInterval, LinearStretch, simple_norm
import numpy as  np
from photutils.isophote import IsophoteList
import sys
sys.path.append("..") 
from aux import addreq,addmu

import astropy.units as u

style.use('bmh')

#%%

# =============================================================================
#  Grafica una sola isofota sobre la imagen, dado un objeto geometry.
# =============================================================================
def graf_1ellip(geometry,image,vmin=None,vmax=None,size=1000,title=None,
                show=False):
    fig=plt.figure()
    interval = ZScaleInterval()
    if (vmin==None) & (vmax==None):                                   
        vmin, vmax = interval.get_limits(image)                  
    norm = simple_norm(image, 'sqrt', percent=99.)            


    aper = EllipticalAperture((geometry.x0, geometry.y0), geometry.sma,
                              geometry.sma * (1 - geometry.eps),
                              geometry.pa)
    
    plt.imshow(image, origin='lower',norm = norm)

    aper.plot(color='white')

    plt.xlim(left=geometry.x0-size,right=geometry.x0+size)
    plt.ylim(top=geometry.y0+size,bottom=geometry.y0-size)
    if title!= None:
        plt.title(title)

    fig.tight_layout()
    return(fig)

# =============================================================================
# Grafica varias isofotas sobre la imagen, dada una lista de isofotas.
# =============================================================================
def graf_all_ellip(geometry,image,isolist,
                   vmin=None, vmax=None,size=1000,title=None,
                   mode='all',
                   show=False):
    interval = ZScaleInterval()
    if (vmin==None) & (vmax==None):                                   
        vmin, vmax = interval.get_limits(image)                  
    norm = simple_norm(image, 'sqrt', percent=99.)        
    fig=plt.figure()
    plt.xlim(left=geometry.x0-size,right=geometry.x0+size)
    plt.ylim(top=geometry.y0+size,bottom=geometry.y0-size)
    
    plt.imshow(image, origin='lower',norm = norm)
    if mode=='all':
        for iso in isolist:
            x,y=iso.sampled_coordinates()
            plt.plot(x,y,color='white')
    else:
        next
            
    if title!= None:
        plt.title(title)
        
    fig.tight_layout()
    return(fig)
    
# =============================================================================
# Grafica una imagen fits    
# =============================================================================
def graffit(image,x0=None,y0=None,vmin=None, vmax=None,size=None,
            title=None,cbar=False
            ):
    fig=plt.figure()
    interval = ZScaleInterval()
    if (vmin==None) & (vmax==None):                                   
        vmin, vmax = interval.get_limits(image)                  
    norm = simple_norm(image, 'sqrt', percent=99.)   
    if (x0!=None) & (y0!=None) & (size!=None):
        plt.xlim(left=x0-size,right=x0+size)
        plt.ylim(top=y0+size,bottom=y0-size)
    if title!= None:
        plt.title(title)
    plt.imshow(image, origin='lower',norm = norm)
    if cbar:
        plt.colorbar()

    
    fig.tight_layout()
    return(fig)
        


#%%


    
#%%

#  Plot some parameters from isolist or qtable (or dataframe)

def param_plot(isolist,req=True,n=1000,E=None,arcmin=False,show=False):
    
    if type(isolist)==IsophoteList:
        isolist=isolist.to_table(isolist.get_names())

    if req:
        addreq(isolist,E,arcmin)
        x=isolist['req']
        if arcmin==False:
            label=r'$r_{eq}$ (arcsec)'
            # n=n*E
        else:
            label=r'$r_{eq}$ (arcmin)'
            # n=n*E/60.
    else:
        x= isolist['sma']
        label='Semieje mayor a (pix)'
        
    
    fig=plt.figure(figsize=(8, 8))
    fig.subplots_adjust(hspace=0.35, wspace=0.35)
    style.use('seaborn-dark')
    
    ### elipticidad
    
    ax1=fig.add_subplot(2, 2, 1)
    
    ax1.plot(x[x<n], isolist['eps'][x<n],'k',alpha=.6,lw=.5 )
    ax1.fill_between( x[x<n],
                     isolist['eps'][x<n] - isolist['ellip_err'][x<n],
                     isolist['eps'][x<n] + isolist['ellip_err'][x<n])
    
    ax1.set(xlabel=label)
    ax1.set_ylim([0,0.6])
    ax1.set(ylabel=r'Elipticidad $\epsilon$')

    ## 180 - pa porque se mide respecto al norte, y la imagen esta rotada
    # y_pa=[]
    # for y in isolist['pa'][x<n]:
    #     y_pa.append( (180. * u.deg - y ) / (1.*u.deg)) # asi si funciona?
    # y_pa_err = []
    # for y in isolist['pa_err'][x<n]:
    #     y_pa_err.append(y * u.dimensionless_unscaled)
    # del y
    y_pa = isolist['pa'][x<n].value
    y_pa_err = isolist['pa_err'][x<n].value
    
    ax2=fig.add_subplot(2, 2, 2)
    
    ax2.plot( x[x<n],180. - y_pa,'k',alpha=.6,lw=.5 )
    ax2.fill_between( x[x<n],
                     180. - y_pa - y_pa_err,
                     180. - y_pa + y_pa_err)

    
    ax2.set(xlabel=label)
    ax2.set_ylim([10,70])
    ax2.set(ylabel='Ángulo de posición PA ($^\circ$)')
    
    ax3=fig.add_subplot(2, 2, 3)
    
    ax3.plot( x[x<n],isolist['x0'][x<n],'k',alpha=.6,lw=.5 )
    ax3.fill_between( x[x<n],
                     isolist['x0'][x<n] - isolist['x0_err'][x<n],
                     isolist['x0'][x<n] + isolist['x0_err'][x<n], label='$x_c$')
    
    ax3.plot( x[x<n], isolist['y0'][x<n],'k',alpha=.6,lw=.5 )
    ax3.fill_between( x[x<n],
                     isolist['y0'][x<n] - isolist['y0_err'][x<n],
                     isolist['y0'][x<n] + isolist['y0_err'][x<n], label='$y_c$')
    
    
    ax3.set(xlabel=label)
    ax3.set(ylabel='Posición del centro [pix]')
    
    ax4=fig.add_subplot(2, 2, 4)
    ax4.plot(x[x<n], isolist['b4'][x<n],'k',alpha=.6,lw=.5 )
    
    ax4.axhline(y=0,lw=.7,ls='-')
    ax4.fill_between(x[x<n],
                     isolist['b4'][x<n] - isolist['b4_err'][x<n],
                     isolist['b4'][x<n] + isolist['b4_err'][x<n])
    
    
    ax4.set(xlabel=label)
    ax4.set(ylabel='$B_4$')
    
    fig.tight_layout()

    return(fig)

def muplot(isolist,E,texp,B,mu0=None, arcmin=True,n=2.,show=False):
    
    if type(isolist)==IsophoteList:
        isolist=isolist.to_table(isolist.get_names())
        
    addreq(isolist,E,arcmin)
    x=isolist['req']
    addmu(isolist,E,texp,B,mu0)
    y=isolist['mu']
    
    if mu0!=None:
        ylab=r'$\mu$ [mag/arcsec$^2$]'
    else:
        ylab=r'$\mu_{inst}$ [mag/arcsec$^2$]'
    
    if arcmin:
        xlab=r'$r_{eq}$ (arcmin)'
    else:
        xlab=r'$r_{eq}$ (arcsec)'
        
        
    style.use('seaborn-dark')
    fig=plt.figure()
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.plot(x[x<n],y[x<n])
    plt.gca().invert_yaxis()
    
    
    fig.tight_layout()   
        
    return(fig)