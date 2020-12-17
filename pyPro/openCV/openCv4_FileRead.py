import cv2
print(cv2.__version__)

# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture('Videos/trialVideo.avi')

while True:
    ret, frameOriginal = cam.read()
    if(ret):
        cv2.imshow('Original frame', frameOriginal)
        keyPressed = cv2.waitKey(33)
        if keyPressed == ord('q'):
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cam.release()
cv2.destroyAllWindows()