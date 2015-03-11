"""
3D Plotting and surface areas
"""

import matplotlib.pyplot as plt
import numpy as np

# with np.indices we are able to have matrices
# that represents indices as we want. More
# powerfull than that, np.meshgrid lets us to have
# any kind of matrices of indexes. The later is
# particularly useful when plotting as i'll show
# next.

# f(x,y) = x + y

X, Y = np.indices((10,10))
Z = (X + Y) % 2
plt.contour(X,Y,Z)


x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x,y)

Z = 4*X**2 + Y**2

# plt.contour(X, Y, Z)

plt.show()
