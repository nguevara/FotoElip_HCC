fname = {
    "ref": {
        "name": "g.fits",
        "path": "input"
    },
    "out": {
        "residue": {
            "path": "data",
            "name": "residue_g.fits"
        },
        "table": {
            "path": "data",
            "name": "isolist.dat"
        }
    }
}
ellipse_incial = {
    "x0": 1185.0,
    "y0": 1384.0,
    "sma": 100,
    "ellip": 0.47,
    "pa": 50
}
ellipse_incial_0 = {
    "x0": 1185.0,
    "y0": 1384.0,
    "sma": 80,
    "ellip": 0.47,
    "pa": 47
}
guardar = {
    "residue": True,
    "save_iso": True
}
fit_ell_par = {
    "sclip": 2.0,
    "nclip": 0,
    "fflag": 0.9,
    "integrmode": "median",
    "cut": 600,
    "maxs": 900.0,
    "fix": True,
    "step0": 0.08,
    "step1": 10,
    "conver": 0.05,
    "minsma": 1
}
fit_ell_par_0 = {
    "sclip": 3.0,
    "nclip": 5,
    "fflag": 1.0,
    "integrmode": "median",
    "cut": 300,
    "maxs": 900,
    "fix": True,
    "step0": 0.1,
    "step1": 5,
    "conver": 0.1,
    "minsma": 1
}
bkg = {
    "bkg": 658.9486947791165,
    "mode": "mean"
}
mask = {
    "file": "mask.fits",
    "path": "../input",
    "calc": True,
    "nthr": 5.0,
    "fwhm": 5.0,
    "sharp": [
        0.0,
        1.5
    ],
    "roundlim": [
        -2.0,
        2.0
    ],
    "threshold": 75
}
plots = {
    "param_plot": True,
    "mu_plot": True,
    "req": True,
    "n_par": 1.2,
    "n_mu": 1.2,
    "E": 0.146,
    "texp": 100.5,
    "mu0": 28.1247,
    "arcmin": True
}
