import cv2

print(cv2.__version__)

cv2.namedWindow('BlendedImage')

def dummyCallback(x):
    pass

# ***Rapberry Pi Camera setting***
dispW = 640
dispH = 480
flip = 2
# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

cam = cv2.VideoCapture(0)

cvImg = cv2.imread('cv.jpg')
cvImg = cv2.resize(cvImg, (320, 240))
cvImgGray = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
cv2.imshow('CVImgGray', cvImgGray)
cv2.moveWindow('CVImgGray', 0, 300)

_,bgMask = cv2.threshold(cvImgGray, 225, 255, cv2.THRESH_BINARY)
cv2.imshow('BGMask', bgMask)
cv2.moveWindow('BGMask', 385, 0)

fgMask = cv2.bitwise_not(bgMask)
cv2.imshow('FGMask', fgMask)
cv2.moveWindow('FGMask', 385, 300)

fgImg = cv2.bitwise_and(cvImg, cvImg, mask=fgMask)
cv2.imshow('FGImage', fgImg)
cv2.moveWindow('FGImage', 700, 300)

cv2.createTrackbar('BlendingValue','BlendedImage', 40, 100, dummyCallback )

while True:
    ret, frameOriginal = cam.read()
    frameOriginal = cv2.resize(frameOriginal, (320, 240))

    bgImg = cv2.bitwise_and(frameOriginal, frameOriginal, mask=bgMask)
    


    cv2.imshow('Original', frameOriginal)
    cv2.moveWindow('Original', 0, 0)

    cv2.imshow("BGImage", bgImg)
    cv2.moveWindow('BGImage', 700, 0)

    blendingValue = cv2.getTrackbarPos('BlendingValue','BlendedImage') / 100
    blendedImg = cv2.addWeighted(frameOriginal, (1 - blendingValue), cvImg, blendingValue, 0)
    cv2.imshow("BlendedImage", blendedImg)
    cv2.moveWindow('BlendedImage', 1020, 300)

    blendedMaskImg = cv2.bitwise_and(blendedImg, blendedImg, mask=fgMask)
    cv2.imshow("BlendedMaskImage", blendedMaskImg)
    cv2.moveWindow('BlendedMaskImage', 1340, 300)    

    finalImg = cv2.add(bgImg, fgImg)
    cv2.imshow("FinalImageBeforeBlending", finalImg)
    cv2.moveWindow('FinalImageBeforeBlending', 1020, 0)

    finalBlendedImg = cv2.add(bgImg, blendedMaskImg)
    cv2.imshow("FinalImageAfterBlending", finalBlendedImg)
    cv2.moveWindow('FinalImageAfterBlending', 1340, 0)

    keyPressed = cv2.waitKey(33)
    if keyPressed == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
