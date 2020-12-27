import face_recognition
import cv2
import os
import pickle

print (cv2.__version__)
dirPath = '/home/suresh/Desktop/'
# dirPath = 'D:/Python/'

Encodings = []
Names = []

imageDir = dirPath + 'AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/known1'
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

with open ('train.pkl', 'wb') as f:
    pickle.dump(Names, f)
    pickle.dump(Encodings, f)

print('Saved all encoding')