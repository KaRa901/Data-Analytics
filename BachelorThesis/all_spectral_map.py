import numpy as np
import matplotlib.pyplot as plt
import astropy as ap
from astropy.io import fits
from astropy.convolution import convolve, Gaussian2DKernel

hdul=ap.io.fits.open('lsdcat0138_minicube.fits')
data=hdul[1].data

A=data.mean(axis=0)
gauss_kernel=Gaussian2DKernel(1,1)
smoothed_data_gauss=convolve(A,gauss_kernel)
plt.figure()
ax=plt.figure(1).add_subplot(1,1,1)
ax.set_ylabel('y [pixels]')
ax.set_xlabel('x [pixels]')

plt.imshow(smoothed_data_gauss,cmap='spectral',interpolation='nearest', origin='lower')
plt.colorbar()

B=data[:,71:79,66:74]
B=np.reshape(B,(2750,64))
B_mean=B.mean(axis=1)

plt.figure()
x=np.arange(4750,8187.5,1.25)
y=B_mean
N=np.size(x)

plt.plot(x,y)
