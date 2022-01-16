import cv2
import sys
import numpy as np


def drawCircleAroundBall(image, sizeOfBoundingBox = 3):
    # image = cv2.imread(im)
    # src = cv2.imread(im)
    src=image
    
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    image_grayscale = cv2.medianBlur(image_grayscale, 5)
    cv2.imshow("img", image_grayscale)

    rows = image_grayscale.shape[0]
    circles = cv2.HoughCircles(image_grayscale, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=1, maxRadius=10)


    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:

            x_center = i[0]
            y_center = i[1]
            radius = i[2]

            center = (x_center, y_center)
            # circle center
            cv2.circle(src, center, 1, (0,0,255), 3)
            # circle outline
            # cv2.circle(src, center, radius, (255, 0, 255), 2)

            x_left = x_center - radius * sizeOfBoundingBox
            x_right = x_center + radius * sizeOfBoundingBox
            y_top = y_center - radius * sizeOfBoundingBox
            y_bottom = y_center + radius * sizeOfBoundingBox

            cv2.rectangle(src, (x_left, y_top), (x_right, y_bottom), (255,0, 255), 2)          

        
    cv2.imshow("detected circles", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def loopThroughVideo(video):



    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imshow("frame", image)
        drawCircleAroundBall(image)
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            cv2.destroyAllWindows()
            break
        success,image = vidcap.read()

def testTracking(video):

    tracker = cv2.TrackerKCF_create()
    video = cv2.VideoCapture(video)
    ok,frame=video.read()
    bbox = cv2.selectROI(frame)
    ok = tracker.init(frame,bbox)
    while True:
        ok,frame=video.read()
        if not ok:
            break
        ok,bbox=tracker.update(frame)
        if ok:
            (x,y,w,h)=[int(v) for v in bbox]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
        else:
            cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow('Tracking',frame)
        if cv2.waitKey(1) & 0XFF==27:
            break
    cv2.destroyAllWindows()

# drawCircleAroundBall("table.jpg", 3)
loopThroughVideo('video3.mp4')
# testTracking('video2.mp4')

