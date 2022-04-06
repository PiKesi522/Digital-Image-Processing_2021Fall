import cv2
import matplotlib.pyplot as plt

path = "C:\\Unit5\\Smooth\\3.png"

img = cv2.imread(path)

Mean_img = cv2.blur(img, (5, 5))
Medium_img = cv2.medianBlur(img, 5)

plt.title("Mean")
plt.imshow(Mean_img)
plt.show()
plt.title("Medium")
plt.imshow(Medium_img)
plt.show()
