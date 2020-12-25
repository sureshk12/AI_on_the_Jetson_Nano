import cv2
import numpy as np
import random
print(cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)

x, y, dx, dy, dirX, dirY = 100, 100, 100, 100, 5, 5

addingImage = np.ones((480, 640), np.uint8)
addingImage[:] = 255
invAddingImage = np.zeros((480, 640, 3), np.uint8)


imgPl = cv2.imread('pl.jpg')
imgPl = cv2.resize(imgPl, (dx, dy))
cv2.imshow('PLImage', imgPl)
cv2.moveWindow('PLImage', 700, 0)

imgPlGray = cv2.cvtColor(imgPl, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgPlGray', imgPlGray)
cv2.moveWindow('imgPlGray', 800, 0)

_, BgMask = cv2.threshold(imgPlGray, 250, 255, cv2.THRESH_BINARY)
cv2.imshow('BgMask', BgMask)
cv2.moveWindow('BgMask', 900, 0)

FgMask = cv2.bitwise_not(BgMask)
FG = cv2.bitwise_and(imgPl, imgPl, mask = FgMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG', 1000, 0)

while True:
    ret, frameOriginal = cam.read()
    frameOriginal = cv2.flip(frameOriginal, 1)
    cv2.imshow('Original', frameOriginal)
    cv2.moveWindow('Original', 0, 0)

    ROI = frameOriginal[y:y+dy, x:x+dx]
    ROIBG = cv2.bitwise_and(ROI,ROI, mask= BgMask)
    cv2.imshow('ROIBG', ROIBG)
    cv2.moveWindow('ROIBG', 1100, 0)

    ROIadded = cv2.add(FG, ROIBG)
    cv2.imshow('ROIadded', ROIadded)
    cv2.moveWindow('ROIadded', 1200, 0)

    frameOriginal[y:y+dy, x:x+dx] = ROIadded
    cv2.imshow('frameOriginal', frameOriginal)
    cv2.moveWindow('frameOriginal', 0, 520)

    x = x + dirX
    y = y + dirY

    if x <=0 or  x+dx >= dispW :
        dirX = dirX * (-1)

    if y <=0 or  y+dy >= dispH :
        dirY = dirY * (-1)


    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()