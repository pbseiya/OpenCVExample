import cv2
import numpy as np

cap = cv2.VideoCapture('cctv.mp4')
buffer = None
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if buffer is not None:
        diff = np.mean(cv2.absdiff(frame, buffer), axis=2)
        fg = np.uint8((diff > 0.5*np.max(diff)) * 255)
        cv2.imshow('diff', np.uint8(diff / np.max(diff) * 255))
        cv2.imshow('fg', fg)
    buffer = frame
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
