import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu)**2 / (2 * sigma**2))

def fit(angle, intensity):
    A0 = intensity.max()
    mu0 = angle[np.argmax(intensity)]
    sig0 = (angle.max()-angle.min())/10
    
    params, cov = curve_fit(gaussian, angle, intensity, p0=[A0, mu0, sig0])
    A, mu, sigma = params
    return A, mu, sigma

filepath = 'data/SampleA_ZnO_002_2thetaomega.txt'
theta = 34.6346 #2theta (dag)

intensity = np.loadtxt(filepath, skiprows=2)[:, 1]
angle = np.linspace(theta-0.2, theta+0.2, len(intensity)) *np.pi/180 #2theta (rad)

A = fit(angle, intensity)[0]
mu = fit(angle, intensity)[1]
sig = fit(angle, intensity)[2]
intensity_fit = gaussian(angle, A, mu, sig)

angle_fwhm_firstindex = np.where(intensity_fit >= intensity_fit.max()/2)[0][0]
angle_fwhm_lastindex = np.where(intensity_fit >= intensity_fit.max()/2)[0][-1]
FWHM_2theta = angle[angle_fwhm_lastindex] - angle[angle_fwhm_firstindex]
print(f'FWHM = {FWHM_2theta}')

# eq.41
theta = theta *np.pi/180
wavelength = 1.54059 *10**-10
lz = 0.9*wavelength/(FWHM_2theta*np.cos(theta/2))
print(f'lz = {lz}')

plt.plot(angle, intensity, label='data', color='black')
plt.plot(angle, intensity_fit, label='Gaussian fit', linewidth=1)
plt.plot(np.linspace(angle[angle_fwhm_lastindex], angle[angle_fwhm_firstindex], 100), np.linspace(intensity_fit[angle_fwhm_firstindex], intensity_fit[angle_fwhm_firstindex], 100), label='FWHM')
plt.xlabel('2θ (rad)')
plt.ylabel('Intensity (cps)')
plt.title('')
plt.legend()
plt.savefig('fig_02.png')
plt.show()
plt.close()

