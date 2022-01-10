#%%

def plot():
    fig = plt.figure(figsize=(6, 3.2))

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(imageMatrix)
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()
    

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im
import pandas as pd
import time

image = im.open('data.png')

image = image.convert("RGB")

print(f'image format: {image.format}')
print(f'image size: {image.size}')
print(f'image mode: {image.mode}')

data = np.array(image)

# Convert to 2D matrix of 1s and 0s
rows, columns = data.shape[0], data.shape[1]
print(f'rows: {rows} columns: {columns}')
imageMatrix = np.empty([rows, columns])

threshold = 200

for i in range(rows):
    for j in range(columns):
        value = data[i, j, 0]
        if value > threshold:
            imageMatrix[i, j] = 1
        else:
            imageMatrix[i, j] = 0

np.savetxt('data.txt', imageMatrix, fmt='% 4d')

np.random.seed = 1

# Locate a random 1 in the image
# found = False
# for i in range(rows):
#     for j in range(columns):
#         value = imageMatrix[i, j]
#         if value == 1:
#             center = (i, j)
#             imageMatrix[i, j] = 3
#             found = True
#             break
#     if found:
#         break

found = False
while found == False:
    rpx = np.random.randint(0, columns)
    rpy = np.random.randint(0, rows)

    if imageMatrix[rpx, rpy] == 1:
        found = True
        imageMatrix[rpx, rpy] = 2
        center = (rpx, rpy)


if center != None:
    print(f'position of a one: {center}')

plot()

# Search around in a circle for a zero
radius = 0
firstzerofound = False
posx = 0
posy = 0
zpos1 = None
while firstzerofound == False:
    radius += 1
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            if i**2 + j**2 <= radius**2:
                print(i, j)
                # Check pixel
                posx = center[0] + int(np.floor(i))
                posy = center[1] + int(np.floor(j))
                if imageMatrix[posx, posy] == 0:
                    firstzerofound = True

                    # Check against existing position to see if this one is shorter
                    if zpos1 != None:
                        currentDist = (zpos1[0] - center[0])**2 + (zpos1[1] - center[1])**2
                        newDist = (posx - center[0])**2 + (posy - center[1])**2
                        if newDist < currentDist:
                            zpos1 = (posx, posy)
                    else:
                        zpos1 = (posx, posy)

# Mark the zero position
imageMatrix[zpos1[0], zpos1[1]] = 2


print(f'first zero: {zpos1}')

plot()



# Get the angle between the center of the circle and the first zero
angle = np.arctan2(zpos1[1] - center[1], zpos1[0] - center[0])
print(f'angle: {angle * 180/np.pi}')

# Follow along the opposite of the angle to get to a dark pixel
oppositeAngle = angle + np.pi

# Iterate along the line until reaches a dark pixel
secondzerofound = False
distance = 0
startx = center[0]
starty = center[1]
while secondzerofound == False:
    distance += 1
    distx = int(np.round(distance * np.cos(oppositeAngle)))
    disty = int(np.round(distance * np.sin(oppositeAngle)))
    posx = startx + distx
    posy = starty + disty

    
    value = imageMatrix[posx, posy]
    imageMatrix[posx, posy] = 0.5
    print(f'value: {value}')

    

    if value == 0:
        imageMatrix[posx, posy] = 2
        secondzerofound = True
        secondzeropos = (posx, posy)

    
plot()

print(f'second zero position: {secondzeropos}')




# %%
