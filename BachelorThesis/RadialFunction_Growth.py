#Radial Function of growth of Nebula B LY ALpha Emission
import numpy as np
import matplotlib.pyplot as plt
import astropy as ap
from astropy.io import fits
from astropy.convolution import convolve, Gaussian2DKernel

hdul=ap.io.fits.open('lsdcat0138_mfscube.fits')
data=hdul[1].data

import numpy.ma as ma
data_subcube=data[272:280,45:62,60:76]
e_sub=np.identity(16)
diag_data=data_subcube*e_sub
diag_data_shaped=np.reshape(diag_data,(8,256))
diag_reduced=diag_data_shaped[:,::17]
diag_reduced_mean=np.mean(diag_reduced, axis=0)
y=diag_reduced_mean
x=np.arange(0,4.5,16)

plt.figure()
ax=plt.figure().add_subplot(1,1,1)
plt.grid()
ax.set_ylabel('Mean Flux    [$x 10^{-20} erg*cm^{-2}*s^{-1}]$')
ax.set_xlabel('Radius [r]')
ax.axhline(y=0.4, linestyle='--', color='red')
ax.arrow(8,0.4,0,0.1, head_width=0.5, head_length=0.02, linewidth='0.5', linestyle='-',color='red')
ax.minorticks_on()
plt.plot(x,y,'b--o', color='black')
