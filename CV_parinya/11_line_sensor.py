import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
L1 = np.r_[100:120]
bgsub = cv2.createBackgroundSubtractorKNN()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame[:, L1, :], cv2.COLOR_BGR2GRAY)
    fg = bgsub.apply(gray)
    if np.sum(fg) > 100:
        frame[:, L1, :2] = 0
    else:
        frame[:, L1, 1:] = 0
    cv2.imshow('fg', fg)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
