# -*- coding: utf-8 -*-
"""
 MatPlotLib - features
"""

import matplotlib.pyplot as plt

# plot from lists
x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_squared = [x ** 2 for x in x_values]
x_cubed = [x ** 3 for x in x_values]

plt.style.available
plt.style.use('tableau-colorblind10')

# plt.plot(x_values, x_squared, label="x squared",
#         color="darkmagenta", linewidth=3, linestyle=":")

# plt.plot(x_values, x_squared, label="x squared",
#         color="darkmagenta", linewidth=3, marker=".")

plt.plot(x_values, x_squared, label="x squared")


# plt.plot(x_values, x_cubed, label="x cubed",
#         color=[0.0, 0.25, 1.0], linewidth=2, linestyle="--")

# plt.plot(x_values, x_cubed, label="x cubed",
#          color=[0.0, 0.25, 1.0], linewidth=2, marker="o",
#         markersize=10, markerfacecolor="red", markeredgecolor="lime")

plt.plot(x_values, x_cubed, label="x cubed")

plt.title("Exponential Growth")
plt.xlabel("values of x")

plt.ylabel("values of y")

plt.legend()
plt.show()
