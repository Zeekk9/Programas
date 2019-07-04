from itoh2d import itoh_2D
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
#from PSI4 import PSI4
from PSI3_VES import PSI_VES
import cv2

# load the images
'''I1 = np.array(Image.open('Images\old_1.bmp'), dtype='double')
I2 = np.array(Image.open('Images\old_2.bmp'), dtype='double')
I3 = np.array(Image.open('Images\old_3.bmp'), dtype='double')
I4 = np.array(Image.open('Images\old_4.bmp'), dtype='double')'''

I1 = np.array(cv2.imread('Images\\I1.png',
                         cv2.IMREAD_UNCHANGED), dtype='double')
I2 = np.array(cv2.imread('Images\\I2.png',
                         cv2.IMREAD_UNCHANGED), dtype='double')
I3 = np.array(cv2.imread('Images\\I3.png',
                         cv2.IMREAD_UNCHANGED), dtype='double')

PSI_old = PSI_VES(I1, I2, I3)
PSI_old.plot()
