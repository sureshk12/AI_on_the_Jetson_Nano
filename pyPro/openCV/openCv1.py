import cv2

print(cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 1920
dispH = 1080
flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12, framerate=30/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink max-buffers=1 drop=true'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frameNew = frame[:, 0:390]
    

    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0, 0)
    keyPressed = cv2.waitKey(1)
    if keyPressed == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

