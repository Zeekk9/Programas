import cv2

# The function cv2.imshow() is used to display an image in a window
# The first argument of this function is the window name
# The second argument of this function is the image to be shown.
# In this case, the second argument is needed because we want to load the image in grayscale.
# Second argument is a flag specifying the way the image should be read.
# Value needed for loading an image in grayscale: 'cv2.IMREAD_GRAYSCALE'.
# load OpenCV logo image:
gray_img = cv2.imread('opencv_frame_1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image", gray_img)
cv2.waitKey(0)

# To get the dimensions of the image use img.shape
# If color image, img.shape returns returns a tuple of number of rows, columns and channels
# If grayscale, returns a tuple of number of rows and columns.
# So, it can be used to check if the loaded image is grayscale or color image.
# Get the shape of the image (in this case only two components!):
dimensions = gray_img.shape
print('dimensions:',dimensions)
# You can access a pixel value by row and column coordinates.
# For BGR image, it returns an array of (Blue, Green, Red) values.
# Get the value of the pixel (x=40, y=6):
i = gray_img[6, 40]
print('original pixel:',i)

# You can modify the pixel values of the image in the same way.# Set the pixel to black:
gray_img[6, 40] = 0
i = gray_img[6, 40]
print('Modified pixel:',i)
