from scipy.integrate import simps
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn')
import time

star_time=time.time()

class Gauss:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def random(self):
        num = np.random.randint(-20, 20)
        while num == 0:
            num = np.random.randint(-20, 20)
        return num

    def random_pos(self):
        num = np.random.randint(1, 5)
        return num

    def gauss_random(self):
        f = 0
        for i in range(0, 50):  
            f = self.random_pos() * np.exp(-(self._x - self.random()) ** 2 / (2 * self.random()
** 2) - (self._y - self.random()) ** 2 / (2 * self.random() ** 2)) + f
        return f

    def gaussian(self, A, x, x0, y, y0, sigmax, sigmay):
        f = A * np.exp(-(x - x0) ** 2 / (2 * sigmax ** 2) -
                       (y - y0) ** 2 / (2 * sigmay ** 2))
        return f

    def plane(self):
        Z = np.zeros(self._x.shape) + 10 + np.zeros(self._y.shape) + 20
        noise = np.random.normal(0, 1, Z.shape)
        return Z

    def phase(self):
        phase = (self._x ** 2 - self._y ** 2) / 10
        noise = np.random.normal(0, 0.5, Z.shape)
        return phase

    def gauss_random_noise(self):
        g = self.gauss_random()
        noise = np.random.normal(0, 0.2, g.shape)
        return g

    def savetxt(self, X, Y, Z, name):
        n, m = Z.shape
        with open(name, "w") as out_file:
            for i in range(n):
                for j in range(m):
                    out_string = ""
                    out_string += str(X[i, j])
                    out_string += "," + str(Y[i, j])
                    out_string += "," + str(Z[i, j])
                    out_string += "\n"
                    out_file.write(out_string)

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

xlim = 10
ylim = 30
n = 400
m = 1000
x = np.linspace(-xlim, xlim, n)
y = np.linspace(-ylim, ylim, m)
X, Y = np.meshgrid(x, y)
gauss = Gauss(X, Y)
Z = gauss.gauss_random_noise()

Amp_ref = gauss.gauss_random_noise()
phase_ref = gauss.phase()

Amp_pru = gauss.gauss_random_noise()
phase_prue = gauss.plane()

E_ref = Amp_ref * np.exp(1j * phase_ref)
E_prueba = Amp_pru * np.exp(1j * phase_prue)

E = E_ref + E_prueba
#I1 = abs(E) ** 2

a = Amp_pru ** 2 + Amp_ref ** 2
b = 2 * Amp_pru * Amp_ref

phi_ = phase_ref - phase_prue
phi_wraped = np.arctan2(np.sin(phi_), np.cos(phi_))

I1 = E * np.conj(E)
I2 = a + b * np.cos(phi_)

'''
gauss.savetxt(X, Y, I1.real, "Iabs.csv")
gauss.savetxt(X, Y, I2.real, "I_rec.csv")
gauss.savetxt(X, Y, Amp_ref, "Amp_ref.csv")
gauss.savetxt(X, Y, Amp_pru, "Amp_pru.csv")
gauss.savetxt(X, Y, E_prueba.real, "E_prueba_real.csv")
gauss.savetxt(X, Y, E_prueba.imag, "E_prueba_imag.csv")
gauss.savetxt(X, Y, E_ref.real, "E_ref_real.csv")
gauss.savetxt(X, Y, E_ref.imag, "E_ref_imag.csv")
gauss.savetxt(X, Y, phase_ref, "phase_ref.csv")
gauss.savetxt(X, Y, phase_prue, "phase_prue.csv")
'''

N = 4
n = np.arange(0, 4, 1)
alpha = 2 * np.pi * n / N
E_r0 = Amp_ref * np.exp(1j * (phase_ref + alpha[0]))
E_r1 = Amp_ref * np.exp(1j * (phase_ref + alpha[1]))
E_r2 = Amp_ref * np.exp(1j * (phase_ref + alpha[2]))
E_r3 = Amp_ref * np.exp(1j * (phase_ref + alpha[3]))

E_0 = E_r0 + E_prueba
E_1 = E_r1 + E_prueba
E_2 = E_r2 + E_prueba
E_3 = E_r3 + E_prueba

I0 = E_0 * np.conj(E_0)
I1 = E_1 * np.conj(E_1)
I2 = E_2 * np.conj(E_2)
I3 = E_3 * np.conj(E_3)
plt.imshow(I0.real)
plt.show()

'''
I0 = a + b * np.cos(phi_ + alpha[0])
I1 = a + b * np.cos(phi_ + alpha[1])
I2 = a + b * np.cos(phi_ + alpha[2])
I3 = a + b * np.cos(phi_ + alpha[3])
'''

phi = np.arctan2((I3.real - I1.real), (I2.real - I0.real))
phi_unwrap = gauss.itoh_2D(phi)

# print(phi_wraped.shape,phi_.shape,phi_unwrap.shape)

'''gauss.savetxt(X, Y, phi_, "phi_original.csv")
gauss.savetxt(X, Y, phi, "phi_wrapped.csv")
gauss.savetxt(X, Y, -phi_unwrap, "phi_unwrapped.csv")'''

fig = plt.figure()
ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(X, Y, phi_, cmap='jet')
plt.title('Phase Original', fontsize='20')
ax = fig.add_subplot(132, projection='3d')
plt.title('Wrapped Phase', fontsize='20')
ax.plot_surface(X, Y, phi, cmap='jet')
ax = fig.add_subplot(133, projection='3d')
ax.plot_surface(X, Y, -phi_unwrap, cmap='jet')
plt.title('Unwrapped Phase', fontsize='20')
print("---%s seconds---"%(time.time()-star_time))
plt.show()