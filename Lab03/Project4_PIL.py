from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Unit3\\zoom\\1.png"

img = Image.open(path)

width, height = img.size
width = int(width * 0.3)
height = int(width * 0.65)

Zoom_Img = img.resize((width, height), Image.ANTIALIAS)

plt.subplot(121)
plt.title('Ori Img')
plt.imshow(img)
plt.subplot(122)
plt.title("Zoomed Img")
plt.imshow(Zoom_Img)
plt.show()