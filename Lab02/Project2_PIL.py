# 启动pycharm, 建立一个简单的工程project2，编写代码
# 完成对上述图像处理，实现灰度化处理的功能，然后显示编辑后的结果

from PIL import Image
import matplotlib.pyplot as plt

path = "C:\\Unit2\\flower.jpg"
img = Image.open(path)
gray_img = img.convert('L')
# PIL转变为灰度图的方法使用.concert(args)方法
# 其中args是目标的图像通道模式‘L’为灰度图; ‘RGB‘为三通道24位图
plt.imshow(gray_img, cmap="gray")
# 由于PIL本身并不具有窗口界面，所以只能使用plt
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = Image.open(path)
gray_img = img.convert('L')
# PIL转变为灰度图的方法使用.concert(arg)方法
# 其中arg是目标的图像通道模式‘L’为灰度图; ‘RGB‘为三通道24位图
plt.imshow(gray_img, cmap="gray")
# 由于PIL本身并不具有窗口界面，所以只能使用plt
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = Image.open(path)
gray_img = img.convert('L')
# PIL转变为灰度图的方法使用.concert(arg)方法
# 其中arg是目标的图像通道模式‘L’为灰度图; ‘RGB‘为三通道24位图
plt.imshow(gray_img, cmap="gray")
# 由于PIL本身并不具有窗口界面，所以只能使用plt
plt.show()
