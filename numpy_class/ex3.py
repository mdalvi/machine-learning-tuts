'''
Load in the MNIST dataset, and plot the mean (average) image for each digit class (0....9)
Recall: mean = sum / number of elements

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# MNIST data-set downloaded form https://www.kaggle.com/c/digit-recognizer/data
mnist_df = pd.read_csv('../large_files/train.csv')

digits = []
for i in range(10):
    # Below statement filters the rows from the mnist dataframe based on the label and then using loc,
    # filters the columns such that result does not contain label column and then converts it
    # to numpy array
    # https://stackoverflow.com/questions/29763620/how-to-select-all-columns-except-one-column-in-pandas
    digits.append(mnist_df[mnist_df['label'] == i].loc[:, mnist_df.columns != 'label'].as_matrix())

for i in range(10):
    #Below statement sums the pixes intensities along 0th axis and then divides the valus with number of records to find the mean pixes intensity , thus resizing to 28 by 28 we get mean image
    plt.imshow((np.sum(digits[i], axis=0) / digits[i].shape[0]).reshape(28, 28), cmap='gray')  # setting colormap to gray
    plt.show()