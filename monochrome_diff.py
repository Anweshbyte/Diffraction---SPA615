
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
    return np.abs(integral) ** 2

x_values = np.arange(-10, 50, 0.2)
cos_integral_values = np.array([integral_function(cos_integrand, x) for x in x_values])
sin_integral_values = np.array([integral_function(sin_integrand, x) for x in x_values])

monochromatic_intensity = (cos_integral_values + sin_integral_values)
monochromatic_intensity[x_values < 0] = 0

plt.plot(x_values, monochromatic_intensity)
plt.title('500nm')
plt.xlabel('x (m)')
plt.ylabel('Intensity')
plt.grid(True)
folder_path = "plots"
file_name = f"plot {lmda*1e9:.0f}nm.png" 

file_path = os.path.join(folder_path, file_name)
plt.savefig(file_path)

folder_path = "int_values"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_path = os.path.join(folder_path, f"monochromatic {lmda*1e9:.0f}nm")
np.save(file_path, monochromatic_intensity)

plt.show()