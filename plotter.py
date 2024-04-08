import os
import numpy as np
import matplotlib.pyplot as plt
from params import *

def generate_plots():
    folder_path = 'int_arr'
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.npy')]
    data_list = []
    labels = []

    for file_name in file_list:
        data = np.load(os.path.join(folder_path, file_name))
        label = file_name[5:-4]  
        data_list.append(data)
        labels.append(label)

    # u_values = np.sqrt(2 / (lmda * dist)) * np.linspace(-50, 10, 100000)
    x_values = np.linspace(-50,10,100000)
    for data, label in zip(data_list, labels):
        plt.plot(x_values, data, label=label)

    plt.xlabel('x (m)')
    plt.ylabel('Intensity of light')
    plt.title('Effect of finite passband')
    plt.legend()
    # plt.xlim(-5, 2)

    folder_path = "plots"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = f"plots.png"
    file_path = os.path.join(folder_path, file_name)
    plt.savefig(file_path)
    plt.close()  # Close the plot to avoid displaying it in Flask app

    return file_path  # Return the path of the saved file

if __name__ == "__main__":
    generate_plots()


