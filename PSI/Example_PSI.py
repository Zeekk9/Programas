from PSI4 import PSI4
import numpy as np
from PIL import Image

I0 = np.array(Image.open('Images\Image.tif'), dtype='double')
I1 = np.array(Image.open('Images\Image-1.tif'), dtype='double')
I2 = np.array(Image.open('Images\Image-2.tif'), dtype='double')
I3 = np.array(Image.open('Images\Image-3.tif'), dtype='double')

I0_f = np.array(Image.open('Images\Image-4.tif'), dtype='double')
I1_f = np.array(Image.open('Images\Image-5.tif'), dtype='double')
I2_f = np.array(Image.open('Images\Image-6.tif'), dtype='double')
I3_f = np.array(Image.open('Images\Image-7.tif'), dtype='double')


a = PSI4(I0, I1, I2, I3, I0_f, I1_f, I2_f, I3_f)
a.plot()
