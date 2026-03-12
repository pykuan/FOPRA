import numpy as np
import matplotlib.pyplot as plt

filepath = 'data/SampleB_ZnO_002_widerange.txt'

intensity = np.loadtxt(filepath, skiprows=2)[:, 1]
angle = np.linspace(20, 150, len(intensity)) #2theta

peaks = np.where(intensity > 10000)
print(angle[peaks])

plt.semilogy(angle, intensity)
plt.xlabel('2θ (deg)')
plt.ylabel('Intensity (cps)')
plt.title('')
plt.savefig('fig_01.png')
plt.show()
plt.close()