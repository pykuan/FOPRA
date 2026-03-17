import numpy as np
import matplotlib.pyplot as plt

filepath = 'data/SampleB_ZnO_002_widerange.txt'

intensity = np.loadtxt(filepath, skiprows=2)[:, 1]
angle = np.linspace(20, 150, len(intensity)) #2theta

i_peaks = np.where(intensity > 10000)
angle_peaks = angle[i_peaks]
# print(angle_peaks[0])

plt.semilogy(angle, intensity)
plt.xlabel('2θ (deg)')
plt.ylabel('Intensity (cps)')
plt.title('')
plt.savefig('fig_01.png')
plt.show()
plt.close()

with open('value.tex', 'a') as f:
    f.write('\n')
    f.write(rf'\newcommand\reportONEangi{{{angle_peaks[0]:.1f}}}' + '\n')
    f.write(rf'\newcommand\reportONEangii{{{angle_peaks[2]:.1f}}}' + '\n')
    f.write(rf'\newcommand\reportONEangiii{{{angle_peaks[4]:.1f}}}' + '\n')
    f.write(rf'\newcommand\reportONEangix{{{angle_peaks[5]:.1f}}}' + '\n')
    f.write(rf'\newcommand\reportONEangx{{{angle_peaks[6]:.1f}}}' + '\n')