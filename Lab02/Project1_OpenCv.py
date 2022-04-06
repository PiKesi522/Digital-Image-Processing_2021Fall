# 启动pycharm, 建立一个简单的工程project1，编写代码
# 分别完成对playboy、Flower、Pepper、fruits等不同图像的像素某些行和列的像素进行颜色修改的功能，然后显示编辑后的结果。

import cv2

path = "C:\\Unit2\\flower.jpg"
img = cv2.imread(path)
cols = img.shape[0]
rows = img.shape[1]
# OpenCv获取大小需要.shape,返回一个三元组

for i in range(cols):
    for j in range(rows):
        B = 255 - img[i, j, 0]
        G = 255 - img[i, j, 1]
        R = 255 - img[i, j, 2]
        # 反色
        img[i, j] = (B, G, R)

cv2.imshow("Flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = cv2.imread(path)
cols = img.shape[0]
rows = img.shape[1]
# OpenCv获取大小需要.shape,返回一个三元组

for i in range(cols):
    for j in range(rows):
        B = 255 - img[i, j, 0]
        G = 255 - img[i, j, 1]
        R = 255 - img[i, j, 2]
        # 反色
        img[i, j] = (B, G, R)

cv2.imshow("Dog", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = cv2.imread(path)
cols = img.shape[0]
rows = img.shape[1]
# OpenCv获取大小需要.shape,返回一个三元组

for i in range(cols):
    for j in range(rows):
        B = 255 - img[i, j, 0]
        G = 255 - img[i, j, 1]
        R = 255 - img[i, j, 2]
        # 反色
        img[i, j] = (B, G, R)

cv2.imshow("Cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()