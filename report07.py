import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
from scipy.interpolate import griddata


# def gaussian(xz, A, x0, z0, sig_x, sig_z, theta):
#     x, z = xz
#     x0 = float(x0)
#     z0 = float(z0)
#     a = (np.cos(theta)**2) / (2 * sig_x**2) + (np.sin(theta)**2) / (2 * sig_z**2)
#     b = -(np.sin(2 * theta)) / (4 * sig_x**2) + (np.sin(2 * theta)) / (4 * sig_z**2)
#     c = (np.sin(theta)**2) / (2 * sig_x**2) + (np.cos(theta)**2) / (2 * sig_z**2)
#     g = A * np.exp(-(a * ((x - x0)**2) + 2 * b * (x - x0) * (z - z0) + c * ((z - z0)**2)))
#     return g.ravel()

# def fit(qx, qz, intensity):
#     A = intensity.max()
#     x0 = qx[np.argmax(intensity)]
#     z0 = qz[np.argmax(intensity)]
#     sig_x = 1
#     sig_z = 1
#     theta = 0
#     params, cov = curve_fit(gaussian, (qx, qz), intensity, p0=[A, x0, z0, sig_x, sig_z, theta])
#     A_, x0_, z0_, sig_x_, sig_z_, theta_ = params
#     return A_, x0_, z0_, sig_x_, sig_z_, theta_

filepath = 'data/SampleB_ZnO_205_RSM.txt'

# a = 0.32475
# c = 0.52024 #nm
wavelength = 0.154059 #nm
h, k, l = 2, 0, 5

qx = np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 0] /(2/wavelength)
qz = np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 1] /(2/wavelength)
intensity = np.loadtxt(filepath, skiprows=2, encoding='utf-8')[:, 2]

# A, x0, z0, sig_x, sig_z, theta = fit(qx, qz, intensity)
# intensity_fit = gaussian((qx, qz), A, x0, z0, sig_x, sig_z, theta)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(qx, qz, intensity, label='data', s=1)
# # ax.plot_trisurf(qx, qz, intensity_fit, alpha=0.5)
# # ax.scatter([], [], [], label='Gaussian fit')
# ax.set_xlabel('qx')
# ax.set_ylabel('qz')
# ax.set_zlabel('Intensity (cps)')
# ax.set_title('')
# ax.legend()

QX, QZ = np.meshgrid(np.linspace(qx.min(), qx.max(), 200), np.linspace(qz.min(), qz.max(), 200))
intensity_grid = griddata((qx, qz), intensity, (QX, QZ), method='linear')
intensity_ratio = intensity_grid / np.nanmax(intensity_grid)
intensity_ratio = np.where(np.isnan(intensity_ratio) | (intensity_ratio <= 0), np.nan, intensity_ratio)
intensity_grid = np.log10(intensity_ratio)
qx0 = qx[np.argmax(intensity)]
qz0 = qz[np.argmax(intensity)]

a = (1/qx0) * (wavelength*h/np.sqrt(3))
c = (1/qz0) * (wavelength*l/2)
print(abs(a))
print(abs(c)) #nm

plt.contourf(QX, QZ, intensity_grid, levels=20, cmap='viridis')
plt.scatter(qx0, qz0, color='red', label='peak', s=1)
plt.colorbar(label='log10(I/Imax)')
plt.xlabel('qx')
plt.ylabel('qz')
plt.legend()
plt.savefig('fig_07.png')
plt.show()
plt.close()

