from PIL import ImageFilter, Image
import matplotlib.pyplot as plt

path = "C:\\Unit5\\Smooth\\3.png"

img = Image.open(path).convert('L')
plt.imshow(img, cmap="gray")
plt.show()

Medium_Filter = img.filter(ImageFilter.MedianFilter(5))
plt.imshow(Medium_Filter, cmap="gray")
plt.show()

# 均值滤波直接逻辑实现

cols, rows = img.size
img_pixel = img.load()
for i in range(1, cols - 1):
    for j in range(1, rows - 1):
        img_pixel[i, j] = \
            (img_pixel[i - 1, j - 1] + img_pixel[i, j - 1] + img_pixel[i + 1, j] +
             img_pixel[i - 1, j    ] + img_pixel[i, j    ] + img_pixel[i + 1, j] +
             img_pixel[i - 1, j + 1] + img_pixel[i, j + 1] + img_pixel[i + 1, j + 1]) // 9
plt.imshow(img, cmap="gray")
plt.show()
