import cv2
# The function cv2.imread() is used to read an image from the the working directory
# Alternatively, you should provide a full path of the image:
# Load OpenCV logo image (in this case from the working directoy):
img = cv2.imread('opencv_frame_1.png')

# To get the dimensions of the image use img.shape
# img.shape returns a tuple of number of rows, columns and channels (if a colour image)
# If image is grayscale, img.shape returns a tuple of number of rows and columns.
# So,it can be used to check if loaded image is grayscale or color image.
# Get the shape of the image:
dimensions = img.shape
print('dimensions:',dimensions)
# Total number of elements is obtained by img.size:
total_number_of_elements = img.size
print('total numeber of elements:',total_number_of_elements)

# Image datatype is obtained by img.dtype.
# img.dtype is very important because a large number of errors is caused by invalid datatype
# Get the image datatype:
image_dtype = img.dtype
print('image type:', image_dtype)

# The function cv2.imshow() is used to display an image in a window
# The first argument of this function is the window name
# The second argument of this function is the image to be shown.
# Each created window should have different window names.
# Show original image:
cv2.imshow("original image", img)
# The function cv2.waitKey(), which is a keyboard binding function, waits for any keyboard event.# This function waits the value indicated by the argument (in milliseconds). # If any keyboard event is produced in this period of time, the program continues its execution# If the value of the argument is 0, the program waits indefinitely until a keyboard event is produced:
cv2.waitKey(0)
# A pixel value can be accessed by row and column coordinates.# In case of BGR image, it returns an array of (Blue, Green, Red) values.# Get the value of the pixel (x=40, y=6):
(b, g, r) = img[6, 40]
# We can only  access one channel at a time.
# In this case, we will use row, column and the index of the desired channel for indexing.
# Get only blue value of the pixel (x=40, y=6):
b = img[6, 40, 0]
print(b)

# The pixel values can be also modified in the same way - (b, g, r) format:
img[6, 40] = (0, 0, 255)
# In this case, we get the top left corner of the image:
top_left_corner = img[0:50, 0:50]
