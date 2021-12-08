import cv2
import numpy as np

img1 = cv2.imread("ARmarker.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("Doraemon.jpg")
img3 = cv2.resize(img3, img1.shape)
blank = np.ones(img1.shape, np.uint8)
rows, cols = img1.shape

cap = cv2.VideoCapture(0)

# Detector
ft = cv2.SIFT_create()
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)  # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params, search_params)

kp1, des1 = ft.detectAndCompute(img1, None)
while True:
    _, frame = cap.read()
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp2, des2 = ft.detectAndCompute(img2, None)
    matches = flann.knnMatch(des1.astype(np.float32), des2.astype(np.float32), k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good.append(m)
    cv2.imshow("frame", frame)
    if len(good) >= 4:
        matching_result = cv2.drawMatches(img1, kp1, img2, kp2, good[:50], None, flags=2)
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        if M is not None:
            mask = cv2.warpPerspective(blank, M, (frame.shape[1], frame.shape[0]))
            mask = ((mask > 0) * 255).astype(np.uint8)
            mask_inv = cv2.bitwise_not(mask)
            bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
            obj = cv2.warpPerspective(img3, M, (frame.shape[1], frame.shape[0]))
            fg = cv2.bitwise_and(obj, obj, None, mask=mask)
            frame = cv2.add(fg, bg)
            #cv2.imshow("fg", fg)
    cv2.imshow("AR", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
