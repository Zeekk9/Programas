import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('dark_background')

xlim = 20
ylim = 20
n = 2000
m = 2000
x = np.linspace(-xlim, xlim, n)
y = np.linspace(-ylim, ylim, m)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = 100 * (np.exp(1j * 2 * np.pi / 0.628 * R)).real
Z = np.sqrt(X ** 2 + Y ** 2)


Z_env = np.arctan2(np.sin(Z), np.cos(Z))
W = Z_env


def itoh_2D(W):
    renglon, columna = W.shape
    phi = np.zeros(W.shape)
    psi = np.zeros(W.shape)
    phi[0, 0] = W[0, 0]
    # Se Desenvuelve la primera columna
    for m in range(1, columna):
        Delta = W[0, m] - W[0, m - 1]
        WDelta = np.arctan2(np.sin(Delta), np.cos(Delta))
        phi[0, m] = phi[0, m - 1] + WDelta
    psi[0, :] = phi[0, :]

    for k in range(columna):
        psi[0, k] = W[0, k]
        for p in range(1, renglon):
            Delta = W[p, k] - W[p - 1, k]
            WDelta = np.arctan2(np.sin(Delta), np.cos(Delta))
            phi[p, k] = phi[p - 1, k] + WDelta
    return phi


'''fig = plt.figure()
ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(X, Y, Z, cmap='jet')
ax = fig.add_subplot(132, projection='3d')
ax.plot_surface(X, Y, Z_env, cmap='jet')
ax = fig.add_subplot(133, projection='3d')
ax.plot_surface(X, Y, itoh_2D(Z_env), cmap='jet')
plt.show() '''

''plt.subplot(121)
plt.imshow(Z, cmap='Reds')
plt.colorbar()
#plt.grid()
plt.subplot(122)
plt.imshow(Z_env, cmap='Reds')
plt.colorbar()
#plt.grid()
plt.savefig('demo2.png', transparent=True, orientation='landscape')
plt.show()''
