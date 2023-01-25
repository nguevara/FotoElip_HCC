from photutils.isophote import build_ellipse_model
from aux.graf import graffit
from astropy.io import  fits


#%%

def model(ref,isolist,bkg,save=True,namef='resifue.fits',path='data',hed=None):
    model_image = build_ellipse_model(ref.shape, isolist,
                                      high_harmonics=True,
                                      fill=bkg)
    
    
    residual = ref - model_image 
    
    plot=graffit(residual,
                 title='residuo',cbar=True)
    
    if save:
        hdu = fits.PrimaryHDU(residual,header=hed)
        hdul=fits.HDUList([hdu])
        hdul.writeto( path + '/' + namef,overwrite=True)
                         
        
    return(model_image,residual,plot)