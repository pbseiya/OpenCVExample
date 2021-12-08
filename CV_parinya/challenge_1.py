import numpy as np
import matplotlib.pyplot as plt

Japan = np.ones((600,900,3))
r = 3/5/2 * Japan.shape[0]
c = [i/2 for i in Japan.shape[:2]]
for i in range(Japan.shape[0]):
    for j in range(Japan.shape[1]):
        if (i-c[0])**2 + (j-c[1])**2 <= r**2:
            Japan[i, j, 1:] = 0
plt.imshow(Japan)
# plt.axis(['off])
plt.show()