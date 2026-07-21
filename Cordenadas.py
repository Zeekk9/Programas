import cv2
import numpy as np

#open image
img = cv2.imread('demo2.png')

#convert to black and white
bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#threshold image
ret, thresh = cv2.threshold(bw, 127, 255, 0)

#find contours
im2, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#obtain the first 2 points of contours
cntx1 = contours[0][0]
cntx = contours[0][1]

#convert coords to points
pt1 = (cntx1[0][0], cntx1[0][1])
pt2 = (cntx[0][0], cntx[0][1])

#draw circles on coordinates
cv2.circle(img, pt1, 5, (0, 255, 0), -1)
cv2.circle(img, pt2, 5, (0, 255, 0), -1)

#display the image
cv2.imshow('f', img)

cv2.waitKey(0)
cv2.destroyAllWindows()