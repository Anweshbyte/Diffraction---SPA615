import numpy as np
from scipy.special import fresnel
from scipy.signal import convolve
import matplotlib.pyplot as plt
import os
from params import *
radius =np.sqrt(2 / (lmda * dist)) * 19/2

u_values = np.sqrt(2 / (lmda * dist)) * np.linspace(-50, 10, 1000)
S, C = fresnel(u_values)
intensity = 0.5 * ((0.5 - C)**2 + (0.5 - S)**2)

# x_values = np.linspace(-radius, radius, len(u_values))
# kernel = 2 * np.sqrt(radius**2 - (x_values)**2)
# convolved_intensity = convolve(intensity, kernel, mode='same')

plt.figure(figsize=(10, 5))
plt.plot(u_values, intensity, label="Fresnel Intensity")
# plt.plot(u_values, kernel, label="Convolved Intensity")
plt.xlabel("Fresnel Number (u)")
plt.ylabel("Normalized Intensity")
plt.legend()
plt.grid(True)

folder_path = "int_arr"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_path = os.path.join(folder_path, f"mono-{(lmda)*1e9:.0f}-nm")
np.save(file_path, intensity)
plt.show()
