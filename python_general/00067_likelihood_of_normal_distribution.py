import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection = "3d")

mu = np.linspace(0, 3, 50)
sigma = np.linspace(1, 3, 30)

# a sample of size 20 from N(2, 4)
true_mu = 2; true_sigma = 2

x = np.random.normal(loc = true_mu, scale = true_sigma, size = 30)

def f(x, mu, sigma) :
    a = 1 / (np.sqrt(2 * np.pi) * sigma)

    b = ((x - mu) / sigma) ** 2

    return(a * np.exp(-b/2))

def likelihood(mu, sigma, sample) :
    f_values = np.ones_like(sample)

    for i in range(len(sample)) :
        f_values[i] = f(sample[i], mu, sigma)
    
    return(np.prod(f_values))

MU, SIGMA = np.meshgrid(mu, sigma)

L = np.ones_like(MU)

for i in range(MU.shape[0]) :
    for j in range(MU.shape[1]) :
        L[i, j] = likelihood(MU[i, j], SIGMA[i, j], sample = x)

ax.plot_surface(MU, SIGMA, L, cmap = "coolwarm", alpha = 0.8)

ax.set_xlabel("mu")
ax.set_ylabel("sigma")
ax.set_zlabel("likelihood")

plt.show()