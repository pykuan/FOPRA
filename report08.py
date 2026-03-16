import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from scipy.interpolate import griddata

filepath = 'data/SampleC_ZnO_006_2thetaomega_FromOtherGroup.txt'

# a = 0.32475
# c = 0.52024 #nm
wavelength = 0.154059 #nm
kin = 2*np.pi/wavelength
h, k, l = 0, 0, 6

angle = np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 0] #deg
intensity = np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 1]

qz = kin * np.sin(angle/2 *np.pi/180) * 2

qz0 = qz[np.argmax(intensity)]

c = (1/qz0) * (wavelength*l/2)
print(abs(c)) #nm #0.0063

c_zno = 0.52024 #nm
x = (c_zno - c) / 0.017
print(x) #18.438

plt.plot(qz, intensity)
plt.scatter(qz0, intensity.max(), color='red', label='peak')
plt.xlabel('qz (nm-1)')
plt.ylabel('Intensity (cps)')
plt.legend()
plt.title('')
plt.savefig('fig_08.png')
plt.show()
plt.close()



