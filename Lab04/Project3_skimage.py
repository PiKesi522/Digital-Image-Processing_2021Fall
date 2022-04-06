from skimage import io, data, exposure, color
import matplotlib.pyplot as plt

path = "C:\\Unit4\\enhance\\2.png"
img = io.imread(path)
img = color.rgba2rgb(img)
img = color.rgb2gray(img)
rows, cols = img.shape[:2]
for i in range(rows):
    for j in range(cols):
        img[i, j] = int(img[i, j] * 255)

plt.figure("hist", figsize=(8, 8))
arr = img.flatten()


plt.subplot(221)
plt.imshow(img, plt.cm.gray)  # 原始图像


plt.subplot(222)
plt.hist(arr, bins=256, edgecolor='None', facecolor='red')  # 原始图像直方图


img1 = exposure.equalize_hist(img)  # 进行直方图均衡化
for i in range(rows):
    for j in range(cols):
        img1[i, j] = int(img1[i, j] * 255)
arr1 = img1.flatten()  # 返回数组折叠成一维的副本
plt.subplot(223)
plt.imshow(img1, plt.cm.gray)  # 均衡化图像


plt.subplot(224)
plt.hist(arr1, bins=256, edgecolor='None', facecolor='red')  # 均衡化直方图
plt.show()


