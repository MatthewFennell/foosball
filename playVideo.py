import cv2
import numpy as np
from findPlayers import getPlayerContours

cap = cv2.VideoCapture("video4.mp4")


def drawRectangles(frame, contours, color):
    numBoxes = 0
    for contour in contours:
        if 200<cv2.contourArea(contour)<5000:     
            numBoxes += 1       
            (xg,yg,wg,hg) = cv2.boundingRect(contour)
            cv2.rectangle(frame,(xg-20,yg-20),(xg+60, yg+60),color,2)
    cv2.waitKey(0)

while True:

    success, frame = cap.read()
    cv2.imshow("Original", frame)

    redContours = getPlayerContours(frame, False)
    blueContours = getPlayerContours(frame, True)
    drawRectangles(frame, redContours, (255,0,255))
    drawRectangles(frame, blueContours, (0, 255, 255))

    key = cv2.waitKey(1)

    cv2.imshow("Frame", frame)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()