import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_size = (480, 640, 3)
vdo_writer = cv2.VideoWriter('out.mp4', fourcc, 30, (frame_size[1], frame_size[0]))

for i in range(640):
    frame = np.zeros(frame_size, np.uint8)
    cv2.circle(frame, (i, 200), 20, (255,255,255), -1)
    vdo_writer.write(frame)

    # cv2.imshow('frame', frame)
    # cv2.waitKey(1)
vdo_writer.release()