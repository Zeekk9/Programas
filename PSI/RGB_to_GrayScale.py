import matplotlib.pyplot as plt
import cv2

image = cv2.imread('images\\opencv_frame_0.png')
print(image.shape)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)
A=[]
for i in range(0, len(gray_image[0, :])):
    A.append(max(gray_image[:, i]))

print(max(A))   
cv2.imwrite('gray.jpg', gray_image)
'''Now if you load the image:'''
plt.imshow(gray_image)
plt.show()
image = cv2.imread('gray.jpg')
print(image.shape)


'''It seems that you have saved the image as BGR, however it is not true, it is just opencv, by default it reads the image with 3 channels, and in the case it is grayscale it copies its layer three times. If you load again the image with scipy you could see that the image is indeed grayscale:'''

image2 = plt.imread('gray.jpg')
print(image2.shape)

'''So if you want to load a grayscale image you will need to set CV_LOAD_IMAGE_GRAYSCALE flag:
For opencv2 use:
image = cv2.imread('gray.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
For opencv 3 and up use'''

image = cv2.imread('gray.jpg', cv2.IMREAD_GRAYSCALE)
print(image.shape)
