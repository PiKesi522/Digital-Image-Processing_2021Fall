from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np

path = "D:\\桌面1\\第3章\\缩放与插值\\1.png"
img = Image.open(path)
cols, rows = img.size
Board = Image.new('RGBA', img.size, (255, 255, 255, 255))

gray_img = img.convert('L')
pixels = gray_img.load()
Board_pixels = Board.load()

for i in range(cols):
    for j in range(rows):
        if pixels[i, j] < 77:
            Board_pixels[i, j] = (0, 0, 0, 0)

Board = ImageChops.multiply(Board, img)

pathB = "D:\\桌面1\\第3章\\缩放与插值\\girl.bmp"
Background = Image.open(pathB).convert('RGBA')
# print(Background)

Background.paste(Board, (100,100,100+cols,100+rows))
kk = Background.load()

plt.imshow(Background)
plt.savefig("D:\\桌面1\\第3章\\t.png")
plt.show()

