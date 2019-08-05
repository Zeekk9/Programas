import cv2
import matplotlib.pyplot as plt
# Load image using cv2.imread:
img_OpenCV = cv2.imread('opencv_frame_1.png')
# Split the loaded image into its three channels (b, g, r):
b, g, r = cv2.split(img_OpenCV)
cv2.imshow("Blue", b)
cv2.waitKey(0)
cv2.imshow("Green", g)
cv2.waitKey(0)
cv2.imshow("Red", r)
cv2.waitKey(0)
# Merge again the three channels but in the RGB format:
img_matplotlib = cv2.merge([r, g, b])
cv2.imshow("img_matplotlib", img_matplotlib)
cv2.waitKey(0)

# Show both images (img_OpenCV and img_matplotlib) using matplotlib
# This will show the image in wrong color:
plt.subplot(121)
plt.imshow(img_OpenCV)
# This will show the image in true color:
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()

# Show both images (img_OpenCV and img_matplotlib) using cv2.imshow()
# This will show the image in true color:
cv2.imshow('bgr image', img_OpenCV)
# This will show the image in wrong color:
cv2.imshow('rgb image', img_matplotlib)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Using numpy capabilities to get the channels and to build the RGB image
# Get the three channels (instead of using cv2.split):
B = img_OpenCV[:, :, 0]
G = img_OpenCV[:, :, 1]
R = img_OpenCV[:, :, 2]
# Transform the image BGR to RGB using Numpy capabilities:
img_matplotlib = img_OpenCV[:, :, ::-1]
plt.subplot(131)
plt.imshow(B)
plt.subplot(132)
plt.imshow(G)
plt.subplot(133)
plt.imshow(R)
plt.show()

# Transform the image BGR to RGB using Numpy capabilities:
img_matplotlib = img_OpenCV[:, :, ::-1]
print(img_matplotlib.shape)
