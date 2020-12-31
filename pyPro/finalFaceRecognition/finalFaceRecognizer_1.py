import face_recognition
import cv2
import pickle
import time
import numpy as np

print (cv2.__version__)

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=15/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink max-buffers=1 drop=true'
cam = cv2.VideoCapture(camSet)

# cam = cv2.VideoCapture(0)q

Encodings = []
Names = []
print ('Reading Trained Data')

with open ('train.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

print ('Loaded all the Trained Data')

font = cv2.FONT_ITALIC
ratio = 0.3

while True:

    ret, frame = cam.read()
    startTime = time.perf_counter()
    frame = cv2.flip(frame, 1)
    frame = frame[:,125:515]
    # print ('Frame Read : {}'.format(time.perf_counter() - startTime))

    frameSmall = cv2.resize(frame,(0, 0), fx = ratio, fy = ratio)
    frameRGB = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2RGB)

    faceLocations = face_recognition.face_locations(frameRGB)
    # print ('detect Locations : {}'.format(time.perf_counter() - startTime))
    if len(faceLocations) > 0:
        tempLocation = faceLocations[0]
        top, right, bottom, left = tempLocation[0], tempLocation[1], tempLocation[2], tempLocation[3]
        if (right - left) > int(90 * ratio ) and (bottom - top) > int(120 * ratio ):
            cv2.imshow('myWindow', frame)
            cv2.moveWindow("myWindow", 0, 0)
            totalTry = 0
            foundName = []
            while totalTry < 8:
                allUnknownEncoding = face_recognition.face_encodings(frameRGB, faceLocations)
                # print ('detect encodings : {}'.format(time.perf_counter() - startTime))
                for (top, right, bottom, left), face_encoding in zip (faceLocations, allUnknownEncoding) :
                    name = 'Unknown Person'

                    matches = face_recognition.compare_faces(Encodings, face_encoding)

                    # # If a match was found in known_faqce_encodings, just use the first one.
                    # if True in matches :
                    # first_match_index = matches.index(True)q
                    # name = Names[first_match_index]

                    ## Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(Encodings, face_encoding)
                    # print(face_distances)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = Names[best_match_index]
                        foundName.append(name)
                totalTry = totalTry + 1

            setFoundName = set(foundName)
            print(len(setFoundName), name)
            
            if len(setFoundName) == 1:
                name = name
            else:
                name = 'Unknown person'

            top = int(top/ratio)
            right = int (right/ratio)
            bottom = int(bottom/ratio)
            left = int(left/ratio)

            # print(top, right, bottom, left)        
            # cv2.rectangle(frame, (left, top), (right, bottom),(255, 255, 225), 2 )
            # cv2.putText(frame, name, (left, top-7), font, 0.8, (0, 255, 0), 2)
            (text_width, text_height) = cv2.getTextSize(name, font, 1,1)[0]
            # print (text_width, text_height)
            cv2.rectangle(frame, (10, 50), (10+20+text_width, 50-20-text_height), (0, 0, 0), -1)
            cv2.putText(frame, name, (20, 40), font, 1, (0, 255, 0), 2)
        else:
            top = int(top/ratio)
            right = int (right/ratio)
            bottom = int(bottom/ratio)
            left = int(left/ratio)
            # cv2.rectangle(frame, (left, top), (right, bottom),(255, 0, 0), 2 )
            cv2.rectangle(frame, (10, 480), (340, 440), (0, 0, 0), -1)
            cv2.putText(frame, 'Please come closer', (20, 470), font, 1, (0, 0, 255), 2 )


    dt = time.perf_counter() - startTime
    dtav = dt * 0.9 + dt * 0.1
    fps = round((1/dtav), 2)
    # print(dtav, fps)
    sizeString = cv2.getTextSize(str(fps),font, 0.75, 2)[0]
    cv2.rectangle(frame, (40, 10), (40+sizeString[0], 10+sizeString[1]), (0, 0, 0), -1)
    cv2.putText(frame, str(fps), (40, 30), font, 0.75,(0, 255, 255), 2)

    # cv2.rectangle(frame, (185, 60), (455, 420),(0, 255, 225), 2 )
    cv2.imshow('myWindow', frame)
    cv2.moveWindow("myWindow", 0, 0)


    keyEntered = cv2.waitKey(1)
    if keyEntered == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

