from skimage import io, filters, data
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Unit6\\Pics\\2.png"

img = io.imread(path, as_gray=True)

Blurred = filters.gaussian(img, sigma=5)

plt.subplot(121), plt.imshow(img, plt.cm.gray), plt.title("Original Img")
plt.subplot(122), plt.imshow(Blurred, plt.cm.gray), plt.title("Gauss Filter")
plt.show()
