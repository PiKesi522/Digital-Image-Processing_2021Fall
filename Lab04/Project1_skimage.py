from skimage import io
import matplotlib.pyplot as plt

path = "C:\\Unit4\\gray\\1.jpg"

img = io.imread(path)
rows, cols = img.shape[:2]

for i in range(rows):
    for j in range(cols):
        Color = img[i, j, 0] * 2 + 12
        if Color > 255:
            Color = 255
        for k in range(3):
            img[i, j, k] = Color

plt.imshow(img, cmap="gray")
plt.show()