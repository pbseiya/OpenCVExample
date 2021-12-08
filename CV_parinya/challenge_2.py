import numpy as np
import cv2
import matplotlib.pyplot as plt
from bitplane import image2bitplane, bitplane2image

im = cv2.imread('challenge_2.png')[: ,: ,::-1]
bp = image2bitplane(im)

idx = np.r_[4:8, 12:16, 20:24]
idx_ans = np.r_[0:4, 8:12, 16:20][::-1]

bp_ans = np.zeros_like(bp)
bp_ans[idx] = bp[idx_ans]
ans = bitplane2image(bp_ans)
plt.subplot(1,2,1)
plt.imshow(im)
plt.subplot(1,2,2)
plt.imshow(ans)
plt.show()