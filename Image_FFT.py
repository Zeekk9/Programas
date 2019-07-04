import numpy as np
import scipy.ndimage
from scipy.misc.pilutil import Image
import matplotlib.pylab as plt
# opening the image and converting it to grayscale
a = Image.open('ultrasound_muscle.png').convert('L')

k = np.fft.fft2(a)
plt.imshow(k)
plt.show()