import cv2
import numpy as np

path = "C:\\Unit3\\geo\\1.jpg"

img = cv2.imread(path)

Right_Left_img = cv2.flip(img, 1)
Top_Down_img = cv2.flip(img, 0)

rows, cols, channels = img.shape
rotate = cv2.getRotationMatrix2D((rows*0.5, cols*0.5), 45, 1)
Rotate_img = cv2.warpAffine(img, rotate, (cols, rows))

M = np.float32([[1,0,100],[0,1,50]])
Moved_img = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Right_Left', Right_Left_img)
cv2.imshow('Top_Down', Top_Down_img)
cv2.imshow('Rotate', Rotate_img)
cv2.imshow('Move', Moved_img)
cv2.waitKey(0)

