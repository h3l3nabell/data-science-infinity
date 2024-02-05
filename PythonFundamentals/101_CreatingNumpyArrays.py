# -*- coding: utf-8 -*-
"""
Numpy
"""
import numpy as np


my_1d_array = np.array([1, 2, 3])
type(my_1d_array)
my_1d_array.shape
my_1d_array[0]
my_1d_array[0:2]  # start, length sliced array
my_1d_array[-1]  # last element

my_2d_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(my_2d_array)
my_2d_array.shape
my_2d_array[0]
my_2d_array[0][1]
my_2d_array[0, 1]
my_2d_array[0:2, 1:3]

np.zeros(3)
np.zeros((3, 3))
np.zeros((3, 3, 3))
np.ones((3, 3, 3))

np.full((3, 3), 5)

np.arange(10)  # = 0 to 10 range
np.arange(2, 10)  # from 2 to 10
np.arange(2, 19, 2)  # from 2 to 10 step 2

np.linspace(1, 5, 20)  # start range, stop range, num of values

float_array = np.linspace(1, 5, 20)
np.round(float_array, 2)

np.random.rand(5)
np.random.rand(5, 2)

np.random.randint(20, 80, 100)
np.random.randint(20, 80, (10, 10))

my_1d_array = np.random.randint(20, 80, 100)
my_2d_array = my_1d_array.reshape(10, 10)
