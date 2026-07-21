import numpy as np
import matplotlib.pylab as plt



n = 200
t = np.linspace(-10, 10, n)
pure = np.sin(t)
noise = np.random.normal(0, 0.1, pure.shape)
signal = pure + noise
fft = np.fft.fftshift(np.fft.fft(signal))


def rect(x, h):
    return np.where(abs(x) <= 1, h, 0)

plt.subplot(211)
plt.plot(t, fft.imag)
plt.subplot(212)
plt.plot(t, fft.real)
plt.show()

h = fft * rect(t, 1)
ffti = np.fft.ifft(np.fft.fftshift(h))

plt.plot(t, signal)
plt.show()

plt.plot(t, rect(t, 1))
plt.plot(t, fft.real)
plt.show()

plt.plot(t, h.imag)
plt.show()

plt.plot(t, ffti.real)
plt.plot(t, pure)
plt.show()

plt.subplot(311)
plt.plot(t, signal)
plt.subplot(312)
plt.plot(t, pure)
plt.subplot(313)
plt.plot(t, ffti.real)
plt.show()
plt.plot(t, ffti.real, t, signal, t, pure)
plt.show()
