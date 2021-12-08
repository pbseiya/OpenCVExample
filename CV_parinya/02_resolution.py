#%%
import numpy as np
import matplotlib.pyplot as plt
import cv2

im = plt.imread('D:\OneDrive - IRPC\DS\Super AI Engineer\SuperAI\Level2\week4\CV_parinya\parrot.jpg')

# Spatial resolution
n = 3
for i in range(1, n+1):
    plt.subplot(1, n, i)
    s = 1/2**(i+1)
    plt.imshow(cv2.resize(im, None, fx=s, fy=s))
    plt.axis('off')
    plt.title(str(s))
plt.show()

# Intensity level resolution
from bitplane import bitplane2image, image2bitplane

for bpc in range(1, 9):
    bp = image2bitplane(im)
    bp[0:8-bpc, :, :] = 0  # R

#%%




    bp[8:8+8-bpc, :, :] = 0  # G
    bp[16:16+8-bpc, :, :] = 0  # B
    im_ = bitplane2image(bp)
    max_vl = sum([2**i for i in range(8-bpc, 8)])
    im_ = np.uint8(im_ / max_vl * 255)  # Fixed scale
    plt.subplot(2, 4, bpc)
    plt.imshow(im_)
    plt.axis('off')
    plt.title(str(bpc))
plt.show()