import cv2
import numpy as np
from findPlayers import getPlayerContours
from findBall import getBallContours
from findCircles import getCircles

cap = cv2.VideoCapture("video5.mp4")

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def findBallByImage(frame):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread('ballThree.png')
    large_image = frame

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    return MPx, MPy, trows, tcols
    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(frame, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)



def drawRectangles(frame, contours, color):
    numBoxes = 0
    for contour in contours:
        if 200<cv2.contourArea(contour)<5000:     
            numBoxes += 1       
            (xg,yg,wg,hg) = cv2.boundingRect(contour)
            # the +- dictate how big the rectangle is
            cv2.rectangle(frame,(xg-10,yg-10),(xg+40, yg+40),color,2)

def drawCircles(frame, circles):
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,255), 3, 1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)


def play():
    tracker = tracker = cv2.legacy.TrackerMOSSE_create()
    ballIsTracked = False
    counter = 0
    frameCounter = 0

    while True:
        success, frame = cap.read()
        frame = rescale_frame(frame, percent=35)
        frameCounter += 1
        # crop the bottom 1/7th of the video
        crop_position = frame.shape[0] // 8
        frame = frame[0:frame.shape[0] - crop_position:]
        if success:
            # redContours = getPlayerContours(frame, False)
            # blueContours = getPlayerContours(frame, True)
            # drawRectangles(frame, redContours, (255,0,255))
            # drawRectangles(frame, blueContours, (0, 255, 255))

            # ballContours = getBallContours(frame)
            # drawRectangles(frame, ballContours, (0, 255, 255))

            # circles = getCircles(frame)
            # drawCircles(frame, circles)

            if not ballIsTracked or frameCounter % 50 == 0:
                x,y,w,h = findBallByImage(frame)
                bbox = (x,y,w,h)
                tracker.init(frame, bbox)
                ballIsTracked = True
            elif frameCounter % 10 == 0:
                success, bbox = tracker.update(frame)

            if success:
                drawBox(frame, bbox)
            else:
                ballIsTracked = False
                cv2.putText(frame, "Lost", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 2)



            key = cv2.waitKey(1)
            cv2.imshow("Frame", frame)
        else:
            break
            cap.release()
            cv2.destroyAllWindows()

        if key == 27:
            break

play()
