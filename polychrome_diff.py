
import numpy as np
import matplotlib.pyplot as plt
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

x_values = np.arange(-10, 50, 0.2)
polychromatic_intensity = np.zeros_like(x_values)

for i in np.arange(lmda_min, lmda_max, alpha):
    cos_integral_values = np.array([integral_function(cos_integrand, x) for x in x_values])
    sin_integral_values = np.array([integral_function(sin_integrand, x) for x in x_values])
    result_values = 0.1*(cos_integral_values + sin_integral_values)
    result_values[x_values < 0] = 0  
    polychromatic_intensity  += result_values

plt.plot(x_values, polychromatic_intensity )
plt.title('Combined Intensity')
plt.xlabel('x (m)')
plt.ylabel('Intensity')
plt.grid(True)

folder_path = "plots"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_name = f"plot {(lmda_min)*1e9:.0f} - {(lmda_max)*1e9:.0f}nm.png"
file_path = os.path.join(folder_path, file_name)
plt.savefig(file_path)

folder_path = "int_values"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, f"polychromatic {(lmda_min)*1e9:.0f} - {(lmda_max)*1e9:.0f}nm")
np.save(file_path, polychromatic_intensity)

plt.show()