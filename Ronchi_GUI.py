from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plot
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
plt.style.use('ggplot')

n = 500
p_lim = 5
n_lim = -5
h = 1
uw = 1
t = np.linspace(n_lim, p_lim, n)


def rect_train(x, u, u_w, u_p, h):
    r = 0
    for i in range(-10, 10):
        r += np.where((np.abs(x - i) <= u_w / u_p), h, 0)
    return r


'''ronchi_train = 0
for i in range(-5, 5):
    ronchi_train += rect_train(t, 0, 1, 3, 1)'''


#################SLIDER####################
fig = plt.figure(figsize=plt.figaspect(1.0))
plt.subplots_adjust(left=0.25, bottom=0.25)
ax = fig.add_subplot(1, 2, 1)
t = np.linspace(n_lim, p_lim, n)
uw0 = 1
h0 = 1
#s = np.where(np.abs(t) <= uw0, h0, 0)
l, = plt.plot(t, rect_train(t, 0, 1, 3, 1), lw=2, color='red')
#plt.axis([n_lim, p_lim, -2*h, 2*h])
plt.axis([-10, 10, -2, 2])
axcolor = 'lightgoldenrodyellow'

uw = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
h = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

s_h = Slider(h, 'Altura', 0.0, 2.0, valinit=h0)
s_uw = Slider(uw, 'Fill Factor', 0.0, 10.0, valinit=uw0)


def update(val):
    s_h0 = s_h.val
    s_uw0 = s_uw.val
    l.set_ydata(rect_train(t, 0, s_uw0, 1, s_h0))
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
    np.fft.fftshift(rect_train(t, 0, uw0, 3, h0)))), lw=2, color='red')


axcolor = 'lightgoldenrodyellow'

uw = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
h = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)


def update2(val):
    s_h0 = s_h.val
    s_uw0 = s_uw.val
    k.set_ydata(np.fft.fftshift(np.fft.fft(
        np.fft.fftshift(rect_train(t, 0, s_uw0, 1, s_h0).real))))
    fig.canvas.draw_idle()


s_uw.on_changed(update2)
s_h.on_changed(update2)

plt.show()
