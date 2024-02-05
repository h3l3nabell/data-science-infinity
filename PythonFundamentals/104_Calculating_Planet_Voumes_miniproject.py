# -*- coding: utf-8 -*-
"""
Numpy
"""
import numpy as np
import time

# array of radii of each planet
radii = np.array([2439.7, 6051.8, 6371, 3389.7, 69911, 58232, 25362, 24622])

# volume calculation
r = 10
volume = 4/3 * np.pi * r**3
print(volume)

start = time.time()
volumes = 4/3 * np.pi * radii**3
print(volumes)
end = time.time()
end = time.time()
print(f"calculated in {end - start} seconds")

# fictional planets!
radii2 = np.random.randint(1, 100000, 1000000)

start = time.time()
volumes = 4/3 * np.pi * radii2**3
print(volumes)
end = time.time()
print(f"calculated in {end - start} seconds")
print(f"length of volumes array is {len(volumes):,d}")
