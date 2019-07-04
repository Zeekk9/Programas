import matplotlib.pyplot as plt
import cv2
'''For use it, needs to load image in this form:
image = cv2.imread('path_to_image')
this code load the image in RGB'''


def RGBtoGray(load_image):
    gray_image = cv2.cvtColor(load_image, cv2.COLOR_BGR2GRAY)
    return gray_image
