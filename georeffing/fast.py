import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

fast = cv.FastFeatureDetector_create()
kp = fast.detect(gray, None)
img = cv.drawKeypoints(gray, kp, None, color=(255, 0, 0))
cv.imwrite('fast_keypoints.jpg', img)


# FAST er en algoritme til hurtig nøglepunktdetektering. Den bruges ofte som en del af andre algoritmer, som ORB.
# Parametre at lege med:
# 
# threshold: Grænseværdi for detektion.
# nonmaxSuppression: Aktivér/Deaktivér undertrykkelse af ikke-maksimal værdier.
# type: Type af FAST (Original, 5-8-12-16).
