import cv2
from matplotlib import pyplot as plt

path = "C:\\Unit4\\enhance\\2.png"
img = cv2.imread(path)
cv2.imshow('image', img)
cv2.waitKey(0)
plt.subplot(121)
plt.hist(img.flatten(), 256, facecolor = 'red')  # numpy的ravel函数功能是将多维数组降为一维数组

(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
imgH = cv2.merge((bH, gH, rH))
imgH = cv2.cvtColor(imgH, cv2.COLOR_BGR2GRAY)

cv2.imshow('imageH', imgH)
cv2.waitKey(0)

plt.subplot(122)
plt.hist(imgH.flatten(), 256, facecolor = 'red')  # numpy的ravel函数功能是将多维数组降为一维数组
plt.show()
