import cv2
import numpy as np 

print(cv2.__version__)

clickArray = []
selColArray = np.zeros((100, 100, 3), np.uint8)

def click(event, x, y, flags, params):
    global xMouse
    global yMouse
    global evtMouse
    global clickArray
    global selColArray

    if event == cv2.EVENT_LBUTTONDOWN :
        xMouse = x
        yMouse = y
        evtMouse = event
        cordMouse = (x, y)
        clickArray.append(cordMouse)

    if event == cv2.EVENT_RBUTTONDOWN :
        b = frame[y, x, 0]
        g = frame[y, x, 1]
        r = frame[y, x, 2]
        seldColor = (b, g, r)
        print("Selected Color is : ", seldColor)
        selColArray[:] = [b, g, r]
        selColArray = cv2.putText(selColArray,str(b)+','+str(g)+','+str(r), (0, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255-int(b),255-int(g),255-int(r)),1)#255-b, 255-g, 255-r

cv2.namedWindow('piCam')
cv2.namedWindow('selectedColor')
cv2.setMouseCallback('piCam', click)
cv2.moveWindow('piCam', 0, 0)
cv2.moveWindow('selectedColor', 750, 0)

# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    for clk in clickArray:
        frame = cv2.circle(frame, clk, 5, (0, 0, 255), -1)
        frame = cv2.putText(frame, str(clk), clk, cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    
    cv2.imshow('piCam', frame)
    cv2.imshow('selectedColor', selColArray)
    keyInput = cv2.waitKey(1)
    if  keyInput == ord('q'):
        break
    if keyInput == ord('c'):
        clickArray = []

cam.release()
cv2.destroyAllWindows()