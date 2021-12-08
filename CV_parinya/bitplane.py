import numpy as np


def image2bitplane(img):
    bp = []
    for c in range(img.shape[2]):
        for i in range(8):
            bp.append(img[:, :, c] // 2 ** i % 2)
    return np.array(bp)


def bitplane2image(bp):
    img = np.zeros((bp[0].shape[0], bp[0].shape[1], 3))
    for b in range(len(bp)):
        img[:, :, b//8] = img[:, :, b//8] + (bp[b] * 2**(b % 8))
    return np.uint8(img)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    img1 = plt.imread('peterparker.jpg')
    bp = image2bitplane(img1)
    print(len(bp))
    for b in range(len(bp)):
        plt.subplot(3, 8, b + 1)
        plt.imshow(bp[b])
    plt.show()
    img2 = bitplane2image(bp)
    plt.subplot(1, 3, 1)
    plt.imshow(img1)
    plt.subplot(1, 3, 2)
    plt.imshow(img2)
    plt.subplot(1, 3, 3)
    plt.imshow(np.abs(img1 - img2))
    plt.show()