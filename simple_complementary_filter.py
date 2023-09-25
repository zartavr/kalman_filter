import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

noise = norm.rvs(0, 0.05, 1000)

angle_sample_1 = np.linspace(0, np.pi/2, 1000)
angle_sample_2 = np.linspace(np.pi/2, 0, 1000)

# angle = np.append(angle_sample_1, angle_sample_2)
angle = angle_sample_1
noise_angle = angle + noise

Kstab = 0.2

filt_angle = np.array([noise_angle[0]])
for k in range(1, len(noise_angle)):
    filt_angle = np.append(filt_angle, Kstab * noise_angle[k] + (1-Kstab)*filt_angle[k-1])

plt.figure()
plt.plot(noise_angle)
plt.plot(filt_angle)
plt.plot(angle)
plt.legend(["Noise", "Filt", "Meas"])
plt.savefig("fig1")
