import face_recognition
import cv2
import os

print (cv2.__version__)

imageDir = '/home/suresh/Desktop/AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/known'
for root, dirs, files in os.walk(imageDir):

    for file in files:
        #Preapare the names from each file and append to Names array
        name = str.split(file, '.')[0]
        print("Resizing :", name)
        #Prepare the encodings for each file and append to Encodings array
        path = os.path.join(root, file)
        # print (path)
        face = face_recognition.load_image_file(path)
        face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
        newFile = cv2.resize(face, (640, 480))
        cv2.imwrite(('/home/suresh/Desktop/AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/knownNew/' + name +'.jpg'), newFile)

