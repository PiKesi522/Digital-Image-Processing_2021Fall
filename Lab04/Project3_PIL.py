from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Unit4\\enhance\\2.png"
img = Image.open(path).convert('L')
plt.figure("hist", figsize=(8, 8))

plt.subplot(221)
plt.imshow(img, cmap="gray")

img = np.array(img)
plt.subplot(222)
plt.hist(img.flatten(), bins=256, edgecolor='None', facecolor='red')  # 原始图像直方图

# 计算图像的直方图
# 在numpy中，也提供了一个计算直方图的函数histogram(),第一个返回的是直方图的统计量，第二个为每个bins的中间值
imhist, bins = np.histogram(img.flatten(), 256, density=True)
cdf = imhist.cumsum()
cdf = 255.0 * cdf / cdf[-1]
# 使用累积分布函数的线性插值，计算新的像素值
img2 = np.interp(img.flatten(), bins[:-1], cdf)
img2 = img2.reshape(img.shape)

plt.subplot(223)
plt.imshow(img2, cmap="gray")

plt.subplot(224)
plt.hist(img2.flatten(), bins=256, edgecolor='None', facecolor='red')
plt.show()
