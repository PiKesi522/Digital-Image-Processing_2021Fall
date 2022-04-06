# 启动pycharm, 建立一个简单的工程project3，编写代码
# 完成对上述图像处理，实现截取部分图像功能，然后显示编辑后的结果。

from skimage import io
import matplotlib.pyplot as plt

path = "C:\\Unit2\\flower.jpg"
rgb_img = io.imread(path)
img_rows, img_cols, img_dims = rgb_img.shape

resize_img = rgb_img[100:200, 100:200, :]
# 裁剪范围是原图像的高100-200，宽100-200的图像
io.imshow(resize_img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
rgb_img = io.imread(path)
img_rows, img_cols, img_dims = rgb_img.shape

resize_img = rgb_img[100:200, 100:200, :]
# 裁剪范围是原图像的高100-200，宽100-200的图像
io.imshow(resize_img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
rgb_img = io.imread(path)
img_rows, img_cols, img_dims = rgb_img.shape

resize_img = rgb_img[100:200, 100:200, :]
# 裁剪范围是原图像的高100-200，宽100-200的图像
io.imshow(resize_img)
plt.show()

