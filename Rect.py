from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
plt.style.use('fivethirtyeight')
# WINDOWS
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
# LINUX
manager = plt.get_current_fig_manager()
manager.window.showMaximized()


def rect(x, u_w, h):
    r = np.where(np.abs(x) <= u_w, h, 0)
    return r


n = 1000
p_lim = 5
n_lim = -5
h = 1
uw = 1
t = np.linspace(n_lim, p_lim, n)
rect = rect(t, uw, h)

rect2 = np.fft.fftshift(rect)
fft_rect = np.fft.fftshift(np.fft.fft(rect))

plt.subplot(211)
plt.plot(t, rect)
plt.subplot(212)
plt.plot(t, fft_rect)
plt.show()

'''fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.25, bottom = 0.25) '''


#################SLIDER####################
fig = plt.figure(figsize=plt.figaspect(1.0))
plt.subplots_adjust(left=0.25, bottom=0.25)
ax = fig.add_subplot(1, 2, 1)

t = np.linspace(n_lim, p_lim, n)
uw0 = 1
h0 = 1
#s = np.where(np.abs(t) <= uw0, h0, 0)
l, = plt.plot(t, np.where(np.abs(t) <= uw0, h0, 0), lw=2, color='red')
#plt.axis([n_lim, p_lim, -2*h, 2*h])

axcolor = 'lightgoldenrodyellow'

uw = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
h = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

s_h = Slider(h, 'Altura', 0.0, 2.0, valinit=h0)
s_uw = Slider(uw, 'Fill Factor', 0.0, 10.0, valinit=uw0)


def update(val):
    s_h0 = s_h.val
    s_uw0 = s_uw.val
    l.set_ydata(np.where(np.abs(t) <= s_uw0, s_h0, 0))
    fig.canvas.draw_idle()


s_uw.on_changed(update)
s_h.on_changed(update)


'''Seguundo grafico'''
ax = fig.add_subplot(1, 2, 2)
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.linspace(n_lim, p_lim, n)
uw0 = 1
h0 = 1
#s = np.fft.fftshift(np.fft.fft(np.where(np.abs(t) <= uw0, h0, 0)))
k, = plt.plot(t, np.fft.fftshift(np.fft.fft(
    np.fft.fftshift(np.where(np.abs(t) <= uw0, h0, 0)))), lw=2, color='red')
#plt.axis([n_lim, p_lim, -2*h, 2*h])

axcolor = 'lightgoldenrodyellow'

uw = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
h = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)


def update2(val):
    s_h0 = s_h.val
    s_uw0 = s_uw.val
    k.set_ydata(np.fft.fftshift(np.fft.fft(
        np.fft.fftshift(np.where(np.abs(t) <= s_uw0, s_h0, 0)))))
    fig.canvas.draw_idle()


s_uw.on_changed(update2)
s_h.on_changed(update2)

plt.show()
