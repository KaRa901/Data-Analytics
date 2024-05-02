#Qwinkel
vlylimit=3.2898419602508E15
lim2=vlya*30
alpha=-1.7
f0=(3E-14/6.5)/vlylimit
Qion=((4*np.pi*(dl_cm_hand**2)*f0)/(h*(vlylimit**(alpha))))*(((1/alpha)*(lim2**alpha))-((1/alpha)*(vlylimit**alpha)))

Qwinkel30=(np.sin((Winkel1*np.pi)/720)**2)*Qion
