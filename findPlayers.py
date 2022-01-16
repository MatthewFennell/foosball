import cv2
import numpy as np

def getColorRanges(isBlue):
    if (isBlue):
        return np.array([100,150,0]), np.array([125,255,255])
    return np.array([0,100,50]), np.array([5,255,255])


def getPlayerContours(frame, isBlue):
    lower_blue, upper_blue = getColorRanges(isBlue)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    colorContours = cv2.findContours(mask.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    return colorContours