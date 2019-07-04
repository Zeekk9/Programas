import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Simulated_PSI(object):
    def __init__(self, f0, f1, f2, a, m, phi):
        self._f0 = f0
        self._f1 = f1
        self._f2 = f2
        self._phi = phi
        self._a = a
        self._m = m

    def I0(self):
        I0 = self._a * (1 + self._m * np.cos(self._phi) + self._f0)
        return I0

    def I1(self):
        I1 = self._a * (1 + self._m * np.cos(self._phi) + self._f1)
        return I1

    def I2(self):
        I2 = self._a * (1 + self._m * np.cos(self._phi) + self._f2)
        return I2

    def phase(self):
        phi = np.arctan2((self.I2() - self.I1()) * np.cos(self._f0) + (self.I0() - self.I2()) * np.cos(self._f1) + (self.I1() - self.I0()) * np.cos(self._f2),
                       (self.I2() - self.I1()) * np.sin(self._f0) + (self.I0() - self.I2()) * np.sin(self._f1) + (self.I1() - self.I0()) * np.sin(self._f2))
        return phi
    def plot(self):
        unwraped = self.phase()
        xlim = unwraped[0, :].size
        ylim = unwraped[:, 0].size
        x = np.linspace(0, xlim, xlim)
        y = np.linspace(0, ylim, ylim)
        X, Y = np.meshgrid(x, y)
        phase = unwraped
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, phase, cmap='gray')
        plt.show()
