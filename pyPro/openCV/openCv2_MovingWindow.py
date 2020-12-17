import cv2
print(cv2.__version__)

# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)

while True:
    ret, frameOriginal = cam.read()
    frameGray = cv2.cvtColor(frameOriginal, cv2.COLOR_BGR2GRAY)   

    cv2.imshow('Original', frameOriginal)
    cv2.moveWindow('Original', 0, 0)
    cv2.imshow('Original2', frameOriginal)
    cv2.moveWindow('Original2',640, 0)
    cv2.imshow('Gray', frameGray)
    cv2.moveWindow('Gray', 0, 480)
    cv2.imshow('Gray2', frameGray)
    cv2.moveWindow('Gray2', 640, 480)

    keyPressed = cv2.waitKey(33)
    #print(keyPressed)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()