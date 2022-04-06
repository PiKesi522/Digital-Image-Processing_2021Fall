from PIL import Image
import matplotlib.pyplot as plt

path = "C:\\Unit4\\gray\\1.jpg"

img = Image.open(path).convert('L')
cols, rows = img.size

lim_down = 40
color_down = 0
lim_up = 180
color_up = 255

pixel = img.load()

for i in range(cols):
    for j in range(rows):
        Color = pixel[i, j]
        if Color < lim_down:
            Color = color_down
        elif Color > lim_up:
            Color = color_up
        else:
            Color = (color_up - color_down) * (Color - lim_down) // (lim_up - lim_down) + color_down

        pixel[i, j] = Color

plt.imshow(img, cmap="gray")
plt.show()

