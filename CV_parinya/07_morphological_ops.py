import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('morph.png')[:, :, 0]
kernel = np.ones((17, 17))
im_dilated = cv2.dilate(im, kernel)
im_eroded = cv2.erode(im, kernel)

plt.subplot(2, 3, 1)
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(im_dilated, cmap='gray')
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(im_eroded, cmap='gray')
plt.axis('off')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17))
im_dilated = cv2.dilate(im, kernel)
im_eroded = cv2.erode(im, kernel)

plt.subplot(2, 3, 5)
plt.imshow(im_dilated, cmap='gray')
plt.axis('off')
plt.subplot(2, 3, 6)
plt.imshow(im_eroded, cmap='gray')
plt.axis('off')
plt.show()

# Opening and Closing
noise = (np.random.rand(*im.shape) > 0.999) + 0.
noise = cv2.dilate(noise, np.ones((5, 5)))
im1 = im/255 + noise
im1[im1 > 1] = 1
# im1 = np.uint8(im1*255)

kernel = np.ones((7, 7))
im_closed = cv2.dilate(im1, kernel)
im_closed = cv2.erode(im_closed, kernel)
im_opened = cv2.erode(im1, kernel)
im_opened = cv2.dilate(im_opened, kernel)

plt.subplot(2, 3, 1)
plt.imshow(im1, cmap='gray')
plt.axis('off')
plt.subplot(2, 3, 2)
plt.imshow(im_opened, cmap='gray')
plt.title('opening')
plt.axis('off')
plt.subplot(2, 3, 3)
plt.imshow(im_closed, cmap='gray')
plt.title('closing')
plt.axis('off')

im2 = im/255 - noise
im2[im2 < 0] = 0
# im2 = np.uint8(im2*255)

im_closed = cv2.dilate(im2, kernel)
im_closed = cv2.erode(im_closed, kernel)
im_opened = cv2.erode(im2, kernel)
im_opened = cv2.dilate(im_opened, kernel)

plt.subplot(2, 3, 4)
plt.imshow(im2, cmap='gray')
plt.axis('off')
plt.subplot(2, 3, 5)
plt.imshow(im_opened, cmap='gray')
plt.axis('off')
plt.title('opening')
plt.subplot(2, 3, 6)
plt.imshow(im_closed, cmap='gray')
plt.axis('off')
plt.title('closing')
plt.show()