import cv2
import numpy as np

# fn = 'vdo.mp4'
fn = 'cctv.mp4'
cap = cv2.VideoCapture(fn)
tracker = cv2.TrackerGOTURN_create()
# tracker = cv2.TrackerMIL_create()

boxes = []
selecting = False
current_mouse_position = np.ones(2, dtype=np.int32)
def on_mouse(event, x, y, flags, params):
    global boxes, selecting, frame, obj, tracker
    current_mouse_position[0] = x
    current_mouse_position[1] = y
    if event == cv2.EVENT_LBUTTONDOWN:
        boxes = [[x, y]]
        selecting = True
    elif event == cv2.EVENT_LBUTTONUP:
        selecting = False
        boxes.append([x, y])
        obj = frame[boxes[0][1]+2:boxes[1][1]-2,boxes[0][0]+2:boxes[1][0]-2,:]
        tracker.init(frame, (boxes[0][0], boxes[0][1], boxes[1][0]-boxes[0][0], boxes[1][1]-boxes[0][1]))
        cv2.imshow('obj', obj)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', on_mouse)
obj = None
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if obj is not None:  # init tracker
        # update tracker
        isTracked, obj = tracker.update(frame)
        if isTracked:
            xy1 = (int(obj[0]), int(obj[1]))
            xy2 = (int(obj[0]+obj[2]), int(obj[1]+obj[3]))
            cv2.rectangle(frame, xy1, xy2, (0, 0, 255), 2)
    if selecting:
        top_left = (boxes[0][0], boxes[0][1])
        bottom_right = (current_mouse_position[0], current_mouse_position[1])
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.waitKey(30)