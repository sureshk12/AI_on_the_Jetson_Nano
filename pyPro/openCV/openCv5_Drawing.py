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
    frameOriginal = cv2.rectangle(frameOriginal, (270, 190), (370, 290), (0, 255, 0), 2)
    frameOriginal = cv2.circle(frameOriginal,(320, 240), 25, (255, 0, 0), -1)
    frameOriginal = cv2.putText(frameOriginal, "Hello World",(279,330), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
    frameOriginal = cv2.line(frameOriginal, (270, 190), (370, 290), (255,255,0), 3)
    frameOriginal = cv2.arrowedLine(frameOriginal, (270, 290), (370, 190), (0, 0, 255), 2)

    cv2.imshow('Original', frameOriginal)
    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()