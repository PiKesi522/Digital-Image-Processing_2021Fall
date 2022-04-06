from skimage import io, data, color, exposure
import math
import matplotlib.pyplot as plt

Color_Box = [(0, 0, 100, 255), (0, 100, 100, 255), (0, 100, 0, 255), (100, 100, 0, 255), (100, 0, 0, 255)]

path = "C:\\Unit4\\Fake\\5.png"
img = io.imread(path)
rows, cols = img.shape[:2]
# 强度分层

Color_Num = 5
MIN = 255
MAX = 0

for i in range(rows):
    for j in range(cols):
        if img[i, j, 0] < MIN:
            MIN = img[i, j, 0]
        elif img[i, j, 0] > MAX:
            MAX = img[i, j, 0]

Each_Color_Scale = math.ceil((MAX - MIN) // Color_Num + 1)

for i in range(rows):
    for j in range(cols):
        target = math.floor((img[i, j, 0] - MIN) // Each_Color_Scale)
        img[i, j] = Color_Box[target]

plt.imshow(img)
plt.show()