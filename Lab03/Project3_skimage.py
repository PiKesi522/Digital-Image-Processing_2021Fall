from skimage import io, transform
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\第3章\\几何运算\\1.jpg"

ori_pic = io.imread(path)
TopDown_pic = io.imread(path)
LeftRight_pic = io.imread(path)

cols, rows = ori_pic.shape[:2]

for i in range(cols):
    for j in range(rows):
        for p in range(3):
            TopDown_pic[i, j, p] = ori_pic[cols-1-i, j, p]
            LeftRight_pic[i, j, p] = ori_pic[i, rows-1-j, p]

plt.imshow(TopDown_pic)
plt.show()
plt.imshow(LeftRight_pic)
plt.show()

# ---------------------------------------------------------

path = "C:\\第3章\\几何运算\\1.jpg"

ori_pic = io.imread(path)
y, x, dims = ori_pic.shape
board = np.full((y, x, 3), (255, 255, 255), np.uint8)
move_x = 60
move_y = 80

for i in range(move_x, x):
    for j in range(move_y, y):
        for p in range(3):
            board[j, i, p] = ori_pic[j - move_y, i - move_x, p]

plt.imshow(board)
plt.show()

# ---------------------------------------------------------

path = "C:\\第3章\\几何运算\\1.jpg"

ori_pic = io.imread(path)
y, x, dims = ori_pic.shape
rotate_pic = transform.rotate(ori_pic, 30.0, True)
plt.imshow(rotate_pic)
plt.show()

