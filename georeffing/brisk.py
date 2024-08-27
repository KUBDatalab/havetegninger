import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)


brisk = cv.BRISK_create()
kp = brisk.detect(gray, None)
kp, des = brisk.compute(gray, kp)
img = cv.drawKeypoints(gray, kp, None, color=(0, 255, 0), flags=0)
cv.imwrite('brisk_keypoints.jpg', img)


# Parametre at lege med:
# 
# thresh: Grænse for FAST algoritmen for nøglepunktdetektering.
# octaves: Antallet af oktaver (billedpyramideniveauer).
# patternScale: Skalaen af BRISK's mønster.
