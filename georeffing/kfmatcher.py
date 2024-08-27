import cv2 as cv

# Læs to billeder
img1 = cv.imread('image1.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('image2.jpg', cv.IMREAD_GRAYSCALE)

# Opret ORB-detektor
orb = cv.ORB_create()

# Detekter nøglepunkter og beregn deskriptorer
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Opret BFMatcher-objekt
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match deskriptorer
matches = bf.match(des1, des2)

# Sorter matcher efter deres distance
matches = sorted(matches, key=lambda x: x.distance)

# Tegn de første 10 matcher
img_matches = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Gem eller vis billedet med de matchede nøglepunkter
cv.imwrite('orb_matches.jpg', img_matches)
