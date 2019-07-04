import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('fivethirtyeight')

'''This module do the Phase shifting 
interferometry method. This need call it as
python PSI(I1,I2,I3,I4), where I1... are the images taken with the module PSI_Camera.py'''

class PSI4(object):
    def __init__(self, I1, I2, I3, I4, I1_f, I2_f, I3_f, I4_f):
        self._I1 = I1
        self._I2 = I2
        self._I3 = I3
        self._I4 = I4
        self._I1_f = I1_f
        self._I2_f = I2_f
        self._I3_f = I3_f
        self._I4_f = I4_f

    def wrapped_phase(self):
        phi_wrapped = np.arctan2(self._I4- self._I2, self._I1 - self._I3)
        return phi_wrapped

    def wrapped_phase_f(self):
        phi_wrapped = np.arctan2(self._I4_f - self._I2_f, self._I1_f - self._I3_f)
        return phi_wrapped

    def itoh_2D(self,W):
        renglon, columna = W.shape
        phi = np.zeros(W.shape)
        psi = np.zeros(W.shape)
        phi[0, 0] = W[0, 0]
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
        unwraped = self.itoh_2D(self.wrapped_phase())
        unwraped_f = self.itoh_2D(self.wrapped_phase_f())
        phase = unwraped - unwraped_f
        xlim = unwraped[0, :].size
        ylim = unwraped[:, 0].size
        x = np.linspace(0, xlim, xlim)
        y = np.linspace(0, ylim, ylim)
        X, Y = np.meshgrid(x, y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, phase, cmap='gray')
        plt.show()
