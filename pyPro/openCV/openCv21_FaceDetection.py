import cv2
print(cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)
face_cascade = cv2.CascadeClassifier('D:\Python\AI_on_the_Jetson_Nano\pyPro\cascade\haarcascade_frontalface_default.xml.xml')
eye_cascade = cv2.CascadeClassifier('D:\Python\AI_on_the_Jetson_Nano\pyPro\cascade\haarcascade_eye.xml')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        ROI = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    # for (x, y, w, h) in eyes:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    

    cv2.imshow('Camera', frame)
    cv2.moveWindow('Camera', 0, 0)
    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()