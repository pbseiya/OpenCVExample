import cv2
import matplotlib.pyplot as plt

bgr = cv2.imread('challenge_3.jpg')
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
rgb = bgr[:,:,::-1]

# RGB
plt.subplot(2,4,1)
plt.imshow(rgb)
plt.axis('off')
plt.title('RGB')

lower = 0
upper = 50
#Red
maskR = cv2.inRange(rgb, (250,lower,lower), (255,upper,upper))
plt.subplot(2,4,2)
plt.imshow(maskR)
plt.axis('off')
plt.title('red')

#Green
maskG = cv2.inRange(rgb, (lower,250,lower), (upper,255,upper))
plt.subplot(2,4,3)
plt.imshow(maskG)
plt.axis('off')
plt.title('green')

#Blue
maskB = cv2.inRange(rgb, (lower,lower,250), (upper,upper,255))
plt.subplot(2,4,4)
plt.imshow(maskB)
plt.axis('off')
plt.title('blue')

#HSV
plt.subplot(2,4,5)
plt.imshow(hsv)
plt.axis('off')
plt.title('HSV')

lower_s, upper_s = 100,255
lower_v, upper_v = 100,255
#Red
maskR = cv2.inRange(hsv,(0,lower_s,lower_v),(5,upper_s,upper_v)) | \
        cv2.inRange(hsv,(175,lower_s,lower_v),(180,upper_s,upper_v))
plt.subplot(2,4,6)
plt.imshow(maskR)
plt.axis('off')
plt.title('red')

#Green
maskG = cv2.inRange(hsv,(55,lower_s,lower_v),(65,upper_s,upper_v))
plt.subplot(2,4,7)
plt.imshow(maskG)
plt.axis('off')
plt.title('green')

#Blue
maskB = cv2.inRange(hsv,(115,lower_s,lower_v),(125,upper_s,upper_v))
plt.subplot(2,4,8)
plt.imshow(maskB)
plt.axis('off')
plt.title('red')
plt.show()

