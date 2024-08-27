import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

akaze = cv.AKAZE_create()
kp = akaze.detect(gray, None)
kp, des = akaze.compute(gray, kp)
img = cv.drawKeypoints(gray, kp, None, color=(0, 255, 0), flags=0)
cv.imwrite('akaze_keypoints.jpg', img)


# Parametre at lege med:
# 
# threshold: Grænse for nøglepunktdetektering.
# nOctaves: Antal oktaver til detektering.
# nOctaveLayers: Antal lag per oktav.

# AKAZE er en variant af KAZE-algoritmen, men hurtigere. Den bruges til at finde 
# nøglepunkter og beskrivelser i billeder, og den er også robust over for skala og rotation.
