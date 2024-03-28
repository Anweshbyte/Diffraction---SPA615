
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

result_values = (cos_integral_values + sin_integral_values)
result_values[x_values < 0] = 0

plt.plot(x_values, result_values)
plt.title('500nm')
plt.xlabel('x (m)')
plt.ylabel('Intensity')
plt.grid(True)
folder_path = "plot"
file_name = f"plot_{lmda*1e9:.0f}nm.png" 

file_path = os.path.join(folder_path, file_name)
plt.savefig(file_path)
plt.show()