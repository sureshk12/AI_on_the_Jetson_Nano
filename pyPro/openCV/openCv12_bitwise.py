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

img1 = np.zeros((480, 640, 3), np.uint8)
img1 [0:480, 0:320] = [0,0,255]
img2 = np.zeros((480, 640, 3), np.uint8)
img2 [190:290, 270:370] = [0,255,0]
img1And2 = cv2.bitwise_and(img1, img2)
img1Or2 = cv2.bitwise_or(img1, img2)
img1Xor2 = cv2.bitwise_xor(img1, img2)

while True:
    ret, frameOriginal = cam.read()
    # frameOriginal = cv2.bitwise_and(frameOriginal, frameOriginal, mask=img1Xor2)


    cv2.imshow('Original', frameOriginal)
    cv2.moveWindow('Original', 0, 0)
 
    cv2.imshow('Img1', img1)
    cv2.moveWindow('Img1',0, 520)

    cv2.imshow('Img2', img2)
    cv2.moveWindow('Img2',640, 0)

    cv2.imshow('Img1And2', img1And2)
    cv2.moveWindow('Img1And2',640, 520)

    cv2.imshow('Img1Or2', img1Or2)
    cv2.moveWindow('Img1Or2',1280, 0)

    cv2.imshow('Img1Xor2', img1Xor2)
    cv2.moveWindow('Img1Xor2',1280, 520)
    
    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()