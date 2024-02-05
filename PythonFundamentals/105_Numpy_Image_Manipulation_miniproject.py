# -*- coding: utf-8 -*-
"""
Numpy
"""
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# import the image file using the skimage package
camaro = io.imread("camaro.jpg")
print(camaro.shape)
print(camaro)

print(camaro[0:5, 0:2, :])

# show in the plots tab of the top right panes of things
plt.imshow(camaro)
plt.show()

# cropping the image
cropped = camaro[0:500, :, :]
plt.imshow(cropped)
plt.show()

cropped = camaro[:, 400:1000, :]
plt.imshow(cropped)
plt.show()

cropped = camaro[350:1100, 200:1400, :]
plt.imshow(cropped)
plt.show()

io.imsave("camaro_cropped.jpg", cropped)

# Flip our image
vertical_flipped = camaro[::-1, :, :]
plt.imshow(vertical_flipped)
plt.show()

io.imsave("camaro_vertical_flipped.jpg", vertical_flipped)

# horizontal flip
horizontal_flipped = camaro[:, ::-1, :]
plt.imshow(horizontal_flipped)
plt.show()

io.imsave("camaro_horizontal_flipped.jpg", horizontal_flipped)

# Colour channels

# select the red only channels from the camaro image array
red = np.zeros(camaro.shape, dtype="uint8")
red[:, :, 0] = camaro[:, :, 0]
plt.imshow(red)
plt.show()
io.imsave("camaro_red.jpg", red)

green = np.zeros(camaro.shape, dtype="uint8")
green[:, :, 1] = camaro[:, :, 1]
plt.imshow(green)
plt.show()
io.imsave("camaro_green.jpg", green)

blue = np.zeros(camaro.shape, dtype="uint8")
blue[:, :, 2] = camaro[:, :, 2]
plt.imshow(blue)
plt.show()
io.imsave("camaro_blue.jpg", blue)

camaro_rainbow = np.vstack((red, green, blue))
plt.imshow(camaro_rainbow)
plt.show()
io.imsave("camaro_rainbow.jpg", camaro_rainbow)

croppedred = red[350:1100, 200:1400, :]
plt.imshow(croppedred)
plt.show()

croppedgreen = green[350:1100, 200:1400, :]
plt.imshow(croppedgreen)
plt.show()

croppedblue = blue[350:1100, 200:1400, :]
plt.imshow(croppedblue)
plt.show()


camaro_rainbow_cropped_h = np.hstack((croppedred, croppedgreen, croppedblue))
plt.imshow(camaro_rainbow_cropped_h)
plt.show()
io.imsave("camaro_rainbow_cropped_h.jpg", camaro_rainbow_cropped_h)
