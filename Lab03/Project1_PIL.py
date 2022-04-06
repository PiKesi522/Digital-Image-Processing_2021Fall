from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np

path1 = "C:\\第3章\\代数运算\\图像合成\\1.png"
path2 = "C:\\第3章\\代数运算\\图像合成\\2.png"
pic1 = Image.open(path1)
pic2 = Image.open(path2)

pic2 = pic2.resize(pic1.size)

cols, rows = pic1.size
board = np.full((cols, rows, 3), (255, 255, 255), np.uint8)

board = Image.blend(pic1, pic2, 0.9)

plt.imshow(board)
plt.show()