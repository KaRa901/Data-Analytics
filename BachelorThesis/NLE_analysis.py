import numpy as np
import matplotlib.pyplot as plt
import astropy as ap
from astropy.io import fits
from astropy.convolution import convolve, Gaussian2DKernel

hdul=ap.io.fits.open('lsdcat0138_minicube.fits')
data=hdul[1].data
header=hdul[1].header
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

data_narrow=mfsmodcube[272:280,:,:]
A=data_narrow.sum(axis=0)*1.25*2.5 #sum für Surface Brightness, 1.25 und 2.5 für px Anpassung
gauss_kernel=Gaussian2DKernel(2.13,2.13)
smoothed_data_gauss=convolve(A,gauss_kernel)
shaped_data=np.reshape(smoothed_data_gauss, 14400)
lowhighcut_data=np.clip(shaped_data, 0, 15)                   #fill in the vmin/vmax function
trans_data=np.power(lowhighcut_data,0.55)
resh_smoothed_data_gauss=np.reshape(trans_data, (120, 120))

x_vals = np.linspace(0, 119, 120)
y_vals = np.linspace(0, 119, 120)
X, Y = np.meshgrid(x_vals, y_vals)
Z=resh_smoothed_data_gauss
plt.figure()
ax=plt.figure(1).add_subplot(1,1,1)
plt.yticks([0,30,60,90,120],['12\'\'','6\'\'','0\'\'','6\'\'','12\'\''])
plt.xticks([0,30,60,90,120],['12\'\'','6\'\'','0\'\'','6\'\'','12\'\''])
ax.set_ylabel(u'$\Delta\u03B4_{2000}$')
ax.set_xlabel(u'$\Delta\u03B1_{2000}$')
ax.minorticks_on()
ax.arrow(110,100,0,10, head_width=2, head_length=2, linewidth='2', linestyle='-',color='black')
ax.arrow(110,100,-10,0, head_width=2, head_length=2, linewidth='2', linestyle='-',color='black')
ax.arrow(10,10,0,13.158, head_width=0.001, head_length=0.001, linewidth='1', linestyle='-',color='black')
plt.text(112,110,'N', size=13)
plt.text(97,93,'E', size=13)
plt.text(12,20,'20 kpc', size=8, rotation=90)
plt.text(90,30,'Nebula B', size=10)
plt.text(50,80,'Nebula A', size=10)
cax=plt.imshow(Z,cmap='Blues',interpolation='nearest', origin='lower')
plt.contour(X,Y,Z, linewidths=0.5)
cbar=plt.colorbar(cax, ticks=[0,1,2,3,4])
cbar.ax.set_yticklabels([0,1,3.6,7.4,12.4])
cbar.set_label(u'$SB_{Ly\u03B1}$  [$x 10^{-19} erg*cm^{-2}*s^{-1}*arcsec^{-2}]$')

