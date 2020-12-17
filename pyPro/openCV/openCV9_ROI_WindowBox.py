import cv2
import numpy as np
print(cv2.__version__)

evtDown = -1
evtUp = -1
evtMoving = -1
drawRect = -1
xRoiLeftTop = 0
yRoiLeftTop = 0
xRoiBotRht = 1
yRoiBotRht = 1
copyFrame = -1

xPosBotRht = 0
yPosBotRht = 0


def click(event, x, y, flags, params):
    global xPosTopLeft
    global yPosTopLeft
    global evtDown
    global xPosBotRht
    global yPosBotRht
    global evtUp
    global xPosMoving
    global yPosMoving
    global evtMoving

    if(event == 0):
        xPosMoving = x
        yPosMoving = y
        evtMoving = event
        # print("Moving X, Y, EVENT: ", x, y, event)

    if(event == cv2.EVENT_LBUTTONDOWN):
        # print("Down X, Y, EVENT: ", x, y, event)
        xPosTopLeft = x
        yPosTopLeft = y
        evtDown = event

    if(event == cv2.EVENT_LBUTTONUP):
        # print("UP : X, Y, EVENT: ", x, y, event)
        xPosBotRht = x
        yPosBotRht = y
        evtUp = event


# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)
cv2.namedWindow("Original")
cv2.setMouseCallback("Original", click)
roi = np.zeros((1, 1, 3), np.uint8)

while True:
    ret, frameOriginal = cam.read()

    if evtDown == 1:
        xPosBotRht = xPosTopLeft
        yPosBotRht = yPosTopLeft
        evtUp = -1
        drawRect = 0
        cv2.rectangle(frameOriginal, (xPosTopLeft, yPosTopLeft), (xPosBotRht, yPosBotRht), (0, 0, 255), 2)

    if drawRect == 0 and evtMoving == 0:
        evtDown = -1
        cv2.rectangle(frameOriginal, (xPosTopLeft, yPosTopLeft), (xPosMoving, yPosMoving), (0, 0, 255), 2)

    if drawRect == 0 and evtUp == 4:
        evtDown = -1
        drawRect = -1
        xRoiBotRht = xPosBotRht
        yRoiBotRht = yPosBotRht
        xRoiLeftTop = xPosTopLeft
        yRoiLeftTop = yPosTopLeft
        cv2.rectangle(frameOriginal, (xPosTopLeft, yPosTopLeft), (xPosBotRht, yPosBotRht), (0, 0, 255), 2)
        copyFrame = 0
        # roi = np.zeros((1, 1, 3), np.uint8)
        roi = frameOriginal[yRoiLeftTop:yRoiBotRht, xRoiLeftTop:xRoiBotRht].copy()
        print(yRoiLeftTop,yRoiBotRht,xRoiLeftTop,xRoiBotRht)   
     
    cv2.imshow('Original', frameOriginal)
    cv2.imshow('ROI', roi)

    cv2.moveWindow('Original', 0, 0)
    cv2.moveWindow('ROI', 640, 0)

    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()