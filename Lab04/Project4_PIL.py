from PIL import Image
import math
import matplotlib.pyplot as plt

Color_Box = [(0, 0, 100, 255), (0, 100, 100, 255), (0, 100, 0, 255), (100, 100, 0, 255), (100, 0, 0, 255)]

path = "C:\\Unit4\\Fake\\6.png"
img = Image.open(path)
rows, cols = img.size
print(rows, cols)
# 强度分层

Color_Num = 5
MIN = 255
MAX = 0

r, g, b, a = img.split()
pixel = r.load()
img_pixel = img.load()

for i in range(rows):
    for j in range(cols):
        if pixel[i, j] < MIN:
            MIN = pixel[i, j]
        elif pixel[i, j] > MAX:
            MAX = pixel[i, j]

Each_Color_Scale = math.ceil((MAX - MIN) // Color_Num + 1)

for i in range(rows):
    for j in range(cols):
        target = math.floor((pixel[i, j] - MIN) // Each_Color_Scale)
        img_pixel[i, j] = Color_Box[target]

plt.imshow(img)
plt.show()