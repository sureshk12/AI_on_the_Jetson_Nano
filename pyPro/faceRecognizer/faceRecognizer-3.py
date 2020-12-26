import face_recognition
import cv2
import os

print (cv2.__version__)

Encodings = []
Names = []

imageDir = '/home/suresh/Desktop/AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/knownNew'
for root, dirs, files in os.walk(imageDir):
    # print(root)
    # print (dirs)
    # print (files)    

    for file in files:
        #Preapare the names from each file and append to Names array
        name = str.split(file, '.')[0]
        Names.append(name)
        print("Encoding :", name)
        #Prepare the encodings for each file and append to Encodings array
        path = os.path.join(root, file)
        # print (path)
        face = face_recognition.load_image_file(path)
        faceLocation = face_recognition.face_locations(face)
        faceEncoding = face_recognition.face_encodings(face, faceLocation)[0]
        Encodings.append(faceEncoding)

# print (Names)

font = cv2.FONT_HERSHEY_SIMPLEX

testImage = face_recognition.load_image_file('/home/suresh/Desktop/AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/unknown/u11.jpg')
faceLocations = face_recognition.face_locations(testImage)
allUnknownEncoding = face_recognition.face_encodings(testImage, faceLocations)

testImageBGR = cv2.cvtColor(testImage, cv2.COLOR_RGB2BGR)

for (top, right, bottom, left), face_encoding in zip (faceLocations, allUnknownEncoding) :
    name = 'Unknow Person'
    matches = face_recognition.compare_faces(Encodings, face_encoding)
    if True in matches :
        first_match_index = matches.index(True)
        name = Names[first_match_index]
        # print(top, right, bottom, left)        

    cv2.rectangle(testImageBGR, (left, top), (right, bottom),(0, 255, 0), 2 )
    cv2.putText(testImageBGR, name, (left, top-7), font, 0.5, (0, 255, 0), 1)

cv2.imshow('myWindow', testImageBGR)
cv2.moveWindow("myWindow", 0, 0)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()