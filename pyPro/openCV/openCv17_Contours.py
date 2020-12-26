import cv2
import numpy as np 
print(cv2.__version__)

def nothing(x):
    pass

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

cv2.namedWindow('TrackBar')
cv2.moveWindow('TrackBar', 1320, 0)

cv2.createTrackbar('hueLower', 'TrackBar', 0, 179, nothing)
cv2.createTrackbar('hueHigher', 'TrackBar',30, 179, nothing)
cv2.createTrackbar('hue2Lower', 'TrackBar', 175, 179, nothing)
cv2.createTrackbar('hue2Higher', 'TrackBar',160, 179, nothing)
cv2.createTrackbar('satLower', 'TrackBar', 150, 255, nothing)
cv2.createTrackbar('satHigher', 'TrackBar',255, 255, nothing)
cv2.createTrackbar('valLower', 'TrackBar', 100, 255, nothing)
cv2.createTrackbar('valHigher', 'TrackBar', 255, 255, nothing)

# cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    # frame = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hueLow = cv2.getTrackbarPos('hueLower', 'TrackBar')
    hueUp = cv2.getTrackbarPos('hueHigher', 'TrackBar')
    hue2Low = cv2.getTrackbarPos('hue2Lower', 'TrackBar')
    hue2Up = cv2.getTrackbarPos('hue2Higher', 'TrackBar')
    lS = cv2.getTrackbarPos('satLower', 'TrackBar')
    uS = cv2.getTrackbarPos('satHigher', 'TrackBar')
    lV = cv2.getTrackbarPos('valLower', 'TrackBar')
    uV = cv2.getTrackbarPos('valHigher', 'TrackBar')

    l_b = np.array([hueLow, lS, lV])
    u_b = np.array([hueUp, uS, uV])

    l_b2 = np.array([hue2Low, lS, lV])
    u_b2 = np.array([hue2Up, uS, uV])

    FGmask = cv2.inRange(hsv, l_b, u_b)
    FGmask2 = cv2.inRange(hsv, l_b2, u_b2)
    FGmaskComp = cv2.add(FGmask, FGmask2)
    cv2.imshow('FGmaskComp', FGmaskComp)
    cv2.moveWindow('FGmaskComp', 0, 410) 

    contours, _ = cv2.findContours(FGmaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x : cv2.contourArea(x), reverse = True)
    for cnt in contours :
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        if area >= 100:
            # cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 2)
            cv2.rectangle(frame, (x , y), (x+w, y+h), (255, 0, 0), 2)
            xCenter = int(x + (w/2))
            yCenter = int(y + (h/2))
            cv2.line(frame, (xCenter, 0), (xCenter, 480), (0, 255, 0), 1)
            cv2.line(frame, (0, yCenter), (640, yCenter), (0, 255, 0), 1)
    # cv2.drawContours(frame, contours, 0, (255, 0, 0), 2)
    # FG = cv2.bitwise_and(frame, frame, mask=FGmaskComp)
    # cv2.imshow('FG', FG)
    # cv2.moveWindow('FG', 500, 0) 

    # BGmask = cv2.bitwise_not(FGmaskComp)
    # cv2.imshow('BGmask', BGmask)
    # cv2.moveWindow('BGmask', 500, 410)

    # BG = cv2.cvtColor(BGmask, cv2.COLOR_GRAY2BGR)

    # Comp = cv2.add(FG, BG)
    # cv2.imshow('Comp', Comp)
    # cv2.moveWindow('Comp', 1000, 410)

    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0, 0)

    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()