import numpy as np
from skimage import io, filters
import matplotlib.pyplot as plt

img = io.imread("./data/flower.bmp", as_gray=True)
result = np.zeros(img.shape)
t = 0.35


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] > t:
            result[i][j] = 1

plt.imshow(result, cmap = 'gray')
plt.show()