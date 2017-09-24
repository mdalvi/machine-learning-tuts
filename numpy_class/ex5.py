'''
Write a function that tests whether or not a matrix is symmetric, i.e.
def is_symmetric(matrix):
    .....

Try both ways: the "manual way" (i.e. by using the definition) and by making use of Numpy functions
'''

import numpy as np

# Matrix A is called symmetric matrix if A = A_transpose

def is_symmetric(matrix):
    # In order to compare the two matrices use np.allclose instead of (if matrix == np.transpose(matrix):)
    # References:
    # https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy
    # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.allclose.html
    # https://en.wikipedia.org/wiki/Symmetric_matrix

    try:

        if np.allclose(matrix, np.transpose(matrix)):  # or if np.allclose(matrix, matrix.T):
            return True
    except ValueError as err:
        print("ValueError: {0}".format(err))
    return False

A = np.array([
    [7, 1, 3],
    [1, 0, 2],
    [3, 2, 5]
])

print(is_symmetric(A))

A = np.array([
    [7, 1, 3],
    [2, 0, 2],
    [3, 1, 5]
])

print(is_symmetric(A))

A = np.array([
    [7, 1, 3],
    [2, 0, 2],
    [3, 1, 5],
    [3, 1, 5]
])

print(is_symmetric(A))
