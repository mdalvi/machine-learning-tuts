import numpy as np
from datetime import datetime

def perform_dot_product(a, b):
    dotproduct = 0
    for num1, num2 in zip(a,b):
        dotproduct += (num1 * num2)
    return dotproduct

# Creating a random vector of 100 elements with floating points varying from gaussian distribution of mean 0 and stddev 1
a = np.random.rand(100)
b = np.random.rand(100)

# Number of iterations = 1 million
T = 100000
t0 = datetime.now()
for i in range(T):
    perform_dot_product(a, b)
t1 = datetime.now()

print('Time taken for iteration 1 = {seconds} seconds'.format(seconds = (t1- t0).total_seconds()))

t0 = datetime.now()
for i in range(T):
    a.dot(b)
t1 = datetime.now()

print('Time taken for iteration 1 = {seconds} seconds'.format(seconds = (t1- t0).total_seconds()))