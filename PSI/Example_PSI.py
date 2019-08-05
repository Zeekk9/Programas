from PSI4 import PSI4
import numpy as np
from PIL import Image

I0 = np.array(Image.open('Images\Image-12.png'), dtype='double')
I1 = np.array(Image.open('Images\Image-13.png'), dtype='double')
I2 = np.array(Image.open('Images\Image-14.png'), dtype='double')
I3 = np.array(Image.open('Images\Image-15.png'), dtype='double')

I0_f = np.array(Image.open('Images\Image-16.png'), dtype='double')
I1_f = np.array(Image.open('Images\Image-17.png'), dtype='double')
I2_f = np.array(Image.open('Images\Image-18.png'), dtype='double')
I3_f = np.array(Image.open('Images\Image-19.png'), dtype='double')


a = PSI4(I0[:, :, 0], I1[:, :, 0], I2[:, :, 0], I3[:, :, 0],
         I0_f[:, :, 0], I1_f[:, :, 0], I2_f[:, :, 0], I3_f[:, :, 0])
a.plot()
