# FB - 201104096
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# First Order ODE (y' = f(x, y)) Solver using Euler method
# xa: initial value of independent variable
# xb: final value of independent variable
# ya: initial value of dependent variable
# n : number of steps (higher the better)
# Returns value of y at xb.


def Euler(f, xa, xb, ya, n):
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    for i in range(n):
        y += h * f(x, y)
        x += h
    return y


def f(x, y):
    f = x ** 2 + y ** 2
    return f



n = 100
m = 200
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, m)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Z2 = Euler(f, -10, 10, 1, len(Z[0]))
fig = plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X, Y, Z,cmap='jet')
plt.show()