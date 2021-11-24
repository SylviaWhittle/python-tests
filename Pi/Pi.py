#%% Leibniz
import numpy

piby4 = 0.0

denominator = 1
sign = 1.0
for x in range(10000000):

    piby4 = piby4 + sign/denominator

    denominator = denominator + 2
    sign = -sign

pi = piby4 * 4

print(pi)

#%% Newton
import numpy as np

pi = 3.0 * np.sqrt(3.0) / 4.0

pi = pi + 24.0 * 1.0/12.0

for x in range(100)
    pi = pi + 24.0 * 

print(pi)

