# 启动pycharm, 建立一个简单的工程project1，编写代码
# 分别完成对playboy、Flower、Pepper、fruits等不同图像的像素某些行和列的像素进行颜色修改的功能，然后显示编辑后的结果。

from skimage import io
# skimage.io 读取出来的图片是numpy格式
# 因而io读入的图片是(height, width, channel)的shape
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Unit2\\flower.jpg"
rgb_img = io.imread(path)
img_rows, img_cols, img_dims = rgb_img.shape

rgb_img[1:100, 100:200, 0] = 0
rgb_img[1:100, 100:200, 1] = 255
rgb_img[1:100, 100:200, 2] = 0
# 区域设置颜色，G通道能量为255，R,B通道能量为零，显示为纯绿

for i in range(300, 400, 10):
    for j in range(500, 600):
        rgb_img[i, j, 0] = 0
        rgb_img[i, j, 1] = 0
        rgb_img[i, j, 2] = 0

io.imshow(rgb_img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
rgb_img = io.imread(path)
img_rows, img_cols, img_dims = rgb_img.shape

rgb_img[1:100, 100:200] = 255
# 区域设置颜色，255的为白色块

for i in range(300, 400, 10):
    for j in range(500, 600):
        rgb_img[i, j, 0] = 0
        rgb_img[i, j, 1] = 0
        rgb_img[i, j, 2] = 0

io.imshow(rgb_img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
rgb_img = io.imread(path)
img_rows, img_cols, img_dims = rgb_img.shape

rgb_img[1:100, 100:200] = 255
# 区域设置颜色，255的为白色块

for i in range(30, 200, 10):
    for j in range(50, 150):
        rgb_img[i, j, 0] = 0
        rgb_img[i, j, 1] = 0
        rgb_img[i, j, 2] = 0

io.imshow(rgb_img)
plt.show()