import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)


orb = cv.ORB_create(nfeatures=500)
kp = orb.detect(gray, None)
kp, des = orb.compute(gray, kp)
img = cv.drawKeypoints(gray, kp, None, color=(0, 255, 0), flags=0)
cv.imwrite('orb_keypoints.jpg', img)


# Parametre at lege med:
# 
# nfeatures: Antallet af nøglepunkter.
# scaleFactor: Skalafaktoren mellem niveauer i pyramiden.
# nlevels: Antal niveauer i pyramiden.
