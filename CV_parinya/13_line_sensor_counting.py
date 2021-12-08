import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
L1, L2, L3, L4 = np.r_[100:120], np.r_[540:560], np.r_[0:20], np.r_[620:640]
line1, line2, line3, line4 = False, False, False, False
bgsub = cv2.createBackgroundSubtractorKNN(history=1)
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fg = bgsub.apply(gray)
    if np.sum(fg[:, L1]) > 100:
        frame[:, L1, :2] = 0
        line1 = True
    else:
        frame[:, L1, 1:] = 0
    if np.sum(fg[:, L2]) > 100:
        frame[:, L2, :2] = 0
        line2 = True
    else:
        frame[:, L2, 1:] = 0
    if np.sum(fg[:, L3]) > 100 or np.sum(fg[:, L4]) > 100 :
        line1, line2 = False, False
    if line2 and line1:
        line1, line2 = False, False
        count += 1

    cv2.putText(frame, str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('fg', fg)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
