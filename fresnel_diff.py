
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

# Generate x values
x_values = np.arange(-10, 50, 0.2)

# Calculate the integral values
cos_integral_values = np.array([integral_function(cos_integrand, x) for x in x_values])
sin_integral_values = np.array([integral_function(sin_integrand, x) for x in x_values])

# Calculate the result
result_values = (cos_integral_values + sin_integral_values)

# Set intensity before knife edge to zero
result_values[x_values < 0] = 0

# Plot the result
plt.plot(x_values, result_values)
plt.title('500nm')
plt.xlabel('x (m)')
plt.ylabel('Intensity')
plt.grid(True)
folder_path = "plot"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

img = f"fresnel_diffraction_plot_{lmda*1e9:.6f}nm.png"
plt.savefig(img)
plt.show()











# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import quad
# from params import *

# def cos_integrand(t):
#     return np.cos(np.pi * t**2 / (dist * lmda))

# def sin_integrand(t):
#     return np.sin(np.pi * t**2 / (dist * lmda))

# def integral_function(integrand_func, x):
#     integral, _ = quad(integrand_func, -np.inf, x)
#     return np.abs(integral)**2

# x_values = np.arange(0, 50, 0.2)

# cos_integral_values = np.array([integral_function(cos_integrand, x) for x in x_values])
# sin_integral_values = np.array([integral_function(sin_integrand, x) for x in x_values])

# result_values = cos_integral_values + sin_integral_values

# plt.plot(x_values, result_values)
# plt.title('|cos(x)|^2 + |sin(x)|^2 vs. x')
# plt.xlabel('x')
# plt.ylabel('|cos(x)|^2 + |sin(x)|^2')
# plt.grid(True)
# plt.show()

