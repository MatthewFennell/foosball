import cv2
import numpy as np

cap = cv2.VideoCapture("video4.mp4")

while True:

    success, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])
    src = frame
    test = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # src[:,:,2] = np.zeros([src.shape[0], src.shape[1]])
    # # src[:,:,0] = np.zeros([src.shape[0], src.shape[1]])
    # src[:,:,1] = np.zeros([src.shape[0], src.shape[1]])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()