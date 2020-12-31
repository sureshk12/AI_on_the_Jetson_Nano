import cv2
import random

print(cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

# cam = cv2.VideoCapture(0)
rectW = 160
rectH = 120
posX = random.randint(0, dispW - rectW)
posY = random.randint(0, dispH - rectH)
dirX = random.randint(0, 1)
dirY = random.randint(0, 1)
stepX = random.randint(3, 12)
stepY = random.randint(3, 9)

while True:
    if dirX == 0:
        posX = posX + stepX
    else:
        posX = posX - stepX
    
    if dirY == 0:
        posY = posY + stepY
    else:
        posY = posY - stepY

    if posX <= 0:
        posX = 0
        if dirX == 0:
            dirX = 1
        else:
            dirX = 0
        stepX = random.randint(1, 4)

    if posX >= dispW - rectW:
        posX = dispW -rectW
        if dirX == 0:
            dirX = 1
        else:
            dirX = 0
        stepX = random.randint(1, 4)


    if posY <= 0:
        posY = 0
        if dirY == 0:
            dirY = 1
        else:
            dirY = 0
        stepY = random.randint(1, 3)

    if posY >= dispH - rectH:
        posY = dispH - rectH
        if dirY == 0:
            dirY = 1
        else:
            dirY = 0
        stepY = random.randint(1, 3)

    ret, frameOriginal = cam.read()
    frameOriginalGray = cv2.cvtColor(frameOriginal, cv2.COLOR_BGR2GRAY).copy()
    frameOriginalGrayProper = cv2.cvtColor(frameOriginalGray, cv2.COLOR_GRAY2BGR)
    roi = frameOriginal[posY : posY + rectH, posX :posX + rectW].copy()
    roiGray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roiGrayShape = cv2.cvtColor(roiGray, cv2.COLOR_GRAY2BGR)
    # frameOriginal[posY : posY + rectH, posX :posX + rectW] = roiGrayShape
    frameOriginalGrayProper[posY : posY + rectH, posX :posX + rectW] = roi

    cv2.rectangle(frameOriginalGrayProper, (posX, posY), (posX + rectW, posY + rectH), (0, 0, 255), 2 )

    # cv2.imshow('Original', frameOriginal)
    cv2.imshow('Original Gray proper', frameOriginalGrayProper)
    cv2.imshow('Roi', roi)
    cv2.imshow('Roi Gray', roiGray)

    cv2.moveWindow('Original Gray proper', 0, 0)
    cv2.moveWindow('Roi', dispW, 0)
    cv2.moveWindow('Roi Gray', dispW, rectH)

    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

