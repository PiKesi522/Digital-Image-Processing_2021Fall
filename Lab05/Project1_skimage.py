from skimage import filters, util, io
import matplotlib.pyplot as plt
from skimage.morphology import disk

path = "C:\\Unit5\\Smooth\\3.png"

img = io.imread(path, as_gray=True)

Medium_Filter = filters.median(img, disk(5))
Average_Filter = filters.rank.mean(img, disk(5))

plt.subplot(131)
plt.title("Mean Filter")
plt.imshow(Average_Filter, cmap="gray")

plt.subplot(132)
plt.title("Original")
plt.imshow(img, cmap="gray")

plt.subplot(133)
plt.title("Medium Filter")
plt.imshow(Medium_Filter, cmap="gray")
plt.show()