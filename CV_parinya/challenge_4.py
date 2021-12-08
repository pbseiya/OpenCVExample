import matplotlib.pyplot as plt
import numpy as np
import cv2

im1 = plt.imread('im1.jpg')
im2 = plt.imread('im2.jpg')

diff = cv2.absdiff(im1,im2)

gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
bw = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)[1]

kernel = np.ones((5,5))
bw = cv2.erode(bw, kernel)
bw = cv2.dilate(bw, kernel)

kernel = np.ones((55,55))
bw = cv2.dilate(bw, kernel)
bw = cv2.erode(bw, kernel)

obj = cv2.bitwise_and(im2, im2, mask=bw)

plt.subplot(2,2,1)
plt.imshow(im1)
plt.title('im1.jpg')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(im2)
plt.title('im2.jpg')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(obj, cmap='gray')
plt.title('object')
plt.axis('off')
plt.show()

