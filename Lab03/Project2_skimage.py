from skimage import io
import matplotlib.pyplot as plt

path1 = "C:\\第3章\\逻辑运算\\1.jpg"
path2 = "C:\\第3章\\逻辑运算\\3.png"

gray_img1 = io.imread(path1)
gray_img2 = io.imread(path2)

gray_img1 = gray_img1[:227, :, :]
gray_img2 = gray_img2[:, :281, :]

cols, rows = gray_img1.shape[:2]

for i in range(cols):
    for j in range(rows):
        if gray_img1[i, j, 0] <= 100:
            for p in range(3):
                gray_img1[i, j, p] = 0
        else:
            for p in range(3):
                gray_img1[i, j, p] = 255

        if gray_img2[i, j, 0] <= 150:
            for p in range(3):
                gray_img2[i, j, p] = 0
        else:
            for p in range(3):
                gray_img2[i, j, p] = 255

        if (gray_img1[i, j, 0] == 255) and (gray_img2[i, j, 0] == 255):
            for p in range(3):
                gray_img1[i, j, p] = 255
        else:
            for p in range(3):
                gray_img1[i, j, p] = 0


plt.imshow(gray_img1)
plt.show()

# ---------------------------------------------------------

path1 = "C:\\第3章\\逻辑运算\\1.jpg"
path2 = "C:\\第3章\\逻辑运算\\3.png"

gray_img1 = io.imread(path1)
gray_img2 = io.imread(path2)

gray_img1 = gray_img1[:227, :, :]
gray_img2 = gray_img2[:, :281, :]

cols, rows = gray_img1.shape[:2]

for i in range(cols):
    for j in range(rows):
        if gray_img1[i, j, 0] <= 125:
            for p in range(3):
                gray_img1[i, j, p] = 0
        else:
            for p in range(3):
                gray_img1[i, j, p] = 255

        if gray_img2[i, j, 0] <= 100:
            for p in range(3):
                gray_img2[i, j, p] = 0
        else:
            for p in range(3):
                gray_img2[i, j, p] = 255

        if (gray_img1[i, j, 0] == 0) and (gray_img2[i, j, 0] == 0):
            for p in range(3):
                gray_img1[i, j, p] = 0
        else:
            for p in range(3):
                gray_img1[i, j, p] = 255

plt.imshow(gray_img1)
plt.show()

# ---------------------------------------------------------

path1 = "C:\\第3章\\逻辑运算\\1.jpg"

gray_img1 = io.imread(path1)

gray_img1 = gray_img1[:227, :, :]

cols, rows = gray_img1.shape[:2]

for i in range(cols):
    for j in range(rows):
        if gray_img1[i, j, 0] <= 100:
            for p in range(3):
                gray_img1[i, j, p] = 0
        else:
            for p in range(3):
                gray_img1[i, j, p] = 255

        if gray_img1[i, j, 0] == 0:
            for p in range(3):
                gray_img1[i, j, p] = 255
        else:
            for p in range(3):
                gray_img1[i, j, p] = 0

plt.imshow(gray_img1)
plt.show()
