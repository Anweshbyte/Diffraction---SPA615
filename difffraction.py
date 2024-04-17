import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel
from scipy.integrate import quad
import os
from params import *

# u_values = np.sqrt(2 / (lmda_min * dist)) * np.linspace(-50, 10, 100000)
x_values = np.linspace(-50,10,100000)
intensity = np.zeros_like(x_values)
poly_intensity = np.zeros_like(x_values)

if BW != 0:
    for i in np.arange(lmda_min, lmda_max, alpha):
        S, C = fresnel(np.sqrt(2 / (i * dist)) * x_values)
        intensity = 0.5 * ((0.5 - C)**2 + (0.5 - S)**2)
        poly_intensity  +=  0.1 * intensity

    folder_path = "int_arr"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"poly-{(lmda_min)*1e9:.0f}-{(lmda_max)*1e9:.0f}-nm")
    np.save(file_path, poly_intensity)


else: 
    S, C = fresnel(np.sqrt(2 / (lmda_min * dist)) * x_values)
    intensity = 0.5 * ((0.5 - C)**2 + (0.5 - S)**2)

    folder_path = "int_arr"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"mono-{(lmda)*1e9:.0f}-nm")
    np.save(file_path, intensity)


plt.plot(x_values, intensity )
plt.title('Lunar Occultation')
plt.xlabel('x (m)')
plt.ylabel('Intensity')
# plt.xlim(-5,2)
plt.grid(True)
plt.show()