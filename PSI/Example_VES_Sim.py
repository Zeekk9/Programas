import numpy as np
from Simulated_PSI import Simulated_PSI
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PSI_VES import PSI_VES

a = 10
b = 20
n = 1000
x = np.linspace(-a, a, n)
y = np.linspace(-b, b, n)
X, Y = np.meshgrid(x, y)
Z = 10 * np.exp(-((X / 4) ** 2 + (Y / 4) ** 2))
A_ = 1
m_ = 1

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, Z, cmap='gray')
ax = fig.add_subplot(122)
plt.imshow(Z, cmap='gray')
plt.grid()
plt.show()

f0 = 0
f1 = 0.7
f2 = 4.0

I0 = A_ * (1 + m_ * np.cos(Z+f0))
I1 = A_ * (1 + m_ * np.cos(Z+f1))
I2 = A_ * (1 + m_ * np.cos(Z+f2))

nn = PSI_VES(I0, I1, I2)
nn.plot()
