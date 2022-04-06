from skimage import color,io,data,filters
import matplotlib.pyplot as plt

path = "C:\\Unit8\\Deal\\003941.jpg"

img = io.imread(path)
plt.subplot(121); plt.title("Original"); plt.imshow(img)

row, col = img.shape[:2]

for i in range(row):
    for j in range(col):
        for k in range(3):
            img[i, j, k] = 255 - img[i, j, k]

plt.subplot(122); plt.title("Reverse"); plt.imshow(img)
plt.show()