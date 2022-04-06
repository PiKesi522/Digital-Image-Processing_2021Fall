from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

path1 = "C:\\Unit3\\logic\\1.jpg"
path2 = "C:\\Unit3\\logic\\3.png"

img1 = Image.open(path1)
img2 = Image.open(path2)

img2 = img2.resize(img1.size)

cols, rows = img1.size
board = np.full((rows, cols, 3), (255, 255, 255), np.uint8)

print(board.shape)
print(img1.size)

gray_img1 = img1.convert('L')
gray_img2 = img2.convert('L')

pixel1 = gray_img1.load()
pixel2 = gray_img2.load()

for i in range(cols):
    for j in range(rows):
        if pixel1[i, j] <= 100:
            pixel1[i, j] = 0
        else:
            pixel1[i, j] = 255

        if pixel2[i, j] <= 150:
            pixel2[i, j] = 0
        else:
            pixel2[i, j] = 255

plt.imshow(gray_img2, cmap="gray")
plt.show()

for i in range(cols):
    for j in range(rows):
        if (pixel1[i, j] == 255) and (pixel2[i, j] == 255):
            board[j, i] = (255, 255, 255)
        else:
            board[j, i] = (0, 0, 0)

plt.imshow(board)
plt.show()


