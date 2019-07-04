import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('multi_1.png', cv2.IMREAD_GRAYSCALE)

y_centro1 =96
y_centro2 =137
d = y_centro2 - y_centro1
y_centro3 = y_centro2 + d
y_centro_1 = y_centro3 + d
y_centro_2 = y_centro_1 - d
h = round((106 - 81) / 2)

inter1 = img[y_centro1 - h : y_centro1 + h, 0::]
inter2 = img[y_centro2 - h : y_centro2 + h, 0::]
inter3 = img[y_centro3 - h : y_centro3 + h, 0::]
inter4 = img[y_centro_1 - h-20 : y_centro_1-20 + h, 0::]

plt.imshow(img)
plt.show()

plt.subplot(311)
plt.imshow(inter1)
plt.subplot(312)
plt.imshow(inter2)
plt.subplot(313)
plt.imshow(inter3)
plt.show()
