import numpy as np
import matplotlib
import matplotlib.pyplot as plt

filepath = 'data/SampleC_ZnO_006_2thetaomega_FromOtherGroup.txt'

# a = 0.32475
# c = 0.52024 #nm
wavelength = 0.154059 #nm
kin = 2*np.pi/wavelength
h, k, l = 0, 0, 6

two_theta_0_deg = 126.5390
omega_0_deg = 63.5835

intensity = np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 1]
two_theta_deg = np.linspace(two_theta_0_deg-0.2, two_theta_0_deg+0.2, len(intensity)) #np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 0] #deg
omega_deg = np.linspace(omega_0_deg-0.2, omega_0_deg+0.2, len(intensity))
two_theta_rad = two_theta_deg *np.pi/180
omega_rad = omega_deg *np.pi/180

qz = kin * (np.sin(two_theta_rad-omega_rad) + np.sin(omega_rad))

qz0 = qz[np.argmax(intensity)]
qz0_rlu = qz0 / (4*np.pi/wavelength)

c = (1/qz0_rlu) * (wavelength*l/2)
print(abs(c)) #nm #0.5175

c_zno = 0.52024 #nm
x = (c_zno - c) / 0.017
print(x) #0.1593

plt.plot(qz, intensity)
plt.scatter(qz0, intensity.max(), color='red', label='peak')
plt.xlabel(r'q$_\perp$ (nm$^{-1}$)')
plt.ylabel('Intensity (cps)')
plt.legend()
plt.title('')
plt.savefig('fig_08.png')
plt.show()
plt.close()

with open('value.tex', 'a') as f:
    f.write(rf'\newcommand\reportEIGHTc{{{c:.4f}}}' + '\n')
    f.write(rf'\newcommand\reportEIGHTx{{{x:.4f}}}' + '\n')