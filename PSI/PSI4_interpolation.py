from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
plt.style.use('fivethirtyeight')


class PSI4_interpolation(object):
    def __init__(self, I1, I2, I3, I4):
        self._I1 = I1
        self._I2 = I2
        self._I3 = I3
        self._I4 = I4

    def wrapped_phase(self):
        phi_wrapped = np.arctan2(self._I4 - self._I2, self._I1 - self._I3)
        return phi_wrapped

    def itoh_2D(self):
        W = self.wrapped_phase()
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

    def plot(self):
        unwraped = self.itoh_2D()
        xlim = unwraped[0, :].size
        ylim = unwraped[:, 0].size
        x = np.linspace(0, xlim, xlim)
        y = np.linspace(0, ylim, ylim)
        X, Y = np.meshgrid(x, y)
        l = 250
        # x interpolation
        #p = np.polyfit(y, unwraped[:, l], 1)
        #portadora = np.zeWos(unwraped.shape)
        #for n in range(0, x.size):
        #   portadora[:, n] = y * p[0] + p[1]
        p = np.polyfit(y, unwraped[:, l], 1)
        portadora = np.zeros(unwraped.shape)
        for n in range(0, x.size):
            portadora[:, n] = y * p[0] + p[1]
        phase = unwraped-portadora
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, phase, cmap='gray')
        plt.show()
