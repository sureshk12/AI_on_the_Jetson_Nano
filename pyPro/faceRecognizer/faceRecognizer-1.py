import face_recognition
import cv2

print (cv2.__version__)

image = face_recognition.load_image_file('/home/suresh/Desktop/AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/known/Bill Barr.jpg')
print(image.shape)
face_locations = face_recognition.face_locations(image)
print (face_locations)
imageBGR = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
for row2, col2, row1, col1 in face_locations :
    cv2.rectangle(imageBGR,(col1, row1), (col2, row2), (0, 255, 0), 2)

cv2.imshow('myWindow', imageBGR)
cv2.moveWindow("myWindow", 0, 0)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()