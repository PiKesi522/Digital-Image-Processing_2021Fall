from skimage import io, transform, filters, img_as_ubyte
import matplotlib.pyplot as plt

path = "C:\\Unit5\\Sharpen\\1.jpg"

img = io.imread(path, as_gray=True)
img = img_as_ubyte(img)
edges_h = filters.prewitt_h(img)
edges_h = img_as_ubyte(edges_h)
plt.imshow(edges_h,cmap='gray')
plt.show()
edges_v = filters.prewitt_v(img)
edges_v = img_as_ubyte(edges_v)
plt.imshow(edges_v,cmap='gray')
plt.show()
edges = filters.prewitt(img)

rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        color = edges_h[i, j] + edges_v[i, j]
        if color > 255:
            color = 255
        img[i, j] = color

img = img_as_ubyte(img)
plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(edges, cmap='gray')
plt.show()
