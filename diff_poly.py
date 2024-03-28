
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel
from scipy.integrate import quad
import os
from params import *

def cos_integrand(t):
    return np.cos(np.pi * t **2 / (dist * lmda))

def sin_integrand(t):
    return np.sin(np.pi * t **2 / (dist * lmda))

def integral_function(integrand_func, x):
    integral, _ = quad(integrand_func, 0, x)
    return (np.abs(integral)) ** 2

u_values = np.sqrt(2 / (lmda_min * dist)) * np.linspace(-50, 10, 1000)
polychromatic_intensity = np.zeros_like(u_values)

for i in np.arange(lmda_min, lmda_max, alpha):
    u_values = np.sqrt(2 / (i * dist)) * np.linspace(-50, 10, 1000)
    S, C = fresnel(u_values)
    intensity = 0.5 * ((0.5 - C)**2 + (0.5 - S)**2)
    polychromatic_intensity  += 0.1 * intensity

plt.plot(u_values, polychromatic_intensity )
plt.title('Combined Intensity')
plt.xlabel('x (m)')
plt.ylabel('Intensity')
plt.grid(True)

folder_path = "int_arr"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, f"poly-{(lmda_min)*1e9:.0f}-{(lmda_max)*1e9:.0f}-nm")
np.save(file_path, polychromatic_intensity)

plt.show()