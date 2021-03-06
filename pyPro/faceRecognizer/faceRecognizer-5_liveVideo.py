import face_recognition
import cv2
import os
import pickle

print (cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
<<<<<<< HEAD
camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
=======
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=10/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)
>>>>>>> d9960b64b80f387533524d9f35a6a8809d00fe6d

cam = cv2.VideoCapture(0)

Encodings = []
Names = []
print ('Reading Trained Data')

with open ('train.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

print ('Loaded all the Trained Data')

font = cv2.FONT_HERSHEY_SIMPLEX
<<<<<<< HEAD
ratio = 0.25
=======
ratio = 0.7
>>>>>>> d9960b64b80f387533524d9f35a6a8809d00fe6d

skipFrameCount= 60
skipFrame = 1

dispTop = 0
dispRight = 100
dispBottom = 100
dispLeft = 0
dispName = 'Unknown Person'

while True:

    ret, frame = cam.read()
    if skipFrame == 0:
        frame = cv2.flip(frame, 1)
        frameSmall = cv2.resize(frame,(0, 0), fx = ratio, fy = ratio)
        frameRGB = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2RGB)

        faceLocations = face_recognition.face_locations(frameRGB, model = 'cnn')# model ='cnn'
        allUnknownEncoding = face_recognition.face_encodings(frameRGB, faceLocations)

        for (top, right, bottom, left), face_encoding in zip (faceLocations, allUnknownEncoding) :
<<<<<<< HEAD

            dispName = 'Unknown Person'
=======
            name = 'Unknown Person'
>>>>>>> d9960b64b80f387533524d9f35a6a8809d00fe6d
            matches = face_recognition.compare_faces(Encodings, face_encoding)
            if True in matches :
                first_match_index = matches.index(True)
                name = Names[first_match_index]
                dispName = Names[first_match_index]
                # print(top, right, bottom, left)        
            dispTop = int(top/ratio)
            dispRight = int(right/ratio)
            dispBottom = int(bottom/ratio)
            dispLeft = int(left/ratio)
<<<<<<< HEAD
            cv2.rectangle(frame, (dispLeft, dispTop), (dispRight, dispBottom),(0, 255, 255), 2)
            cv2.putText(frame, dispName, (dispLeft, dispTop-7), font, 0.3, (0, 255, 0), 1)

=======
            cv2.rectangle(frame, (dispLeft, dispTop), (dispRight, dispBottom),(0, 255, 225), 2 )
            cv2.putText(frame, name, (dispLeft, dispTop-7), font, 0.3, (0, 255, 0), 1)
>>>>>>> d9960b64b80f387533524d9f35a6a8809d00fe6d

    else :
        # skipFrame = skipFrame + 1
        if skipFrame > skipFrameCount :
            skipFrame = 0
        
<<<<<<< HEAD
=======

>>>>>>> d9960b64b80f387533524d9f35a6a8809d00fe6d
    # cv2.rectangle(frame, (10,5), (200,30),(0, 0, 0), -1 )
    # cv2.putText(frame, dispName, (10, 20), font, 0.6, (0, 255, 0), 1)

    cv2.imshow('myWindow', frame)
    cv2.moveWindow("myWindow", 0, 0)

    keyEntered = cv2.waitKey(1)
    if keyEntered == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

