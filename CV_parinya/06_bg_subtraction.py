import cv2
import numpy as np
import matplotlib.pyplot as plt

im1 = plt.imread('im1.jpg')
im2 = plt.imread('im2.jpg')

diff_RGB = cv2.absdiff(im1, im2)
# diff_RGB = np.uint8(np.abs(im1/255 - im2/255)*255)

def angle_diff(a1, a2):
    return (180 - abs(abs(a1 - a2) - 180)) / 360

def absdiff_hsv(hsv1, hsv2):
    h1 = hsv1[:, :, 0] * 2.
    h2 = hsv2[:, :, 0] * 2.
    diff = np.zeros(hsv1.shape).astype(np.uint8)
    diff[:, :, 0] = np.uint8(angle_diff(h1, h2) * 255)
    diff[:, :, 1:] = np.uint8(np.abs(hsv1[:, :, 1:]/255 - hsv1[:, :, 2:]/255)*255)
    return diff


hsv1 = cv2.cvtColor(im1, cv2.COLOR_RGB2HSV)
hsv2 = cv2.cvtColor(im2, cv2.COLOR_RGB2HSV)
diff_HSV = absdiff_hsv(hsv1, hsv2)
diff_H = diff_HSV[:, :, 0]

plt.subplot(2, 2, 1)
plt.imshow(im1)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(im2)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(diff_RGB)
plt.axis('off')
plt.title('diff_RGB')

plt.subplot(2, 2, 4)
plt.imshow(diff_H, cmap='gray')
plt.axis('off')
plt.title('diff_H')
plt.show()