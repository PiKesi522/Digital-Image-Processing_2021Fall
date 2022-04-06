from skimage import io
import matplotlib.pyplot as plt

path1 = "C:\\第3章\\代数运算\\图像合成\\1.png"
path2 = "C:\\第3章\\代数运算\\图像合成\\2.png"

pic1 = io.imread(path1)
pic2 = io.imread(path2)

pic1 = pic1[:189, :, :]
pic2 = pic2[:, :263, :]
cols, rows, dims = pic1.shape

for i in range(cols):
    for j in range(rows):
        R = (pic1[i, j, 0] / 2 + pic2[i, j, 0] / 2)
        G = (pic1[i, j, 1] / 2 + pic2[i, j, 1] / 2)
        B = (pic1[i, j, 2] / 2 + pic2[i, j, 2] / 2)

        if R > 255:
            R = 255
        if G > 255:
            G = 255
        if B > 255:
            B = 255

        pic2[i, j, 0] = R
        pic2[i, j, 1] = G
        pic2[i, j, 2] = B

plt.imshow(pic2)
plt.show()

# ---------------------------------------------------------

path1 = "C:\\第3章\\代数运算\\图像扣取\\1.png"
path2 = "C:\\第3章\\代数运算\\图像扣取\\2.png"

pic1 = io.imread(path1)
pic2 = io.imread(path2)
pic1 = pic1[:206, :262, :]

cols, rows, dims = pic1.shape

for i in range(cols):
    for j in range(rows):
        if pic2[i, j, 0] <= 100:
            pic1[i, j, 0] = 0
            pic1[i, j, 1] = 0
            pic1[i, j, 2] = 0

plt.imshow(pic1)
plt.show()