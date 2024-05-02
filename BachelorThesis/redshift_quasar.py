#calculate the redshift of the quasar with line CIV at 1549.48

import numpy.ma as ma
data_aperture=data[1320:1480,55:66,55:66]
zz,yy,xx=np.indices([160,11,11], dtype='float')
radius=(((yy-5)**2+(xx-5)**2)**0.5)+(zz-zz)
mask=radius>5.5
circular_data=ma.masked_where(mask,data_aperture)
circular_data_shaped=np.reshape(circular_data,(250,121))
circular_mean=circular_data_shaped.mean(axis=1)
x=np.arange(6400,6600,1.25)
y=circular_mean
plt.figure()
plt.plot(x,y)
ax=plt.figure().add_subplot(1,1,1)
plt.grid()
ax.set_ylabel('$F_/lambda$    [$x 10^{-20} erg*Å^{-1}*cm^{-2}*s^{-1}]$')
ax.set_xlabel('Wavelength [Å]')
ax.minorticks_on()
