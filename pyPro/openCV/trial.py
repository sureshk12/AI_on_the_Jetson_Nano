import cv2
import numpy as np 

wind = np.zeros((480, 680, 3), np.uint8)
wind = cv2.rectangle(wind, (100,100), (440, 280), (0, 0, 255), -1)
cv2.imshow('Window', wind)

wind = cv2.rectangle(wind, (100,100), (440, 280), (0, 0, 255), -1)
while True:
    keyInput = cv2.waitKey(50)
    if keyInput == ord('q'):
        break