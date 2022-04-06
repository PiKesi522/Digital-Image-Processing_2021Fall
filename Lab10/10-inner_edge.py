import cv2
import numpy as np

## 测试图片，为反斜杠
pic = "./data/flower.bmp" #'./img1-1.png'

## a.图像的二值化 ，这里没有做阈值处理
src = cv2.imread(pic, cv2.IMREAD_UNCHANGED)

## b.设置卷积核5*5
kernel = np.ones((5, 5), np.uint8)

## c.图像的腐蚀，默认迭代次数
erosion = cv2.erode(src, kernel)

## 效果展示
cv2.imshow('origin', src)
cv2.waitKey(0)

## 腐蚀后
cv2.imshow('after erosion', erosion)
cv2.waitKey(0)

## 取差求边缘
inner_edge =src - erosion
cv2.imshow('inner edge', inner_edge)
cv2.waitKey(0)