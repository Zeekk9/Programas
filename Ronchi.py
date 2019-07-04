from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
plt.style.use('ggplot')
# WINDOWS
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
# LINUX
manager = plt.get_current_fig_manager()
manager.window.showMaximized()


def rect_train(x, u, u_w, u_p, h):
    r = np.where((np.abs(x-u) <= u_w/u_p), h, 0)
    return r


t = np.linspace(-10, 10, 500)
rect = rect_train(t, 0, 1, 1, 1)

rect_fft = np.fft.fftshift(rect)
rect_fft = np.fft.fft(rect_fft)
rect_fft = np.fft.fftshift(rect_fft)

ronchi_train = 0
for i in range(-5, 5):
    ronchi_train += rect_train(t, i, 1, 3, 1)

#ronchi_fft = np.fft.fftshift(ronchi_train)
ronchi_fft = np.fft.fft(ronchi_train)
ronchi_fft = np.fft.fftshift(ronchi_fft)

plt.subplot(221)
plt.plot(t, rect)
plt.subplot(222)
plt.plot(t, rect_fft.real)
plt.subplot(223)
plt.plot(t, ronchi_train)
plt.subplot(224)
plt.plot(t, ronchi_fft.real)
plt.show()
