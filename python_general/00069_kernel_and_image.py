import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

# span{(1, 2, 3)}

c = np.linspace(-5, 5, 50)

x1 = c * 1; y1 = c * 2; z1 = c * 3

ax = plt.axes(projection = "3d")

ax.plot(x1, y1, z1, "b--")
ax.quiver(0, 0, 0, 1, 2, 3, color = "red")

v1 = np.array([-2, 1, 0])
v2 = np.array([-3, 0, 1])

A, B = np.meshgrid(c, c)

X = A * v1[0] + B * v2[0]
Y = A * v1[1] + B * v2[1]
Z = A * v1[2] + B * v2[2]

ax.plot_surface(X, Y, Z, cmap = "viridis", alpha = 0.8)

ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color = "black", label = "v1")
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color = "black", label = "v2")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()