import cv2
import numpy as np

# red = [122, 170]
# gre = [25. 130]
# blu = [20, 80]

def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        # print("Red: ",colorsR)
        # print("Green: ",colorsG)
        # print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        # print("Coordinates of pixel: X: ",x,"Y: ",y)


cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

capture = cv2.VideoCapture('video4.mp4')

while(True):

    ret, frame = capture.read()

    cv2.imshow('mouseRGB', frame)

    cv2.waitKey(0)

    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()
