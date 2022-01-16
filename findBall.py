import cv2
import numpy as np

def getBallContours(frame):
    lower = np.array([32, 120, 90])
    upper = np.array([45, 255, 255])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("Mask", mask)
    colorContours = cv2.findContours(mask.copy(),
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    return colorContours