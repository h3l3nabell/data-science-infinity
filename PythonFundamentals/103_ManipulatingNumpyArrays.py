# -*- coding: utf-8 -*-
"""
Numpy
"""
import numpy as np

my_1d_array = np.zeros(10)
my_1d_array[0] = 50

my_1d_array[3: 6] = 50

np.where(my_1d_array == 50)

my_2d_array = np.array([[1, 5, 9], [8, 5, 5]])
print(my_2d_array)
np.where(my_2d_array == 5)
np.where(my_2d_array < 5)
np.where(my_2d_array > 5)
np.where(my_2d_array != 5)

np.argwhere(my_2d_array == 5)

index = np.where(my_2d_array > 5)
print(index)
my_2d_array[index]

# manipulate them!
my_2d_array[index] = 100

# are all values in this array non-zero?
np.all(my_1d_array)
np.all(my_1d_array >= 0)
np.all(my_1d_array >= 5)

# are any values in this array non-zero?
np.any(my_1d_array)

# stacks
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a)
print(b)

# vstack (vertical stack) needs both arrays to have the same number of columns
v = np.vstack((a, b))
print(v)
np.vstack((a, b, a, b))

# hstack (horizontal stack) needs both arrays to have the same number of rows
h = np.hstack((a, b))
print(h)
np.hstack((a, b, a, b))

# flatten
print(my_2d_array)
my_2d_array.flatten()
