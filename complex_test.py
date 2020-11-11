import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def f(z, a, n):
    return a * z**n


amplitude = 1.0
power = -1

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
z = np.ravel(X) + np.ravel(Y) * 1j
w = f(z, amplitude, power)
W = w.reshape(X.shape)

levels = np.linspace(-1, 1, 39)
# levels = 20

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_wireframe(X, Y, W.imag, rstride=5, cstride=5, lw=0.5, color='k')

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

fig, ax = plt.subplots(1, 1)
ax.contour(X, Y, W.imag, levels, linewidths=0.5, linestyles='-', colors='k')
ax.contour(X, Y, W.real, levels, linewidths=0.5, linestyles='-', colors='b')

ax.set_aspect('equal')
plt.show()
