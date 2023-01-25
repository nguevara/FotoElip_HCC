from photutils.background import Background2D, MedianBackground,MeanBackground

#%%


def bkg(ref,mode='mean'):
    if mode=='mean':
        bkg_estimator =  MeanBackground()
    elif mode=='median':
        bkg_estimator = MedianBackground()
    bkg = Background2D(ref, (50, 50), filter_size=(3, 3),
                       bkg_estimator=bkg_estimator)
    return bkg.background_median