# 启动pycharm, 建立一个简单的工程project1，编写代码
# 分别完成对playboy、Flower、Pepper、fruits等不同图像的像素某些行和列的像素进行颜色修改的功能，然后显示编辑后的结果。

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Unit2\\flower.jpg"
img = Image.open(path)
pixels = img.load()
# PLT改变像素颜色需要先调用.load()方法
cols, rows = img.size
color = 0
for i in range(cols // 2):
    for j in range(rows // 2):
        if i * j <= 25500:
            color = i * j // 100
        else:
            color = 255
        pixels[i, j] = (color, color, color)
        # 在改变像素的时候直接在原图上改变RGB值
plt.imshow(img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = Image.open(path)
pixels = img.load()
# PLT改变像素颜色需要先调用.load()方法
cols, rows = img.size
color = 0
for i in range(30000):
    # 随机增加噪点
    x = np.random.randint(cols)
    y = np.random.randint(rows)
    pixels[x, y] = (0, 0, 0)
    # 在改变像素的时候直接在原图上改变RGB值
plt.imshow(img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = Image.open(path)
pixels = img.load()
# PLT改变像素颜色需要先调用.load()方法
cols, rows = img.size
color = 0
for i in range(30000):
    # 随机增加噪点
    x = np.random.randint(cols)
    y = np.random.randint(rows)
    pixels[x, y] = (0, 0, 0)
    # 在改变像素的时候直接在原图上改变RGB值
plt.imshow(img)
plt.show()