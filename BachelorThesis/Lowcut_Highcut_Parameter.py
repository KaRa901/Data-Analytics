hdul=ap.io.fits.open('lsdcat0138_mfscube.fits')
data=hdul[1].data
data_narrow=data[272:280,:,:]
A=data_narrow.sum(axis=0) #oder sum für die Surface Brightness über die Wellenlänge integriert

gauss_kernel=Gaussian2DKernel(2.13,2.13)
smoothed_data_gauss=convolve(A,gauss_kernel)
shaped_data=np.reshape(smoothed_data_gauss, 14400)
lowhighcut_data=np.clip(shaped_data, 0, 5)                   #fill in the vmin/vmax function
trans_data=np.power(lowhighcut_data,0.5)
resh_smoothed_data_gauss=np.reshape(trans_data, (120, 120))

plt.figure()
ax=plt.figure(1).add_subplot(1,1,1)
plt.yticks([0,30,60,90,120],['0\'\'','6\'\'','12\'\'','18\'\'','24\'\''])
plt.xticks([0,30,60,90,120],['0\'\'','6\'\'','12\'\'','18\'\'','24\'\''])
ax.set_ylabel(u'$\Delta\u03B4_{2000}$')
ax.set_xlabel(u'$\Delta\u03B1_{2000}$')

plt.imshow(resh_smoothed_data_gauss,cmap='Blues',interpolation='nearest', origin='lower')
