import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('fivethirtyeight')

xlim = 40
ylim = 40
n = 60

def func(x, y):
    y = np.exp(x, y)
    return y


def gaussian(A, x, x0, y, y0, sigmax, sigmay):
    f = A * np.exp(-(x - x0) ** 2 / (2 * sigmax ** 2) -
                    (y - y0) ** 2 / (2 * sigmay ** 2))
    return f


def rect(x,h):
    return np.where(abs(x) <= 3.5, h, 0)



def cylinder(center_x, center_y, radius, height_z,n):
    z = np.linspace(0, height_z, n)
    theta = np.linspace(0, 2*np.pi, n)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid, y_grid, z_grid


x = np.linspace(-xlim, xlim, n)
y = np.linspace(-ylim, ylim, n)
X, Y = np.meshgrid(x, y)
Z = gaussian(10, X, 0, Y, 0, 10, 10)
noise = np.random.normal(0, 0.1, Z.shape)
Z1 = Z + noise
fft = np.fft.fftshift(np.fft.fft2(Z1))
filtro1 = rect(X, 1) * rect(Y, 1)
Xc, Yc, Zc = cylinder(0, 0, 8, 3500, n)
print(Zc.shape)
np.savetxt('cylinder.txt', filtro1, delimiter=',')
filtro2 = [(Xc, Yc, Zc)]
print(len(filtro2))
h = fft * filtro1
ffti = np.fft.ifft2(np.fft.fftshift(h))
filter0 = 4000 * (rect(X, 1) * rect(Y, 1))
print(ffti.shape)

plt.show()

with open("Filter.csv", "w") as out_file:
    for i in range(len(Z)):
        for j in range(len(Z)):
            out_string = ""
            out_string += str(X[i, j])
            out_string += "," + str(Y[i, j])
            out_string += "," + str(filter0[i, j])
            out_string += "\n"
            out_file.write(out_string)

with open("Noise_Gauss.csv", "w") as out_file:
    for i in range(len(Z)):
        for j in range(len(Z)):
            out_string = ""
            out_string += str(X[i, j])
            out_string += "," + str(Y[i, j])
            out_string += "," + str(fft.real[i, j])
            out_string += "\n"
            out_file.write(out_string)


fig = plt.figure(figsize=plt.figaspect(0.5))
ax = plt.axes(projection='3d')
'''ax.plot_surface(X, Y, rect(X, 1)*rect(Y, 1)*4000, rstride=1, cstride=1,
                cmap='magma_r', edgecolor='none')'''
ax.plot_surface(Xc, Yc, Zc, alpha=0.5)

ax.plot_surface(X, Y, fft.real, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
'''plt.ylim(-1000, 1000)
plt.xlim(-1000, 1000)'''
#ax.set_zlim(-100, 100)
plt.show()

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax = fig.add_subplot(1, 3, 2, projection='3d')
ax.plot_surface(X, Y, Z1, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax = fig.add_subplot(1, 3, 3, projection='3d')
ax.plot_surface(X, Y, ffti.real, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plt.show()
