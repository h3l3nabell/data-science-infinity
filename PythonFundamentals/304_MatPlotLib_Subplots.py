# -*- coding: utf-8 -*-
"""
 MatPlotLib - sub plots
"""

import matplotlib.pyplot as plt

# plot from lists
x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_squared = [x ** 2 for x in x_values]
x_cubed = [x ** 3 for x in x_values]

# width, height, ID
plt.subplot(2, 1, 1)
plt.plot(x_values, x_squared, label="x squared")
plt.title("Square Values")
plt.xlabel("X")
plt.ylabel("X Squared")

plt.subplot(2, 1, 2)
plt.bar(x_values, x_cubed, label="x cubed")
plt.title("Cube Values")
plt.xlabel("X")
plt.ylabel("X Cubed")

plt.tight_layout()
plt.show()


# width, height, ID
plt.subplot(1, 2, 1)
plt.plot(x_values, x_squared, label="x squared")
plt.title("Square Values")
plt.xlabel("X")
plt.ylabel("X Squared")

plt.subplot(1, 2, 2)
plt.bar(x_values, x_cubed, label="x cubed")
plt.title("Cube Values")
plt.xlabel("X")
plt.ylabel("X Cubed")

plt.tight_layout()
plt.show()


# width, height, ID
plt.subplot(2, 2, 1)
plt.plot(x_values, x_squared, label="x squared")
plt.title("Square Values")
plt.xlabel("X")
plt.ylabel("X Squared")

plt.subplot(2, 2, 2)
plt.bar(x_values, x_cubed, label="x cubed")
plt.title("Cube Values")
plt.xlabel("X")
plt.ylabel("X Cubed")

plt.subplot(2, 2, 3)
plt.plot(x_values, x_squared, label="x squared")
plt.title("Square Values")
plt.xlabel("X")
plt.ylabel("X Squared")

plt.subplot(2, 2, 4)
plt.bar(x_values, x_cubed, label="x cubed")
plt.title("Cube Values")
plt.xlabel("X")
plt.ylabel("X Cubed")


plt.tight_layout()
plt.show()
