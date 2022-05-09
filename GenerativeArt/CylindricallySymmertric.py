#%%
import numpy as np
import math
import matplotlib.pyplot as plt
import time


def dx(x, y, z, b):
    return np.sin(y) - b * x

def dy(x, y, z, b):
    return np.sin(z) - b * y

def dz(x, y, z, b):
    return np.sin(x) - b * z

def main():
    # b = 0.208186
    b = 0.208186

    iterations = int(1e7)
    particles = 1e4
    time_start = 0.0
    # time_end = 10.0

    # timestep = (time_end - time_start)/iterations
    timestep = 0.01
    xs = np.zeros(iterations)
    ys = np.zeros(iterations)
    zs = np.zeros(iterations)
    times = np.zeros(iterations)

    h, w = 1600, 1600
    hist = np.zeros((h, w), dtype=int)

    x_min = -6
    x_max = 6
    y_min = x_min * (h / w)
    y_max = x_max * (h / w)
    z_max = x_max
    z_min = x_min

    for i in range(iterations-1):

        x = xs[i]
        y = ys[i]
        z = zs[i]

        if i % particles == 0:
            x = 2 * np.random.rand() - 1
            y = 2 * np.random.rand() - 1
            z = 2 * np.random.rand() - 1

        # RK4 
        # kx1 = timestep * dx(x, y, z, b)
        # ky1 = timestep * dy(x, y, z, b)
        # kz1 = timestep * dz(x, y, z, b)

        # kx2 = timestep * dx(x + kx1/2, y + ky1/2, z + kz1/2, b)
        # ky2 = timestep * dy(x + kx1/2, y + ky1/2, z + kz1/2, b)
        # kz2 = timestep * dz(x + kx1/2, y + ky1/2, z + kz1/2, b)

        # kx3 = timestep * dx(x + kx2/2, y + ky2/2, z + kz2/2, b)
        # ky3 = timestep * dy(x + kx2/2, y + ky2/2, z + kz2/2, b)
        # kz3 = timestep * dz(x + kx2/2, y + ky2/2, z + kz2/2, b)

        # kx4 = timestep * dx(x + kx3, y + ky3, z + kz3, b)
        # ky4 = timestep * dy(x + kx3, y + ky3, z + kz3, b)
        # kz4 = timestep * dz(x + kx3, y + ky3, z + kz3, b)

        # xs[i+1] = x + 1.0/6.0 * (kx1 + 2*kx2 + 2*kx3 + kx4)
        # ys[i+1] = y + 1.0/6.0 * (ky1 + 2*ky2 + 2*ky3 + ky4)
        # zs[i+1] = z + 1.0/6.0 * (kz1 + 2*kz2 + 2*kz3 + kz4)

        xs[i+1] = x + dx(x, y, z, b) * timestep
        ys[i+1] = y + dy(x, y, z, b) * timestep
        zs[i+1] = z + dz(x, y, z, b) * timestep

        times[i+1] = times[i] + timestep

        # x_i = int( (x - x_min) * w / (x_max - x_min) )
        # y_i = int( (y - y_min) * h / (y_max - y_min) )
        # if (x_i >= 0 and x_i < w \
        # and y_i >= 0 and y_i < h):
        #     hist[y_i, x_i] += 1

        z_i = int( (z - z_min) * w / (z_max - z_min) )
        x_i = int( (x - x_min) * h / (x_max - x_min) )
        if (z_i >= 0 and z_i < w \
        and x_i >= 0 and x_i < h):
            hist[x_i, z_i] += 1
    
    # Output
    im = np.zeros((h, w, 3), dtype=int)
    sens = 4e-4
    # sens = 4e-1
    color = (36, 169, 174)
    
    for i in range(h):
        for j in range(w):
            val = hist[i, j]
            r = int((1. - math.exp(-sens * val * color[0])) * 255)
            g = int((1. - math.exp(-sens * val * color[1])) * 255)
            b = int((1. - math.exp(-sens * val * color[2])) * 255)
            im[i, j, :] = r, g, b

    im = im.astype(np.uint8)

    plt.imsave('Cylindrical.png', im, dpi=600, origin='lower')

    # plt.axis('off')
    # plt.imshow(im)
    # plt.show()

    color = (36, 169, 174)


if __name__=="__main__":
    start = time.time()
    main()
    end = time.time() - start
    print('process complete | elapsed time: ')



# %%
