import os
import numpy as np
import matplotlib.pyplot as plt
from params import *

folder_path = 'int_arr'

file_list = [f for f in os.listdir(folder_path) if f.endswith('.npy')]
data_list = []
labels = []

for file_name in file_list:
    data = np.load(os.path.join(folder_path, file_name))
    label = file_name[5:-4]  
    data_list.append(data)
    labels.append(label)

u_values = np.sqrt(2 / (lmda * dist)) * np.linspace(-50, 10, 1000)
for data, label in zip(data_list, labels):
    plt.plot(u_values, data, label=label)

plt.xlabel('u (Fresnel Number)')
plt.ylabel('Intensity of light')
plt.title('Effect of finite passband')
plt.legend()

folder_path = "plots"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_name = f"Combined plots.png"
file_path = os.path.join(folder_path, file_name)
plt.savefig(file_path)

plt.show()


