import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func(x, y):
    y = np.exp(x, y)
    return y


def gaussian(A, x, x0, y, y0, sigmax, sigmay):
    f = A * np.exp(-(x - x0) ** 2 / (2 * sigmax ** 2) -
                    (y - y0) ** 2 / (2 * sigmay ** 2))
    return f


xlim = -20
ylim = 20
n = 80
x = np.linspace(-xlim, xlim, n)
y = np.linspace(-ylim, ylim, n)
X, Y = np.meshgrid(x, y)
Z = gaussian(10, X, 0, Y, 0, 10, 10)
Z1 = np.fft.fft2(Z)
Z2 = np.fft.ifft2(Z1)
Z3=np.fft.fftshift(Z2)
np.savetxt('iFFt.txt',Z2,delimiter=',')

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.plot_surface(X, Y, Z1.imag, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax = fig.add_subplot(1, 3, 3, projection='3d')
ax.plot_surface(X, Y, abs(Z2), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plt.show()
