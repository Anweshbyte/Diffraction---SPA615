import numpy as np
from scipy.special import fresnel
import matplotlib.pyplot as plt
import os
from params import *

u_values = np.linspace(-5, 5, 1000)
S, C = fresnel(u_values)

intensity = 0.5 * ((0.5 - C)**2 + (0.5 - S)**2)

plt.plot(u_values, intensity, label="Fresnel Intensity")
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
