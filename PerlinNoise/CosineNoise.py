import random
import numpy as np
import matplotlib.pyplot as plt

def perlin(x):
    # Determine the cell that the point is between and fetch the values of the two cells
    x0 = int(np.floor(x))
    x1 = int(np.ceil(x))
    y0 = randarray[x0]
    y1 = randarray[x1]

    # Cosine interpolation

    cospix = np.cos((x - x0) * np.pi) 
    
    mu2 = (1 - cospix)/2

    intensity = y0 * (1 - mu2) + y1 * mu2

    return intensity

# Create random noise
length = 20
stepsize = 0.01

randarray = np.random.rand(length)
xs = np.arange(length)


# Cosine interpolation
xs_perlin = np.arange(0, len(randarray) - 1, stepsize)
perlinArray = np.array([])
for index, value in enumerate(xs_perlin):
    perlinArray = np.append(perlinArray, perlin(value))


plt.figure(figsize=(12, 6), dpi=80)
plt.scatter(xs_perlin, perlinArray, marker='.')
plt.scatter(xs, randarray, marker='.')
plt.show()
