import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
#from PSI4 import PSI4
from PSI_VES_Inter import PSI_VES_Inter
import cv2
from Surf import surf

x = np.linspace(-3, 3, 2000)
y = np.linspace(-3, 3, 2000)
X, Y = np.meshgrid(x, y)

phi_prue = np.exp(-((X ** 2 + Y ** 2) / 20))
Amp_prue = 10
E_prue = Amp_prue * np.exp(1j * phi_prue)
phi_ref = np.zeros(x.shape) + 1 + np.zeros(y.shape) + 1
Amp_ref = 1
alpha1 = 7 * np.pi / 10
alpha2 = 4 * np.pi / 3
print('originales', alpha1, alpha2)
print('resta original', alpha2 - alpha1)
E_ref_1 = Amp_ref * np.exp(1j * phi_ref)
E_ref_2 = Amp_ref * np.exp(1j * (phi_ref - alpha1))
E_ref_3 = Amp_ref * np.exp(1j * (phi_ref - alpha2))

E_0 = E_ref_1 + E_prue
E_1 = E_ref_2 + E_prue
E_2 = E_ref_3 + E_prue

I0 = E_0 * np.conj(E_0)
I1 = E_1 * np.conj(E_1)
I2 = E_2 * np.conj(E_2)


'''plt.subplot(131)
plt.imshow(I0.real, cmap='gray')
plt.subplot(132)
plt.imshow(I1.real, cmap='gray')
plt.subplot(133)
plt.imshow(I2.real, cmap='gray')
plt.show()'''

'''
I1 = np.array(Image.open('Images\old_1.bmp'), dtype='double')
I2 = np.array(Image.open('Images\old_2.bmp'), dtype='double')
I3 = np.array(Image.open('Images\old_3.bmp'), dtype='double')
I4 = np.array(Image.open('Images\old_4.bmp'), dtype='double')
'''

'''I0 = np.array(cv2.imread('Images\\1.png',
                         cv2.IMREAD_UNCHANGED), dtype='double')
I1 = np.array(cv2.imread('Images\\2.png',
                         cv2.IMREAD_UNCHANGED), dtype='double')
I2 = np.array(cv2.imread('Images\\3.png',
                         cv2.IMREAD_UNCHANGED), dtype='double')'''

'''I0_ = cv2.imread('Images\\I0.png', cv2.COLOR_BGR2GRAY)
I1_ = cv2.imread('Images\\I1.png', cv2.COLOR_BGR2GRAY)
I2_ = cv2.imread('Images\\I2.png', cv2.COLOR_BGR2GRAY)'''

'''I0 = cv2.imread('Images\\I0.png', cv2.COLOR_BGR2GRAY)
I1 = cv2.imread('Images\\I1.png', cv2.COLOR_BGR2GRAY)
I2 = cv2.imread('Images\\I2.png', cv2.COLOR_BGR2GRAY)'''

PSI_old = PSI_VES_Inter(I0.real, I1.real, I2.real)
PSI_old.plot()
surf(phi_prue)
