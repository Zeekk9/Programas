import matplotlib.pyplot as plt
import numpy as np

def surf(phi):
    unwraped=phi
    xlim = unwraped[0, :].size
    ylim = unwraped[:, 0].size
    x = np.linspace(0, xlim, xlim)
    y = np.linspace(0, ylim, ylim)
    X, Y = np.meshgrid(x, y)
    phase = unwraped
    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(X, Y, phase, cmap='gray')
    ax = fig.add_subplot(122)
    plt.imshow(phase, cmap='gray')
    plt.grid()
    plt.show()
