
import cv2
import matplotlib.pyplot as plt
refPt = []


def show():
    global image, refPt
    # create a copy so the drawn rectangles wont show up in subimages
    img_copy = image.copy()
    # create a subimage in a separate window
    # similar code can be used that checks if 4 points are selected, then saves the subimages and exits script
    i = 0
    for rect in refPt:
        subimage = img_copy[rect[0][1]:rect[1][1], rect[0][0]:rect[1][0]]
        cv2.imshow("image" + str(i), subimage)
        img_name = "Images\opencv_frame_{}.png".format(i)
        cv2.imwrite(img_name, subimage)
        i += 1
        
    # draw rectangle on full image
    for rect in refPt:
        cv2.rectangle(img_copy, rect[0], rect[1], (0, 255, 0), 2)
    # show full image
    cv2.imshow("image", img_copy)


def click_and_crop(event, x, y, flags, param):
    global refPt
    if event == cv2.EVENT_LBUTTONUP:
        # create tuples with two opposite cornerpoints and add to list
        point_a = (x-80, y-12)
        point_b = (x+80, y+12)
        refPt.append((point_a, point_b))
        # show images
        show()


# load and display image
image = cv2.imread('ROI_multi_1.png')

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
show()

cv2.waitKey(0)
cv2.destroyAllWindows()
image0 = cv2.imread('Images\\opencv_frame_0.png')
image1 = cv2.imread('Images\\opencv_frame_1.png')
image2 = cv2.imread('Images\\opencv_frame_2.png')

plt.subplot(311)
plt.imshow(image0)
plt.subplot(312)
plt.imshow(image1)
plt.subplot(313)
plt.imshow(image2)
plt.show()
