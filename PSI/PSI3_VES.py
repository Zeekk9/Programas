
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
plt.style.use('fivethirtyeight')

'''This module do the Phase shifting 
interferometry method. This need call it as
python PSI(I1,I2,I3,I4), where I1... are the images taken with the module PSI_Camera.py'''


class PSI_VES(object):
    def __init__(self, I0, I1, I2):
        self._I0 = I0
        self._I1 = I1
        self._I2 = I2

    def VES(self):
        p = self._I0 - self._I1
        q = self._I1 - self._I2
        r = self._I0 - self._I2
        A1 = np.trace(np.dot(q.transpose(), r))
        B1 = np.trace(np.dot(q.transpose(), q)) * np.trace(np.dot(r.transpose(), r))
        A2 = np.trace(np.dot(p.transpose(), r))
        B2 = np.trace(np.dot(p.transpose(), p)) * np.trace(np.dot(r.transpose(), r))
        alpha1 = 2 * np.arccos(A1 / np.sqrt(B1))
        alpha2 = 2 * np.arccos(A2 / np.sqrt(B2)) + alpha1
        phi_wrapped = np.arctan2(self._I2 - self._I1 + (self._I0 - self._I2) * np.cos(alpha1) - (self._I0 - self._I1) * np.cos(
            alpha2), (self._I0 - self._I2) * np.sin(alpha1) - (self._I0 - self._I1) * np.sin(alpha2))
        print(alpha1, alpha2)
        print('resta:', alpha2 - alpha1)
        return phi_wrapped

    def itoh_2D(self, W):
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
        unwraped = self.itoh_2D(self.VES())
        xlim = unwraped[0, :].size
        ylim = unwraped[:, 0].size
        x = np.linspace(0, xlim, xlim)
        y = np.linspace(0, ylim, ylim)
        X, Y = np.meshgrid(x, y)
        '''l = 30
        p = np.polyfit(y, unwraped[:, l], 1)
        portadora = np.zeros(unwraped.shape)
        for n in range(0, x.size):
            portadora[:, n] = n * p[0] + p[1]'''
        phase = unwraped
        fig = plt.figure()
        ax = fig.add_subplot(121, projection='3d')
        ax.plot_surface(X, Y, phase, cmap='gray')
        ax = fig.add_subplot(122)
        plt.imshow(phase,cmap='gray')
        plt.grid()
        plt.show()

