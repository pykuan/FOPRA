import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

filepath = 'data/SampleC_ZnO_006_2thetaomega_FromOtherGroup.txt'

def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu)**2 / (2 * sigma**2))

def fit(angle, intensity):
    A0 = intensity.max()
    mu0 = angle[np.argmax(intensity)]
    sig0 = (angle.max()-angle.min())/10
    
    params, cov = curve_fit(gaussian, angle, intensity, p0=[A0, mu0, sig0])
    A, mu, sigma = params
    return A, mu, sigma, cov

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

A = fit(qz, intensity)[0]
mu = fit(qz, intensity)[1]
sig = fit(qz, intensity)[2]
cov = fit(qz, intensity)[3]
err = np.sqrt(np.diag(cov))
intensity_fit = gaussian(qz, A, mu, sig)
qz0 = mu
dqz0 = err[1]

qz0_rlu = qz0 / (4*np.pi/wavelength)

c = (1/qz0_rlu) * (wavelength*l/2)
print(abs(c)) #nm

c_zno = 0.52024 #nm
x = (c_zno - c) / 0.017
print(x)

dx = dqz0 * (2*np.pi*l)/(0.17*qz0**2) #error propagation
print(dx)

plt.plot(qz, intensity, color='black', label='data')
plt.plot(qz, gaussian(qz, A, mu, sig), color='tab:blue', label='Gaussian fit')
plt.scatter(qz0, gaussian(qz0, A, mu, sig), color='red', label='peak')
plt.xlabel(r'q$_\perp$ (nm$^{-1}$)')
plt.ylabel('Intensity (cps)')
plt.legend()
plt.title('')
plt.savefig('fig_08.png')
plt.show()
plt.close()

with open('value.tex', 'a') as f:
    f.write('\n')
    f.write(rf'\renewcommand\reportEIGHTc{{{c:.4f}}}' + '\n')
    f.write(rf'\renewcommand\reportEIGHTx{{{x:.4f}}}' + '\n')
    f.write(rf'\renewcommand\reportEIGHTdx{{{dx*10**5:.4f}}}' + '\n')