import numpy as np
import matplotlib.pyplot as plt
xlim = 30
ylim = 30
n = 200
x = np.linspace(-xlim, xlim, n)
y = np.linspace(-ylim, ylim, n)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2

renglon, columna = Z.shape
k = 10
for k in range(renglon):
    print(Z[k])
