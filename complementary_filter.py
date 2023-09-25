import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def rad(degree):
    return degree*np.pi/180


meas_noise = norm.rvs(0.50, 0.05, 1000)

noise = norm.rvs(0, 1, 1000)

omega = 0.1/180*np.pi # rad per sec
gyro1 = np.linspace(0, 0.02, 200)
gyro2 = np.linspace(0.04, -0.05, 200)
gyro3 = np.linspace(0, 0.02, 600)

gyro = np.concatenate((gyro1, gyro2, gyro3))

Kstab = 0.022
Kstab_acc = 0.1


angle =np.array([20])
angle_noise =np.array([angle[0] + noise[0]])
angle_filt =np.array([angle_noise[0]])
angle_filt_acc =np.array([angle_noise[0]])
for k in range(1, len(gyro)):
    angle_noise = np.append(angle_noise, angle[k-1] + gyro[k] + noise[k])
    angle = np.append(angle, angle[k-1] + gyro[k])
    angle_filt = np.append(angle_filt, Kstab * angle_noise[k] + (1-Kstab)*(angle_filt[k-1] + gyro[k-1]))
    angle_filt_acc = np.append(angle_filt_acc, Kstab_acc * angle_noise[k] + (1-Kstab_acc)*(angle_filt_acc[k-1]))


plt.figure()
plt.plot(angle_noise)
plt.plot(angle_filt_acc)
plt.plot(angle_filt)
plt.plot(angle)
plt.legend(["angle + noise", "complementary filter accel", "complementary filter accel + gyro", "angle"])
plt.xlabel(r"tilt angle, $\degree$")
plt.ylabel(r"time, s")
plt.savefig("fig1")
