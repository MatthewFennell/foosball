import cv2
import numpy as np

def getCircles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100, maxRadius=50)
    print (circles)
    return circles