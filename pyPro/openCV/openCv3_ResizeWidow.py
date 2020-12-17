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
    
    gray = cv2.cvtColor(frameOriginal, cv2.COLOR_BGR2GRAY)
    originalSmall = cv2.resize(frameOriginal, (320, 240))
    graySamll = cv2.resize(gray, (320, 240))

    cv2.moveWindow('Original', 650,0)
    cv2.moveWindow('Original Small', 0, 0)
    cv2.moveWindow('Gray Small', 0,240)

    cv2.imshow('Original', frameOriginal)
    cv2.imshow('Original Small', originalSmall)
    cv2.imshow('Gray Small', graySamll)

    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()