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

def Calculate_dxy_dislocation(filepath, omega, domega, theta):
    
    print(filepath)

    intensity = np.loadtxt(filepath, skiprows=2)[:, 1]
    angle = np.linspace(omega-domega, omega+domega, len(intensity)) *np.pi/180 #omega (rad)

    A = fit(angle, intensity)[0]
    mu = fit(angle, intensity)[1]
    sig = fit(angle, intensity)[2]
    intensity_fit = gaussian(angle, A, mu, sig)

    angle_fwhm_firstindex = np.where(intensity_fit >= intensity_fit.max()/2)[0][0]
    angle_fwhm_lastindex = np.where(intensity_fit >= intensity_fit.max()/2)[0][-1]
    FWHM_omega = angle[angle_fwhm_lastindex] - angle[angle_fwhm_firstindex]
    print(f'FWHM = {FWHM_omega}')

    # eq.43
    omega = omega *np.pi/180
    wavelength = 1.54059 *10**-10
    lxy = 0.9*wavelength/(FWHM_omega*np.sin(theta))
    print(f'lxy = {lxy}')

    c = 5.2024 *10**-10 #b_screw
    dislocation_screw = FWHM_omega**2/(4.35*c**2)
    print(f'screw dislocation density = {dislocation_screw}')


    lower_boundary = 0 #int(len(intensity)/2-200)
    upper_boundary = len(intensity) #int(len(intensity)/2+200)
    plt.plot(angle[lower_boundary:upper_boundary], intensity[lower_boundary:upper_boundary], label='data', color='black')
    plt.plot(angle[lower_boundary:upper_boundary], intensity_fit[lower_boundary:upper_boundary], label='Gaussian fit', linewidth=1)
    plt.plot(np.linspace(angle[angle_fwhm_lastindex], angle[angle_fwhm_firstindex], 100), np.linspace(intensity_fit[angle_fwhm_firstindex], intensity_fit[angle_fwhm_firstindex], 100), label='FWHM')
    plt.xlabel('ω (rad)')
    plt.ylabel('Intensity (cps)')
    plt.title('')
    plt.legend()
    plt.savefig('fig_04.png')
    plt.show()
    plt.close()
    
Calculate_dxy_dislocation(filepath='data/SampleA_ZnO_002_omega.txt', omega=17.1784, domega=0.5, theta=34.4326/2 *np.pi/180)
Calculate_dxy_dislocation(filepath='data/SampleB_ZnO_002_omega.txt', omega=17.2270, domega=0.05, theta=34.4498/2 *np.pi/180)