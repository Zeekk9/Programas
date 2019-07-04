from itoh2d import itoh_2D
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D

# load the image
I1 = np.array(Image.open('Images\Image-4.bmp'), dtype='double')
I2 = np.array(Image.open('Images\Image-5.bmp'), dtype='double')
I3 = np.array(Image.open('Images\Image-6.bmp'), dtype='double')
I4 = np.array(Image.open('Images\Image-7.bmp'), dtype='double')
phi = np.arctan2(I1 - I3, I4 - I2)
unwraped = itoh_2D(phi)
xlim = unwraped[0, :].size
ylim = unwraped[:, 0].size
x = np.linspace(0, xlim, xlim)
y = np.linspace(0, ylim, ylim)
X, Y = np.meshgrid(x, y)
l = 170
p = np.polyfit(y, unwraped[:, l], 1)
portadora = np.zeros(unwraped.shape)

for n in range(0, x.size):
    portadora[:, n] = y * p[0] + p[1]

phase = portadora - unwraped

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, phase, cmap='gray')
plt.show()
