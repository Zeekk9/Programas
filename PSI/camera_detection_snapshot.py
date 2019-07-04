import numpy as np
import cv2
import time

color = (255, 0, 0)
thickness = 2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
img_counter = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret = 1 if the video is captured; frame is the image
    k = cv2.waitKey(1)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(gray,(21,21),0)
    ret, thresh = cv2.threshold(gray, 10, 20, cv2.THRESH_BINARY_INV)
    img1, contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        c = max(contours, key=cv2.contourArea)  # find the largest contour
        # get bounding box of largest contour
        x, y, w, h = cv2.boundingRect(c)
        # img2=cv2.drawContours(frame, c, -1, color, thickness) # draw largest contour
        img2 = cv2.drawContours(
            frame, contours, -1, color, thickness)  # draw all contours
        # draw red bounding box in img
        img3 = cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Contour', img3)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break

    elif k % 256 == 32:
            # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
