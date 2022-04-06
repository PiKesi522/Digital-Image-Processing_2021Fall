from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt

path = "C:\\Unit4\\enhance\\1.jpg"
img = Image.open(path)
rows, cols = img.size
r, g, b, a= img.split()
rp = r.load()
gp = g.load()
bp = b.load()
pixel = img.load()
new_img = np.zeros((rows, cols, 3), dtype=np.float32)

c = 10
gamma = 0.5
for i in range(rows):
    for j in range(cols):
        color_R = int(c * math.pow(rp[i, j], gamma))
        color_G = int(c * math.pow(gp[i, j], gamma))
        color_B = int(c * math.pow(bp[i, j], gamma))

        if color_R > 255:
            color_R = 255
        if color_G > 255:
            color_G = 255
        if color_B > 255:
            color_B = 255

        rp[i, j] = color_R
        gp[i, j] = color_G
        bp[i, j] = color_B


img = Image.merge('RGB', (r,g,b))
plt.imshow(img)
plt.show()
