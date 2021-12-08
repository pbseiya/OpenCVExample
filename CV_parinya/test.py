import cv2
import numpy as np
import matplotlib.pyplot as plt

A = cv2.imread('challenge_3.jpg')
plt.imshow(A[:,:,::-1])
plt.show()

tol = 30
color = np.array([0,0, 255])

mask = cv2.inRange(A, color-tol, color+tol)
Amask = cv2.bitwise_and(A, A, mask=mask)
cv2.imshow('mask', mask)
cv2.imshow('Amask', Amask)
cv2.waitKey()
cv2.imwrite('mask.png', mask)
cv2.imwrite('Amask.png', Amask)