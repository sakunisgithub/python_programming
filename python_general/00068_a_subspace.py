import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

# {(x, y, z) : x - 2y + 3z = 0}

x = np.linspace(-5, 5, 50)
y = x

z = (2 * y - x) / 3

ax = plt.axes(projection = "3d")

ax.scatter(x, y, z)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()