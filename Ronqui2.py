from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

t = t = np.linspace(0, 4, 500, endpoint=False)

'''
A 5 Hz waveform sampled at 500 Hz for 1 second:
from scipy import signal
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500, endpoint=False)
plt.plot(t, signal.square(2 * np.pi * 5 * t))
'''

rochi = signal.square(2 * np.pi * 1 * t)+1
rochi = np.fft.fftshift(rochi)
fft_rochi = np.fft.fftshift(np.fft.fft(rochi))
inv_fftrochi=np.fft.ifft(fft_rochi)
plt.subplot(311)
plt.plot(t, rochi)
plt.subplot(312)
plt.plot(t, fft_rochi.imag)
plt.subplot(313)
plt.plot(t,inv_fftrochi.real)
plt.show()

x = np.arange(-3, 3, 0.01)
y = np.zeros(len(x))
y[200:400] = 1

yShift = np.fft.fftshift(y)
fftyShift = np.fft.fft(yShift)
ffty = np.fft.fftshift(fftyShift)

'''plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
plt.plot(x,ffty.real)
plt.show()
'''
