import cv2
import sys
import numpy as np

def nothing(x):
    pass

useCamera=False

# Check if filename is passed
if (len(sys.argv) <= 1) :
    print("'Usage: python hsvThresholder.py <ImageFilePath>' to ignore camera and use a local image.")
    useCamera = True

# Create a window
cv2.namedWindow('image')
cv2.namedWindow('image2')

# create trackbars for color change
cv2.createTrackbar('HMin','image2',0,179,nothing) # Hue is from 0-179 for Opencv
cv2.createTrackbar('SMin','image2',0,255,nothing)
cv2.createTrackbar('VMin','image2',0,255,nothing)
cv2.createTrackbar('HMax','image2',0,179,nothing)
cv2.createTrackbar('SMax','image2',0,255,nothing)
cv2.createTrackbar('VMax','image2',0,255,nothing)

# Set default value for MAX HSV trackbars.
cv2.setTrackbarPos('HMin', 'image2', 0)
cv2.setTrackbarPos('SMin', 'image2', 128)
cv2.setTrackbarPos('VMin', 'image2', 102)
cv2.setTrackbarPos('HMax', 'image2', 72)
cv2.setTrackbarPos('SMax', 'image2', 215)
cv2.setTrackbarPos('VMax', 'image2', 221)

# Initialize to check if HSV min/max value changes
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# Output Image to display
if useCamera:
    cap = cv2.VideoCapture('video5.mp4')
    # Wait longer to prevent freeze for videos.
    waitTime = 10
else:
    img = cv2.imread(sys.argv[1])
    output = img
    waitTime = 33

while(1):

    if useCamera:
        # Capture frame-by-frame
        ret, img = cap.read()
        output = img

    # get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin','image2')
    sMin = cv2.getTrackbarPos('SMin','image2')
    vMin = cv2.getTrackbarPos('VMin','image2')

    hMax = cv2.getTrackbarPos('HMax','image2')
    sMax = cv2.getTrackbarPos('SMax','image2')
    vMax = cv2.getTrackbarPos('VMax','image2')

    # Set minimum and max HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Create HSV Image and threshold into a range.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(img,img, mask= mask)

    # Print if there is a change in HSV value
    if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display output image
    cv2.imshow('image',output)

    # Wait longer to prevent freeze for videos.
    if cv2.waitKey(waitTime) & 0xFF == ord('q'):
        break

# Release resources
if useCamera:
    cap.release()
cv2.destroyAllWindows()