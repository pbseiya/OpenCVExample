import cv2

img1 = cv2.imread("ARmarker.png", cv2.IMREAD_GRAYSCALE)
ft = cv2.SIFT_create()
kp, des = ft.detectAndCompute(img1, None)
img = cv2.drawKeypoints(img1, kp, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('img', img)
cv2.waitKey()
