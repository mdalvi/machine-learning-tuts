'''
Hopefully you noticed the last 3 datasets all had the exact same structure:

x1      x2      y
0.1     0.3     0
0.5     -0.2    1
...

Take any of the datasets you previously generated, and save it to CSV with these headers, using Pandas
(Use Pandas documentation)

'''

import numpy as np
import pandas as pd

data_set_x_y = np.random.randint(low=0, high=2, size=(5000, 2))

# https://stackoverflow.com/questions/14562991/python-equivalent-of-sum-using-xor
xor_labels = list(map(lambda a, b: a ^ b, data_set_x_y[:, 0], data_set_x_y[:, 1]))

# noise = np.random.uniform(low=-1.0, high=0, size=5000)
x = data_set_x_y[:, 0] + np.random.uniform(low=-1.0, high=0, size=5000)
y = data_set_x_y[:, 1] + np.random.uniform(low=-1.0, high=0, size=5000)

# https://stackoverflow.com/questions/29978241/how-do-i-convert-a-numpy-array-to-pandas-dataframe
df = pd.DataFrame({'x1': x, 'x2': y, 'y': xor_labels})

# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv
df.to_csv(path_or_buf='ex9_csv.csv', sep='\t', encoding='utf-8', index=False)
