# 启动pycharm, 建立一个简单的工程project3，编写代码
# 完成对上述图像处理，实现截取部分图像功能，然后显示编辑后的结果。

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Unit2\\flower.jpg"
img = Image.open(path)
size = (100, 100, 300, 300)
# 目标截取区域是从（100，100）到（300，300）的区块
part = img.crop(size)
# 截取区域使用.crop(args)方法，截取目标区域
# 其中args表示目标区域
plt.imshow(part)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = Image.open(path)
size = (100, 100, 300, 300)
# 目标截取区域是从（100，100）到（300，300）的区块
part = img.crop(size)
# 截取区域使用.crop(args)方法，截取目标区域
# 其中args表示目标区域
plt.imshow(part)
plt.show()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = Image.open(path)
size = (100, 100, 300, 300)
# 目标截取区域是从（100，100）到（300，300）的区块
part = img.crop(size)
# 截取区域使用.crop(args)方法，截取目标区域
# 其中args表示目标区域
plt.imshow(part)
plt.show()


