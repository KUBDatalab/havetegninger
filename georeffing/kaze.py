import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

kaze = cv.KAZE_create()
kp = kaze.detect(gray, None)
kp, des = kaze.compute(gray, kp)
img = cv.drawKeypoints(gray, kp, None, color=(255, 0, 0))
cv.imwrite('kaze_keypoints.jpg', img)

# Parametre at lege med:
# 
# threshold: Grænse for nøglepunktdetektering.
# nOctaves: Antal oktaver.
# nOctaveLayers: Antal lag i hver oktav.
# 
# KAZE er en algoritme, der er designet til at detektere nøglepunkter i et ikke-lineært skalarum, hvilket gør den robust mod støj.
