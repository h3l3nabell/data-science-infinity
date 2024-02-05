# -*- coding: utf-8 -*-
"""
 MatPlotLib - features
"""

import pandas as pd
import matplotlib.pyplot as plt

# plot from lists
x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_squared = [x ** 2 for x in x_values]
x_cubed = [x ** 3 for x in x_values]

plt.plot(x_values, x_squared, label="x squared")
plt.plot(x_values, x_cubed, label="x cubed")
plt.title("exponential growth")
plt.xlabel("values of x")
# plt.xticks([])
# plt.xlim(2,8)
# plt.xticks(range(11))
# you can put text on the  ticks and specify rotation of text in degrees
plt.ylabel("values of y")
# plt.yticks([])
# plt.ylim(-100, 600)
plt.grid(True)
plt.legend()
plt.show()
