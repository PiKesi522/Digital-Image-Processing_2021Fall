# 高斯滤波
from skimage import data,filters
import matplotlib.pyplot as plt

img = data.astronaut()

edges1 = filters.gaussian_filter(img,sigma=0.4) #sigma=0.4
edges2 = filters.gaussian_filter(img,sigma=5) #sigma=5
plt.figure('gaussian',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)
plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)
plt.show()