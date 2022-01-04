import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im
import pandas as pd

image = im.open('data.png')

image = image.convert("RGB")

print(f'image format: {image.format}')
print(f'image size: {image.size}')
print(f'image mode: {image.mode}')

data = np.array(image)

print(data)

np.savetxt('data.txt', data)
