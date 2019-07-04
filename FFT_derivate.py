import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

N = 100
L = 10
x = np.linspace(-L, L, N)  

y = x ** 6
dy_analytical = 6 * x**5
k = 2 * np.pi*np.fft.fftfreq(len(x), d=2*L/N)*1j
fd = np.fft.ifft(k * np.fft.fft(y))

plt.plot(x, k.imag)
plt.show()
plt.subplot(211)
plt.plot(x, dy_analytical, label='analytical der')
plt.legend(loc='best')
plt.subplot(212)
plt.plot(x, fd.real, label='fft der',c='r')
plt.ylim(min(dy_analytical), max(dy_analytical))
plt.legend(loc='best')
plt.show()