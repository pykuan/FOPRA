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

filepath = 'data/SampleA_ZnO_101_omega.txt'
omega = 18.1463

intensity = np.loadtxt(filepath, skiprows=2)[:, 1]
angle = np.linspace(omega-1.5, omega+1.5, len(intensity)) *np.pi/180 #2omega (rad)

A = fit(angle, intensity)[0]
mu = fit(angle, intensity)[1]
sig = fit(angle, intensity)[2]
intensity_fit = gaussian(angle, A, mu, sig)

angle_fwhm_firstindex = np.where(intensity_fit >= intensity_fit.max()/2)[0][0]
angle_fwhm_lastindex = np.where(intensity_fit >= intensity_fit.max()/2)[0][-1]
FWHM_omega = angle[angle_fwhm_lastindex] - angle[angle_fwhm_firstindex]
print(f'FWHM = {FWHM_omega}')

# eq.46
omega = omega *np.pi/180
wavelength = 1.54059 *10**-10
a = 3.2475 *10**-10 #b_edge
dislocation_edge = FWHM_omega**2/(4.35*a**2)
print(f'edge dislocation density = {dislocation_edge}')

lower_boundary = 0 #int(len(intensity)/2-200)
upper_boundary = len(intensity) #int(len(intensity)/2+200)
plt.plot(angle[lower_boundary:upper_boundary], intensity[lower_boundary:upper_boundary], label='data', color='black')
plt.plot(angle[lower_boundary:upper_boundary], intensity_fit[lower_boundary:upper_boundary], label='Gaussian fit', linewidth=1)
plt.plot(np.linspace(angle[angle_fwhm_lastindex], angle[angle_fwhm_firstindex], 100), np.linspace(intensity_fit[angle_fwhm_firstindex], intensity_fit[angle_fwhm_firstindex], 100), label='FWHM')
plt.xlabel('ω (rad)')
plt.ylabel('Intensity (cps)')
plt.title('')
plt.legend()
plt.savefig('fig_05.png')
plt.show()
plt.close()

