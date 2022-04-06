import numpy as np
from skimage import io
import matplotlib.pyplot as plt

img = io.imread("./data/flower.bmp", as_gray=True)
result = np.zeros(img.shape)
t = np.mean(img)
d = t
e = 0.1

while d >= e:
    count_1 = 0
    total_1 = 0
    count_2 = 0
    total_2 = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] > t:
                total_1 += img[i][j]
                count_1 += 1
                result[i][j] = 1
            else:
                result[i][j] = 0
                total_2 += img[i][j]
                count_2 += 1
    d = abs(t - ((total_1 / count_1) + (total_2 / count_2)))/ 2
    t = ((total_1 / count_1) + (total_2 / count_2)) / 2

plt.imshow(result, cmap = 'gray')
plt.show()