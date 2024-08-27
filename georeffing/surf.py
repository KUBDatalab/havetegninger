import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create(hessianThreshold=400)
kp, des = surf.detectAndCompute(gray, None)
img = cv.drawKeypoints(gray, kp, None, color=(255, 0, 0))
cv.imwrite('surf_keypoints.jpg', img)


# SURF er en forbedret version af SIFT, der er hurtigere og mere robust, men den er ikke fri for patentrettigheder.
# Parametre at lege med:
# 
# hessianThreshold: Grænse for detektion. Jo højere værdi, desto færre nøglepunkter.
# nOctaves: Antal oktaver.
# nOctaveLayers: Antal lag i hver oktav.
