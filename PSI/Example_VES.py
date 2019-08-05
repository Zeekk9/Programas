import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import cv2
from PSI_VES import PSI_VES

# load the images
'''I0 = np.array(Image.open('Images\Old_1.bmp'), dtype='double')
I1 = np.array(Image.open('Images\Old_2.bmp'), dtype='double')
I2 = np.array(Image.open('Images\Old_3.bmp'), dtype='double')'''

I0 = np.array(Image.open('Images\Image-12.tif'), dtype='double')
I1 = np.array(Image.open('Images\Image-13.tif'), dtype='double')
I2 = np.array(Image.open('Images\Image-14.tif'), dtype='double')


I0_f = np.array(Image.open('Images\Image-17.tif'), dtype='double')
I1_f = np.array(Image.open('Images\Image-18.tif'), dtype='double')
I2_f = np.array(Image.open('Images\Image-19.tif'), dtype='double')


PSI = PSI_VES(I0, I1, I2,
              I0_f, I1_f, I2_f)
PSI.plot()
