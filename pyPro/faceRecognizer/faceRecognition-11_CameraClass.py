from threading import Thread
import cv2
import time
import face_recognition
import pickle
import numpy as np

Encodings = []
Names = []
print ('Reading Trained Data')

with open ('train.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

print ('Loaded all the Trained Data')

class camera:
    def __init__(self, src, width, height):
        self.capture = cv2.VideoCapture(src)
        self.width = width
        self.height = height
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            _, self.frame = self.capture.read()
            self.frame = cv2.resize(self.frame, (self.width, self.height))

    def getFrame(self):
        return self.frame

dispW = 640
dispH = 480
flip = 2
cam1 = camera(0, dispW, dispH)
startTime = time.time()
font = cv2.FONT_HERSHEY_SIMPLEX
ratio = 1
cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)

while True:
    try:
        frame1 = cam1.getFrame()
        frame1 = cv2.flip(frame1, 1)
        frame1Small = cv2.resize(frame1,(0, 0), fx = ratio, fy = ratio)
        frame1RGB = cv2.cvtColor(frame1Small, cv2.COLOR_BGR2RGB)

        faceLocations = face_recognition.face_locations(frame1RGB)
        if len(faceLocations) > 0:
            top, right, bottom, left = faceLocations[0][0],faceLocations[0][1], faceLocations[0][2],faceLocations[0][3]
            # print('Top: {}, Right : {}, Bottom : {}, Left :{}'.format(top, right, bottom, left))
            dTop = int(top/ratio)
            dRight = int(right/ratio)
            dBottom = int(bottom/ratio)
            dLeft = int(left/ratio)
            # cv2.rectangle(frame1, (dLeft, dTop), (dRight, dBottom),(0, 255, 0), 2 )
            if (right - left) > int(180 * ratio ) and (bottom - top) > int(240 * ratio ):
                allUnknownEncoding = face_recognition.face_encodings(frame1RGB, faceLocations)
                for (top, right, bottom, left), face_encoding in zip (faceLocations, allUnknownEncoding) :
                    name = 'Unknown Person'
                    matches = face_recognition.compare_faces(Encodings, face_encoding)

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches :
                    # first_match_index = matches.index(True)
                    # name = Names[first_match_index]

                    ## Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(Encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = Names[best_match_index]
       
                    print(name)
                    cv2.rectangle(frame1, (dLeft, dTop), (dRight, dBottom),(0, 255, 0), 5 )
                    # cv2.putText(frame, name, (dLeft, dTop-7), font, 0.8, (0, 255, 0), 2)
                    (text_width, text_height) = cv2.getTextSize(name, font, 1,1)[0]
                    # print (text_width, text_height)
                    cv2.rectangle(frame1, (10, 50), (10+20+text_width, 50-20-text_height), (0, 0, 0), -1)
                    cv2.putText(frame1, name, (20, 40), font, 1, (0, 255, 0), 2)
                    # time.sleep(10)
            else:
                cv2.rectangle(frame1, (dLeft, dTop), (dRight, dBottom),(255, 0, 0), 2 )
                cv2.rectangle(frame1, (10, 480), (340, 440), (0, 0, 0), -1)
                cv2.putText(frame1, 'Please come closer', (20, 470), font, 1, (0, 0, 255), 2 )


        dt = time.time() - startTime
        startTime = time.time()
        dtav = dt * 0.9 + dt * 0.1
        fps = round((1/dtav), 2)
        sizeString = cv2.getTextSize(str(fps),font, 0.75, 2)[0]
        cv2.rectangle(frame1, (600, 10), (600+sizeString[0], 10+sizeString[1]), (0, 0, 0), -1)
        cv2.putText(frame1, str(fps), (600, 30), font, 0.75,(0, 255, 255), 2)

        cv2.imshow('Camera', frame1)
        cv2.moveWindow('Camera', 0, 0)
    except:
        print('Error in the code')

    enteredKey = cv2.waitKey(1)
    if enteredKey == ord('q'):
        cam1.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break



