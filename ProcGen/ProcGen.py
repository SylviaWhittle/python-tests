from collections import namedtuple
import random
import numpy as np
from PIL import Image

#random.seed(1)

print(random.uniform(0, 1))

Point = namedtuple('Point', 'x y')
mapshape = Point(140, 200)


WALL = 1
FLOOR = 200

map = np.ones((mapshape.x, mapshape.y))

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

# Save image
im = Image.fromarray(map)
if im.mode != 'RGB':
    im = im.convert('RGB')
im.save('ProcGen/data.png')
