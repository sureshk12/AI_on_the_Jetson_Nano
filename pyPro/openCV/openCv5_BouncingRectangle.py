import cv2
import random

print(cv2.__version__)

# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)

dispW = 640
dispH = 480
boxL = int(0.15*dispW)
boxH = int(0.15*dispH)
boxX = random.randint(0, dispW - boxL)
boxY = random.randint(0, dispH - boxH)
boxXD = random.randint(0, 1)
boxYD = random.randint(0, 1)
varX = random.randint(6, 12)
varY = random.randint(5, 9)

while True:
    ret, frameOriginal = cam.read()
    if(boxXD == 0):
        boxX = boxX + varX
        if boxX >= 640 - boxL:
            boxX = 640 - boxL
            boxXD = 1
            varX = random.randint(6, 12)
    else:
        boxX = boxX - varX
        if boxX <= 0:
            boxX = 0
            boxXD = 0
            varX = random.randint(6, 12)
            
    if(boxYD == 0):
        boxY = boxY + varY
        if boxY >= 480 - boxH:
            boxY = 480 - boxH
            boxYD = 1
            random.randint(5, 9)
    else:
        boxY = boxY - varY
        if boxY <= 0:
            boxY = 0
            boxYD = 0
            random.randint(5, 9)

    frameOriginal = cv2.rectangle(frameOriginal, (boxX, boxY), (boxX+boxL, boxY+boxH), (0, 255, 0), -1)

    cv2.imshow('Original', frameOriginal)
    keyPressed = cv2.waitKey(100)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()