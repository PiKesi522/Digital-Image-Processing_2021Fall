from skimage import io,data,color,filters
import matplotlib.pyplot as plt

path = "C:\\Unit8\\Deal\\003941.jpg"

img = io.imread(path)
plt.subplot(121);plt.title('Original');plt.imshow(img)

img = color.rgb2gray(img)

col, row = img.shape[:2]

for i in range(1, col):
    for j in range(row):
        prev = img[i - 1, j]
        pres = img[i, j]
        new = (pres - prev)*255 + 128
        if new > 255:
            new = 255

        if new < 0:
            new = 0

        img[i-1, j] = new

plt.subplot(122);plt.title('Emboss');plt.imshow(img, cmap="gray")
plt.show()