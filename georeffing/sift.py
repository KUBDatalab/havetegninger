import numpy as np
import cv2 as cv
 
img = cv.imread('home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 

sift = cv.SIFT_create(nfeatures=500, contrastThreshold=0.05, edgeThreshold=10, sigma=1.6)
mask = np.zeros(gray.shape[:2], dtype="uint8")
mask[50:200, 50:200] = 255
kp = sift.detect(gray, None)
img = cv.drawKeypoints(gray, kp, img)
cv.imwrite('sift_keypoints.jpg', img)
