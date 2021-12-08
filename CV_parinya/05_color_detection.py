import cv2
import numpy as np
import matplotlib.pyplot as plt

A = cv2.imread('parrot.jpg')
plt.imshow(A[:,:,::-1])
plt.show()

tol = 30
color = np.array([64, 116, 138])

mask = cv2.inRange(A, color-tol, color+tol)
Amask = cv2.bitwise_and(A, A, mask=mask)
cv2.imshow('mask', mask)
cv2.imshow('Amask', Amask)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('mask.png', mask)
# cv2.imwrite('Amask.png', Amask)