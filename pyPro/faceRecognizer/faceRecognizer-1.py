import face_recognition
import cv2

print (cv2.__version__)

image = face_recognition.load_image_file('/home/suresh/Desktop/AI_on_the_Jetson_Nano/pyPro/faceRecognizer/demoImages/unknown/u3.jpg')
face_locations = face_recognition.face_locations(image)
print (face_locations)
imageBGR = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow('myWindow', imageBGR)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()