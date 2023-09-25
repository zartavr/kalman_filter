import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

noise = norm.rvs(0, 1.2, 1000)
x = np.linspace(0, 2*np.pi, 1000)
y = np.array([])
y_noise = np.array([])
for i in range(0, len(x)):
    y = np.append(y, 20*np.sin(x[i]))
    y_noise = np.append(y_noise, y[i] + noise[i])

plt.figure()
plt.plot(x, y_noise)
plt.plot(x, y)
plt.savefig("fig.jpg")