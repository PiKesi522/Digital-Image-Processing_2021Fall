from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Unit3\\geo\\1.jpg"

img = Image.open(path)

LeftRight_img = img.transpose(Image.FLIP_LEFT_RIGHT)
TopDown_img = img.transpose(Image.FLIP_TOP_BOTTOM)

Rotate_img_Expand = img.rotate(30, expand = True)
Rotate_img = img.rotate(30)

Board = Image.new('RGB', img.size, (255, 255, 255))
Board = ImageChops.offset(img, 50, 50)
Board.paste((0, 0, 0), (0, 0, 50, Board.size[1]))
Board.paste((0, 0, 0), (0, 0, Board.size[0], 50))

Processed_Board = Image.new('RGB', img.size, (255, 255, 255))
Processed_Board = ImageChops.offset(img, 50, 50)

plt.subplot(241)
plt.title("Origin Img")
plt.imshow(img)

plt.subplot(242)
plt.title("Rotate Img\n(Full Scale)")
plt.imshow(Rotate_img_Expand)

plt.subplot(246)
plt.title("Rotate Img\n(Same Size)")
plt.imshow(Rotate_img)

plt.subplot(243)
plt.title("Left-Right Img")
plt.imshow(LeftRight_img)

plt.subplot(247)
plt.title("Top-Down Img")
plt.imshow(TopDown_img)

plt.subplot(244)
plt.title("Moved Img")
plt.imshow(Board)

plt.subplot(248)
plt.title("Moved Img\n(Processed)")
plt.imshow(Processed_Board)

plt.show()