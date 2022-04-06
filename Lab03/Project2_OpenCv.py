import cv2
import numpy as np

path1 = "C:\\Unit3\\logic\\1.jpg"
path2 = "C:\\Unit3\\logic\\3.png"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
rows = img1.shape[0]
cols = img1.shape[1]
img2 = cv2.resize(img2, (cols, rows))

And = cv2.bitwise_and(img1, img2)
Or = cv2.bitwise_or(img1, img2)
Not = cv2.bitwise_not(img1)

cv2.imshow("And", And)
cv2.imshow("Or", Or)
cv2.imshow("Not", Not)
cv2.waitKey(0)