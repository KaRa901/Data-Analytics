import numpy as np
import matplotlib.pyplot as plt
import astropy as ap
from astropy.io import fits
from astropy.convolution import convolve, Gaussian2DKernel

hdul=ap.io.fits.open('lsdcat0138_minicube.fits')
data=hdul[1].data
