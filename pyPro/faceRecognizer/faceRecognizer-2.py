import face_recognition
import cv2

print (cv2.__version__)

# dirPath = '/home/suresh/Desktop/'
dirPath = 'D:/Python/'

donFace = face_recognition.load_image_file(dirPath + 'AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/known/Donald Trump.jpg')
donFaceEncoding = face_recognition.face_encodings(donFace)[0]

nancyFace = face_recognition.load_image_file(dirPath + 'AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/known/Nancy Pelosi.jpg')
nancyEncoding = face_recognition.face_encodings(nancyFace)[0]

penceFace = face_recognition.load_image_file(dirPath + 'AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/known/Mike Pence.jpg')
penceEncoding = face_recognition.face_encodings(penceFace)[0]

Encoding = [donFaceEncoding, nancyEncoding, penceEncoding]
Names = ['Donald Trup','Nancy Pelosi', 'Mike Pence' ]

font = cv2.FONT_HERSHEY_SIMPLEX

testImage = face_recognition.load_image_file(dirPath + 'AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/unknown/u11.jpg')
faceLocations = face_recognition.face_locations(testImage)
allUnknownEncoding = face_recognition.face_encodings(testImage, faceLocations)

testImageBGR = cv2.cvtColor(testImage, cv2.COLOR_RGB2BGR)

for (top, right, bottom, left), face_encoding in zip (faceLocations, allUnknownEncoding) :
    name = 'Unknow Person'
    matches = face_recognition.compare_faces(Encoding, face_encoding)
    if True in matches :
        first_match_index = matches.index(True)
        name = Names[first_match_index]
        print(top, right, bottom, left)
        

    cv2.rectangle(testImageBGR, (left, top), (right, bottom),(0, 255, 0), 2 )
    # cv2.circle(testImageBGR, (left, top), 5, (0, 0, 255), -1)
    # cv2.circle(testImageBGR, (right, bottom), 5, (255, 0, 255), -1)
    cv2.putText(testImageBGR, name, (left, top-7), font, 0.5, (0, 255, 0), 1)

cv2.imshow('myWindow', testImageBGR)
cv2.moveWindow("myWindow", 0, 0)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()