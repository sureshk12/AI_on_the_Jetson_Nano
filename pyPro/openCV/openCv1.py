import cv2
print(cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
<<<<<<< HEAD
camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
=======
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)
>>>>>>> 509133bad7ee783cc1a7d92c0c85c25d49063f49


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0, 0)
<<<<<<< HEAD
    keyPressed = cv2.waitKey(20)
=======
    keyPressed = cv2.waitKey(5)
>>>>>>> 509133bad7ee783cc1a7d92c0c85c25d49063f49
    if keyPressed == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

