# -*- coding: utf-8 -*-
"""
Numpy
"""
import numpy as np

# 16 random integers between the values of 2 and 8
my_1d_array = np.random.randint(2, 8, 16)

# numpy has its own max for arrays
np.max(my_1d_array)

# or
my_1d_array.max()

my_1d_array.min()
my_1d_array.mean()
my_1d_array.sum()
my_1d_array.std()

# reshape the 1d array of 16 into a 2d array that is 4x4
my_2d_array = my_1d_array.reshape(4, 4)
print(my_2d_array)

my_2d_array.max()
my_2d_array.max(axis=0)  # a 1d array contianing the max value for each col
my_2d_array.max(axis=1)  # a 1d array contianing the max value for each row

my_2d_array.argmax(axis=0)  # a 1d array contianing the index of max col value
my_2d_array.argmax(axis=1)  # a 1d array contianing the index of max row value


# sort
np.sort(my_1d_array)

# array and maths
a = np.array([1, 2, 3, 4, 5])
a + 10

b = np.array([3, 7, 1, 2, 6])
a + b

a = np.array([-2, -1, 0, 1, 2])

np.square(a)
np.sqrt(a)
np.sign(a)
np.sin(a)
np.cos(a)
np.tan(a)

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

np.dot(a, b)  # = 1 X 4 + 2 X 5 + 3 X 6
