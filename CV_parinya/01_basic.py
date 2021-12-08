import numpy as np
import matplotlib.pyplot as plt

# im_shape = 480, 640, 3
# im = (np.random.rand(*im_shape)*255).astype(np.uint8)
# plt.imshow(im)
# plt.show()

# Flag of Thailand
Thai = np.ones((6, 9, 3))
Thai[[0, -1], :, 1:] = 0
Thai[2:4, :, :2] = 0
plt.imshow(Thai)
plt.show()

# # Import an image
# import matplotlib.pyplot as plt
# im = plt.imread('parrot.jpg')
# plt.imshow(im)
# plt.show()

# from PIL import Image
# im = Image.open('parrot.jpg')
# im = np.array(im)
# plt.imshow(im)
# plt.show()

# import cv2
# im = cv2.imread('parrot.jpg')
# cv2.imshow('im', im)
# cv2.waitKey()

# # Export an image
# cv2.imwrite('Thai.png', np.uint8(Thai[:, :, ::-1]*255))

# im = Image.fromarray(np.uint8(Thai*255))
# im.save('Thai.jpg')

# im2 = Image.fromarray(np.uint8(255-Thai*255))
# im.save('Thai.gif', save_all=True, append_images=[im2, im]*20)
