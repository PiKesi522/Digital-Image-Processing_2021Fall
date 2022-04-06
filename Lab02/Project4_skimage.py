# 启动pycharm, 建立一个简单的工程project4，编写代码
# 完成对上述彩色图像灰度化处理之后，同时在一个窗口内显示原图像和灰度化结果的图像。

from skimage import io
import matplotlib.pyplot as plt

path = "C:\\Unit2\\flower.jpg"
rgb_img = io.imread(path)
gray_img = io.imread(path, as_gray=True)
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("RGB_Image")
plt.imshow(rgb_img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Gray_Image")
plt.imshow(gray_img, plt.cm.gray)
# plt.imshow的方法显示灰度图需要额外参数，否则会使用G通道的图片
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
rgb_img = io.imread(path)
gray_img = io.imread(path, as_gray=True)
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("RGB_Image")
plt.imshow(rgb_img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Gray_Image")
plt.imshow(gray_img, plt.cm.gray)
# plt.imshow的方法显示灰度图需要额外参数，否则会使用G通道的图片
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
rgb_img = io.imread(path)
gray_img = io.imread(path, as_gray=True)
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("RGB_Image")
plt.imshow(rgb_img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Gray_Image")
plt.imshow(gray_img, plt.cm.gray)
# plt.imshow的方法显示灰度图需要额外参数，否则会使用G通道的图片
plt.show()