from itoh2d import itoh_2D
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
#from PSI4 import PSI4
from PSI_interpolation import PSI4_interpolation
import cv2

# load the images
'''I1 = np.array(Image.open('Images\old_1.bmp'), dtype='double')
I2 = np.array(Image.open('Images\old_2.bmp'), dtype='double')
I3 = np.array(Image.open('Images\old_3.bmp'), dtype='double')
I4 = np.array(Image.open('Images\old_4.bmp'), dtype='double')'''

I1 = np.array(Image.open('Images\\Old_1.bmp'), dtype='double')
I2 = np.array(Image.open('Images\\Old_2.bmp'), dtype='double')
I3 = np.array(Image.open('Images\\Old_3.bmp'), dtype='double')
I4 = np.array(Image.open('Images\\Old_4.bmp'), dtype='double')

#PSI = PSI4(I1, I2, I3, I4, I1_f, I2_f, I3_f, I4_f)
PSI_old = PSI4_interpolation(
    I1, I2, I3, I4)
PSI_old.plot()
# PSI.plot()
