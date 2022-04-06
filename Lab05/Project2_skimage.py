from skimage import io, filters, data, feature, util
from skimage.morphology import disk
import matplotlib.pyplot as plt

path = "C:\\Unit5\\Sharpen\\1.jpg"

img = io.imread(path, as_gray=True)
plt.imshow(img, cmap="gray")
plt.show()

Edge_Sobel = filters.sobel(img)
Edge_Laplace = filters.laplace(img)
Edge_Canny = feature.canny(img, sigma=1)
plt.subplot(131)
plt.title("Sobel")
plt.imshow(Edge_Sobel,cmap="gray")
plt.subplot(132)
plt.title("Laplace")
plt.imshow(Edge_Laplace,cmap="gray")
plt.subplot(133)
plt.title("Canny")
plt.imshow(Edge_Canny,cmap="gray")
plt.show()


Edge_Sobel = util.img_as_ubyte(Edge_Sobel)
img = util.img_as_ubyte(img)

cols, rows = img.shape[:2]
for i in range(cols):
    for j in range(rows):
        Color = img[i, j] + Edge_Sobel[i, j]
        if Color > 255:
            Color = 255
        img[i, j] = Color
plt.imshow(Edge_Sobel, cmap="gray")
plt.show()
plt.imshow(img, cmap="gray")
plt.show()
