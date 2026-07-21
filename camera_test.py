import cv2
from matplotlib import pyplot as plt


def sketch_transform(image):
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (7, 7), 0)
    image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    _, mask = image_canny_inverted = cv2.threshold(
        image_canny, 30, 255, cv2.THRESH_BINARY_INV)
    return mask


cam_capture = cv2.VideoCapture(0)
cv2.destroyAllWindows()

upper_left = (50, 50)
bottom_right = (300, 300)

while True:
    _, image_frame = cam_capture.read()

    # Rectangle marker
    r = cv2.rectangle(image_frame, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = image_frame[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]



    cv2.imshow("Sketcher ROI", image_frame)
    if cv2.waitKey(1) == 13:
        break

cam_capture.release()
cv2.destroyAllWindows()
