import numpy as np
import matplotlib.pyplot as plt

filepath_z = 'data/SampleA_ZnO_112_pi.txt'
filepath_a = 'data/SampleA_Al2O3_112_pi.txt'

intensity_z = np.loadtxt(filepath_z, skiprows=2)[:, 1]
angle_z = np.linspace(0, 360, len(intensity_z)) #phi
intensity_a = np.loadtxt(filepath_a, skiprows=2)[:, 1]
angle_a = np.linspace(0, 360, len(intensity_a)) #phi

peaks_z = np.where(intensity_z > 600)
print(angle_z[peaks_z])
peaks_a = np.where(intensity_a > 600)
print(angle_a[peaks_a])

plt.plot(angle_z, intensity_z, label='ZnO (112)')
plt.plot(angle_a, intensity_a, label='Al2O3 (113)')
plt.xlabel('φ (deg)')
plt.ylabel('Intensity (cps)')
plt.title('')
plt.legend()
plt.savefig('fig_06.png')
plt.show()
plt.close()
    
# Plot('data/SampleA_ZnO_112_pi.txt', 'fig_06_ZnO_112.png')
# Plot('data/SampleA_Al2O3_112_pi.txt', 'fig_06_Al2O3_113.png')