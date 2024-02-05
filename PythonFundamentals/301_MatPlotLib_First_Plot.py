# -*- coding: utf-8 -*-
"""
 MatPlotLib - first plot
"""

import pandas as pd
import matplotlib.pyplot as plt

# plot from lists
x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_sqared = [x ** 2 for x in x_values]

plt.plot(x_values, x_sqared)
plt.title("exponential growth")
plt.xlabel("values of x")
plt.ylabel("values of y")
plt.show()

# plots from pandas dataframes

my_df = pd.DataFrame(
    {"X": x_values,
     "Y": x_sqared})

plt.plot(my_df["X"], my_df["Y"])
plt.title("exponential growth")
plt.xlabel("values of x")
plt.ylabel("values of y")
plt.show()
