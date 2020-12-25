import cv2
import numpy as np 
print(cv2.__version__)

# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0, 0)

    #split picture into 3 colours
    # b = cv2.split(frame)[0]
    # g = cv2.split(frame)[1]
    # r = cv2.split(frame)[2]
    b, g, r = cv2.split(frame)

    bn = frame
    bn[:,:,[1]] = 0
    bn[:,:,[2]] = 0
    blank = np.zeros((480, 640), np.uint8)
    blue  = cv2.merge((b, blank, blank))
    green  = cv2.merge((blank, g, blank))
    red  = cv2.merge((blank, blank, r))

    #you can also increase the colour 
    # b[:] = b[:] * 1.2


    cv2.imshow('Blue', bn)
    cv2.moveWindow('Blue', 0, 515)
    
    cv2.imshow('Green', green)
    cv2.moveWindow('Green', 650, 0)

    cv2.imshow('Red', red)
    cv2.moveWindow('Red', 650, 515)


    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()