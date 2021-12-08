import cv2
import numpy as np

cap = cv2.VideoCapture('cctv.mp4')
n_buffer = 10
buffer = None
iframe = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if buffer is None:
        buffer = np.zeros((n_buffer, *gray.shape))
    buffer[iframe % n_buffer] = gray
    if iframe >= n_buffer:
        # M = np.mean(buffer, axis=0)
        M = np.median(buffer, axis=0)
        diff = cv2.absdiff(gray, np.uint8(M))
        fg = np.uint8((diff > .4 * np.max(diff)) * 255)
        cv2.imshow('fg', fg)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    iframe += 1
