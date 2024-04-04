import os
import numpy as np
import matplotlib.pyplot as plt

folder_path = 'int_values'

file_list = [f for f in os.listdir(folder_path) if f.endswith('.npy')]
data_list = []
labels = []

for file_name in file_list:
    data = np.load(os.path.join(folder_path, file_name))
    label = file_name[14:-4]  
    data_list.append(data)
    labels.append(label)

for data, label in zip(data_list, labels):
    plt.plot(data, label=label)

plt.xlabel('X (m)')
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


