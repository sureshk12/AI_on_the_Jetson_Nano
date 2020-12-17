import cv2
print(cv2.__version__)

def noActionFunction(x):
    pass


# ***Rapberry Pi Camera setting***
# dispW = 640
# dispH = 480
# flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)
cv2.namedWindow('Original')
cv2.createTrackbar('xVal', 'Original', 100, 640, noActionFunction )
cv2.createTrackbar('yVal', 'Original', 100, 640, noActionFunction )
cv2.createTrackbar('wVal', 'Original', 100, 640, noActionFunction )
cv2.createTrackbar('hVal', 'Original', 100, 640, noActionFunction )

while True:
    ret, frameOriginal = cam.read()
    xVal = cv2.getTrackbarPos('xVal', 'Original')
    yVal = cv2.getTrackbarPos('yVal', 'Original')
    wVal = cv2.getTrackbarPos('wVal', 'Original')
    hVal = cv2.getTrackbarPos('hVal', 'Original')

    cv2.rectangle(frameOriginal, (xVal, yVal), (xVal+wVal, yVal+hVal), (255, 0, 0), 2)

    cv2.imshow('Original', frameOriginal)
    cv2.moveWindow('Original', 0, 0)
    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()