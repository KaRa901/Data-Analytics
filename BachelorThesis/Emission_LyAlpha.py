import numpy as np
import matplotlib.pyplot as plt
import astropy as ap
from astropy.io import fits
from astropy.convolution import convolve, Gaussian2DKernel

hdul=ap.io.fits.open('lsdcat0138_minicube.fits')
data=hdul[1].data
hdul1=ap.io.fits.open('lsdcat0138_mfscube.fits')
mfscube=hdul1[1].data

mfcube=data-mfscube

xc,yc=60,60
l1dla,l2dla=250,290
yy,xx=np.indices(mfcube[0].shape)
rr=np.sqrt((xx-xc)**2+(yy-yc)**2)
mfmaxrad=5.5
rsel=rr<mfmaxrad
mfcube[l1dla:l2dla,rsel]=0

mfsmodcube=data-mfcube
