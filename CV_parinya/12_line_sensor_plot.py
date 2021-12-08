import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
L1 = np.r_[100:120]
bgsub = cv2.createBackgroundSubtractorKNN()

iframe = 0

# For ploting
monitor_frames = 500
line1 = np.zeros(monitor_frames)
fig = plt.figure()
ax = fig.gca()
graph1 = ax.plot(np.arange(monitor_frames), np.zeros((monitor_frames,)), c='r')[0]
ax.set_xlim(0, monitor_frames)
ax.set_ylim(0, 480*len(L1))
ax.set_xlabel('$n^{th}$ frame')
ax.set_ylabel('Sum of fg')
background = fig.canvas.copy_from_bbox(ax.bbox)
plt.ion()
plt.show()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame[:, L1, :], cv2.COLOR_BGR2GRAY)
    fg = bgsub.apply(gray)

    if iframe > 0:
        line1[:-1] = line1[1:]
        line1[-1] = np.sum(fg/255)
        ax.set_xlim(iframe, iframe+monitor_frames)
        graph1.set_xdata(np.arange(iframe, iframe+monitor_frames))
        graph1.set_ydata(line1)
        fig.canvas.restore_region(background)
        ax.draw_artist(graph1)
        fig.canvas.blit(ax.bbox)

    if np.sum(fg) > 100:
        frame[:, L1, :2] = 0
    else:
        frame[:, L1, 1:] = 0
    cv2.imshow('fg', fg)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    iframe += 1
