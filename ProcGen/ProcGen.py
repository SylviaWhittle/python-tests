from collections import namedtuple
from math import floor
import random
import numpy as np
from PIL import Image

#random.seed(1)

print(random.uniform(0, 1))

Point = namedtuple('Point', 'x y')
mapshape = Point(140, 200)

Feature = namedtuple('Feature', 'pos, width, height, maxquantity, chance, colour')
#feature = Feature(Point(100, 100), 10, 20)


WALL = [0, 0, 0]
FLOOR = [200, 200, 200]

map = np.ones([mapshape.x, mapshape.y, 3], dtype=np.uint8)


for i in range(mapshape.x):
    for j in range(mapshape.y):
        map[i, j] = WALL

chance = lambda x: x > random.uniform(0, 1)

brush_size = 1

iterations = 20000

velx = 1
vely = 0

max_velocity = 1

# Start in the middle
posx = round(mapshape.x/2)
posy = round(mapshape.y/2)

for iteration in range(iterations):

    # Change velocity
    if chance(0.8):
        velx = random.randint(-max_velocity, max_velocity)
        vely = random.randint(-max_velocity, max_velocity)
    
    # Fill brush area
    for i in range(-brush_size, brush_size + 1):
        for j in range(-brush_size, brush_size + 1):
            x = posx + i
            y = posy + j
            
            if x >= 0 and x < mapshape.x and y >= 0 and y < mapshape.y:
                map[x][y] = FLOOR

    # Move brush
    if posx - brush_size + velx > 0 and posx + brush_size + velx < mapshape.x - 1:
        posx += velx
    if posy - brush_size + vely > 0 and posy + brush_size + vely < mapshape.y - 1:
        posy += vely

# Add features

# Feature: empty space only
area_size = 10
quantity = 0
max_quantity = 1
for i in range(mapshape.x):
    for j in range(mapshape.y):
        testarea = map[max(i - area_size, 0):min(i + area_size, mapshape.x - 1), max(j - area_size, 0):min(j + area_size, mapshape.y)]
        if (testarea != WALL).all():
            if(chance(0.01) and quantity < max_quantity):
                map[max(i - area_size, 0):min(i + area_size, mapshape.x - 1), max(j - area_size, 0):min(j + area_size, mapshape.y)] = [200, 180, 0]
                quantity += 1

# Feature: some connected points
area_size = 8
quantity = 0
max_quantity = 10

tries = 1000
for iteration in range(tries):
    i = random.randint(0 + area_size/2 + 4, mapshape.x - 1 - area_size/2 - 4)
    j = random.randint(0 + area_size/2 + 4, mapshape.y - 1 - area_size/2 - 4)
    testarea = map[max(i - area_size, 0):min(i + area_size, mapshape.x - 1), max(j - area_size, 0):min(j + area_size, mapshape.y)]
    # print(testarea)
    if quantity < max_quantity:
        floortiles = (testarea == FLOOR).sum()

        # Get number of tiles that are not wall or floor
        othertiles = (value != FLOOR and value != WALL for value in testarea).sum()
        

        if floortiles > 20 and floortiles <= 30 and othertiles == 0:
            map[max(i - area_size, 0):min(i + area_size, mapshape.x - 1), max(j - area_size, 0):min(j + area_size, mapshape.y)] = [0, 180, 100]
            quantity += 1

# Save image
im = Image.fromarray(map)
# if im.mode != 'RGB':
#     im = im.convert('RGB')
im.save('ProcGen/data.png')
