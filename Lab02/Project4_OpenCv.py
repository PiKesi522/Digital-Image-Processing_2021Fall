# 启动pycharm, 建立一个简单的工程project4，编写代码
# 完成对上述彩色图像灰度化处理之后，同时在一个窗口内显示原图像和灰度化结果的图像。

import cv2
import matplotlib.pyplot as plt

path = "C:\\Unit2\\flower.jpg"
GBR_img = cv2.imread(path)
gray_img = cv2.cvtColor(GBR_img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(GBR_img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.title("RGB_Image")
plt.imshow(img)

plt.subplot(122)
plt.title("Gray_Image")
plt.imshow(gray_img, cmap="gray")
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
GBR_img = cv2.imread(path)
gray_img = cv2.cvtColor(GBR_img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(GBR_img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.title("RGB_Image")
plt.imshow(img)

plt.subplot(122)
plt.title("Gray_Image")
plt.imshow(gray_img, cmap="gray")
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
GBR_img = cv2.imread(path)
gray_img = cv2.cvtColor(GBR_img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(GBR_img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.title("RGB_Image")
plt.imshow(img)

plt.subplot(122)
plt.title("Gray_Image")
plt.imshow(gray_img, cmap="gray")
plt.show()

# ---------------------------------------------------------

