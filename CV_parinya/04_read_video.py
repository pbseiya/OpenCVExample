import cv2

cap = cv2.VideoCapture('cctv.mp4')
# cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # cv2.imshow('frame', frame)
        cv2.imshow('frame', frame[:,:,:])
    if cv2.waitKey(1) == ord('q') or not ret:
        break
cap.release()
cv2.destroyAllWindows()
