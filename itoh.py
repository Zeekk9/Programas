import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

t = np.linspace(-10, 10, 2000)


def func(t):
    f = t**3
    return f


def envolve(f):
    f = np.arctan2(np.sin(f), np.cos(f))
    return f


def itoh(W):
    Num_Datos = len(W)
    phi = np.zeros(len(W))
    phi[0] = W[0]
    for m in range(1, Num_Datos):
        Delta = W[m] - W[m - 1]
        WDelta = np.arctan2(np.sin(Delta), np.cos(Delta))
        phi[m] = phi[m - 1] + WDelta
    return phi


plt.subplot(211)
plt.ylabel('Función Original',size='19')
plt.plot(t, func(t))
plt.subplot(212)
plt.ylabel('Funcion envuelta',size='19')
plt.plot(t, envolve(func(t)))
'''plt.subplot(313)
plt.ylabel('Funcion desenvuelta',size='19')
plt.plot(t, itoh(envolve(func(t))))'''
plt.show()
