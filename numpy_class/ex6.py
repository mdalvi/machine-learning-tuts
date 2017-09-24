'''
Generate and plot this dataset (XOR)
Recall:
    0 XOR 0 = 0
    0 XOR 1 = 1
    1 XOR 0 = 1
    1 XOR 1 = 0
'''

import numpy as np
import matplotlib.pyplot as plt

data_set_x_y = np.random.randint(low=0, high=2, size=(5000, 2))

# https://stackoverflow.com/questions/14562991/python-equivalent-of-sum-using-xor
xor_labels = list(map(lambda a, b: a ^ b, data_set_x_y[:, 0], data_set_x_y[:, 1]))

# noise = np.random.uniform(low=-1.0, high=0, size=5000)
x = data_set_x_y[:, 0] + np.random.uniform(low=-1.0, high=0, size=5000)
y = data_set_x_y[:, 1] + np.random.uniform(low=-1.0, high=0, size=5000)

# https://stackoverflow.com/questions/43090817/matplotlib-scatter-plot-change-color-based-on-value-on-list
plt.scatter(x, y, c=xor_labels, cmap='seismic', marker='o')
plt.show()
