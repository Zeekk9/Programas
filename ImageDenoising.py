import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images\\Image-12.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-12.png',dst)

img = cv2.imread('Images\\Image-13.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-13.png',dst)

img = cv2.imread('Images\\Image-14.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-14.png', dst)

img = cv2.imread('Images\\Image-15.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-15.png', dst)

img = cv2.imread('Images\\Image-16.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-16.png', dst)

img = cv2.imread('Images\\Image-17.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-17.png', dst)

img = cv2.imread('Images\\Image-18.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-18.png', dst)

img = cv2.imread('Images\\Image-19.tif')
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
dst = cv2.imwrite('Images\\Image-19.png', dst)
