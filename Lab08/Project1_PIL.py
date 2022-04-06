from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Unit8\\Deal\\003941.jpg"

img = Image.open(path)
R, G, B = img.split()
col, row = img.size

R_pixel = R.load()
G_pixel = G.load()
B_pixel = B.load()

for i in range(col):
    for j in range(row):
        R_pixel[i, j] = 255 - R_pixel[i, j]
        G_pixel[i, j] = 255 - G_pixel[i, j]
        B_pixel[i, j] = 255 - B_pixel[i, j]

New_img = Image.merge('RGB', (R, G, B))
plt.imshow(New_img)
plt.show()