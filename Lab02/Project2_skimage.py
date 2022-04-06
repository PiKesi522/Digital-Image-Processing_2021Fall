# 启动pycharm, 建立一个简单的工程project2，编写代码
# 完成对上述图像处理，实现灰度化处理的功能，然后显示编辑后的结果

from skimage import io, color
import matplotlib.pyplot as plt

path = "C:\\Unit2\\flower.jpg"
ori_img = io.imread(path, as_gray=True)
# 读取图片的时候直接读取灰色图片
io.imshow(ori_img)
# 使用io.imshow可以自动转换成灰度图像
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
ori_img = io.imread(path)
gray_img = color.rgb2gray(ori_img)
# 利用内置方法将三通道图转换成单通道的灰度图
io.imshow(gray_img)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
gray_img = io.imread(path, as_gray=True)
plt.imshow(gray_img, cmap="gray")
# 使用plt.imshow需要额外加一个参数，否则会变成绿色通道图
plt.show()
