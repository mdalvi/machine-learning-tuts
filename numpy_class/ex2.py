'''
Demonstrate the central limit theorem (CLT)
Recall:
    If Y = X1 + X2 + X3 + ... + XN
    where X are IID (independent, identically distributed)
    Then as N -> infinity, Y -> Gaussian distribution

Use the uniform distribution as your base for X
Use N = 1000 (or higher if you want)
Then draw 1000 Y's (or more if you want)
Plot histogram of Y's -> should be a "bell curve"
Bonus: find the expected mean and variance of Y

'''

import numpy as np
import matplotlib.pyplot as plt

N = 100000
draw_Y = 1000
uniform = np.random.rand(N, draw_Y)
Y = np.sum(uniform, axis=1)

print('The mean of gaussian distribution is: {0}'.format(Y.mean()))
print('The variance of gaussian distribution is: {0}'.format(Y.var()))
print('The standard deviation of gaussian distribution is: {0}'.format(Y.std()))

plt.hist(Y, bins=100)
plt.show()

