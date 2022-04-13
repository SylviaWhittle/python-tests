#%%
import numpy as np
import math
import matplotlib.pyplot as plt

def dx(x, y, z, rho, sigma, beta):
    return sigma * (y - x)

def dy(x, y, z, rho, sigma, beta):
    return x * (rho - z) - y

def dz(x, y, z, rho, sigma, beta):
    return x * y - beta * z

def main():
    # sigma = 10.0
    sigma = 12
    # rho = 28.0
    rho = 20
    # beta = 8.0 / 3.0
    beta = 10.0/3.33

    iterations = 100000
    time_start = 0.0
    time_end = 100.0

    timestep = (time_end - time_start)/iterations
    xs = np.zeros(iterations)
    ys = np.zeros(iterations)
    zs = np.zeros(iterations)
    times = np.zeros(iterations)

    xs[0] = 10.0
    ys[0] = 10.0 
    zs[0] = 10.0

    h, w = 1600, 1600
    hist = np.zeros((h, w), dtype=int)

    x_min = -40
    x_max = 40
    y_min = x_min * (h / w)
    y_max = x_max * (h / w)

    for i in range(iterations-1):

        x = xs[i]
        y = ys[i]
        z = zs[i]

        # RK4 
        kx1 = timestep * dx(x, y, z, rho, sigma, beta)
        ky1 = timestep * dy(x, y, z, rho, sigma, beta)
        kz1 = timestep * dz(x, y, z, rho, sigma, beta)

        kx2 = timestep * dx(x + kx1/2, y + ky1/2, z + kz1/2, rho, sigma, beta)
        ky2 = timestep * dy(x + kx1/2, y + ky1/2, z + kz1/2, rho, sigma, beta)
        kz2 = timestep * dz(x + kx1/2, y + ky1/2, z + kz1/2, rho, sigma, beta)

        kx3 = timestep * dx(x + kx2/2, y + ky2/2, z + kz2/2, rho, sigma, beta)
        ky3 = timestep * dy(x + kx2/2, y + ky2/2, z + kz2/2, rho, sigma, beta)
        kz3 = timestep * dz(x + kx2/2, y + ky2/2, z + kz2/2, rho, sigma, beta)

        kx4 = timestep * dx(x + kx3, y + ky3, z + kz3, rho, sigma, beta)
        ky4 = timestep * dy(x + kx3, y + ky3, z + kz3, rho, sigma, beta)
        kz4 = timestep * dz(x + kx3, y + ky3, z + kz3, rho, sigma, beta)

        xs[i+1] = x + 1.0/6.0 * (kx1 + 2*kx2 + 2*kx3 + kx4)
        ys[i+1] = y + 1.0/6.0 * (ky1 + 2*ky2 + 2*ky3 + ky4)
        zs[i+1] = z + 1.0/6.0 * (kz1 + 2*kz2 + 2*kz3 + kz4)

        times[i+1] = times[i] + timestep

        x_i = int( (x - x_min) * w / (x_max - x_min) )
        y_i = int( (y - y_min) * h / (y_max - y_min) )
        if (x_i >= 0 and x_i < w \
        and y_i >= 0 and y_i < h):
            hist[y_i, x_i] += 1
    
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

    plt.imsave('Lorenz.png', im, dpi=600, origin='lower')

    plt.axis('off')
    plt.imshow(im)
    plt.show()

    color = (36, 169, 174)


if __name__=="__main__":
    main()


