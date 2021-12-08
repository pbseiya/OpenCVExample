import cv2
import numpy as np

img1 = cv2.imread("ARmarker.png", cv2.IMREAD_GRAYSCALE)
ft = cv2.SIFT_create()
kp1, des1 = ft.detectAndCompute(img1, None)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# FLANN parameters
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

while True:
    ret, img2 = cap.read()
    kp2, des2 = ft.detectAndCompute(img2, None)
    matches = flann.knnMatch(des1.astype(np.float32), des2.astype(np.float32), k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.6*n.distance:
            good.append(m)
    matching_result = cv2.drawMatches(img1, kp1, img2, kp2, good[:50], None, flags=2)
    cv2.imshow("Matching result", matching_result)
    cv2.waitKey(1)
