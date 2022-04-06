# 启动pycharm, 建立一个简单的工程project4，编写代码
# 完成对上述彩色图像灰度化处理之后，同时在一个窗口内显示原图像和灰度化结果的图像。

from PIL import Image
import matplotlib.pyplot as plt

path = "C:\\Unit2\\flower.jpg"
img = Image.open(path)
gray_img = img.convert('L')
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("RGB_Image")
plt.imshow(img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Gray_Image")
plt.imshow(gray_img, cmap="gray")
# plt.imshow的方法显示灰度图需要额外参数，否则会使用G通道的图片
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = Image.open(path)
gray_img = img.convert('L')
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("RGB_Image")
plt.imshow(img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Gray_Image")
plt.imshow(gray_img, cmap="gray")
# plt.imshow的方法显示灰度图需要额外参数，否则会使用G通道的图片
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = Image.open(path)
gray_img = img.convert('L')
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("RGB_Image")
plt.imshow(img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Gray_Image")
plt.imshow(gray_img, cmap="gray")
# plt.imshow的方法显示灰度图需要额外参数，否则会使用G通道的图片
plt.show()