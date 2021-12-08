import cv2

cap = cv2.VideoCapture('cctv.mp4')
bgsubknn = cv2.createBackgroundSubtractorKNN()
bgsubmog = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    fgknn = bgsubknn.apply(frame)
    fgmog = bgsubmog.apply(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('fgknn', fgknn)
    cv2.imshow('fgmog', fgmog)
    cv2.waitKey(1)
