#%%
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from PIL import Image
from collections import namedtuple

# Position and velocity
px = 0
py = 0
vx = 0
vy = 0

# Velocity
max_velocity = 1
velocity_delta = 0.1

# Create the spline array
iterations = 100
spline = np.zeros([iterations, 2])

# Create points of a circle to test the curvature calculation
pi = math.pi
r = 10
n = 40
spline = [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n)]
print(f'Expected curvature (1/r): {1/r}') # Curvature of a circle is 1/radius

# Create random squiggle
# for iteration in range(iterations):

#     # Update velocity, ensuring that either vx or vy is nonzero
#     while True:
#         vx += random.uniform(-velocity_delta, velocity_delta)
#         vy += random.uniform(-velocity_delta, velocity_delta)
#         if abs(vx) > max_velocity:
#             vx = np.sign(vx) * max_velocity
#         if abs(vy) > max_velocity:
#             vy = np.sign(vy) * max_velocity
#         if vx != 0 or vy != 0:
#             break

#     # Update position
#     px += vx
#     py += vy
    
#     # Add point to the spline
#     spline[iteration] = (px, py)

# Turn the spline into a dataframe and plot
df = pd.DataFrame(data=spline, columns=['x','y'])

fig, axes = plt.subplots(2, 1, figsize=(5,10))

ax1 = axes[0]
ax1.figsize = (5, 5)
df.plot(kind='scatter',ax=ax1, x='x', y='y')

# Create longer array so the edges are looped
longdata = np.concatenate([spline, spline, spline])
# print('len longdata: ', len(longdata))
# print(longdata)
longdf = pd.DataFrame(data=longdata, columns=['x','y'])

# print('data:')
# print(spline)
# print('longdf:')
# print(longdf)

# Calculate the curvature and plot
window_size = 8
longdf['dx'] = np.gradient(longdf['x'])
longdf['dx'] = longdf['dx'].rolling(window_size, center=True).mean()
longdf['dy'] = np.gradient(longdf['y'])
longdf['dy'] = longdf['dy'].rolling(window_size, center=True).mean()
longdf['d2x'] = np.gradient(longdf['dx'])
longdf['d2x'] = longdf['d2x'].rolling(window_size, center=True).mean()
longdf['d2y'] = np.gradient(longdf['dy'])
longdf['d2y'] = longdf['d2y'].rolling(window_size, center=True).mean()

longdf['curvature'] = longdf.eval('abs(dx * d2y - d2x * dy) / (dx * dx + dy * dy) ** 1.5')

print('spline: ')
print(spline)
print('spline length: ', len(spline))

ax2 = axes[1]
longdf['curvature'].plot(ax=ax2, xlabel='Point in spline', ylabel='Smoothed curvature')

print('longdf: ', longdf)

print('size: ', len(longdata))

newdf = longdf.iloc[len(spline) : len(spline)*2, :]
print('newdf head:')
print(newdf.head())

# # Calculate the curvature and plot
# window_size = 8
# df['dx'] = np.gradient(df['x'])
# df['dx'] = df['dx'].rolling(window_size, center=True).mean()
# df['dy'] = np.gradient(df['y'])
# df['dy'] = df['dy'].rolling(window_size, center=True).mean()
# df['d2x'] = np.gradient(df['dx'])
# df['d2x'] = df['d2x'].rolling(window_size, center=True).mean()
# df['d2y'] = np.gradient(df['dy'])
# df['d2y'] = df['d2y'].rolling(window_size, center=True).mean()

# df['curvature'] = df.eval('abs(dx * d2y - d2x * dy) / (dx * dx + dy * dy) ** 1.5')

# ax2 = axes[1]
# df['curvature'].plot(ax=ax2, xlabel='Point in spline', ylabel='Smoothed curvature')

# Create pixel image from the spline
pixelarray = np.round(spline)

Point = namedtuple('Point', 'x y')
mapshape = Point(400, 400)

imagemap = np.ones([mapshape.x, mapshape.y, 3], dtype=np.uint8)


# Set all sets of x, y coords in the spline to white in the map
WHITE = (200, 200, 200)
for index, value in enumerate(pixelarray):
    imagemap[int(mapshape.x/2) + int(value[0]), int(mapshape.y/2) + int(value[1])] = WHITE

# Save image
im = Image.fromarray(imagemap)
if im.mode != 'RGB':
    im = im.convert('RGB')
im.save('./SquigglePixels.png')




# %%
