from PIL import Image,ImageFilter
import matplotlib.pyplot as plt

path = "C:\\Unit8\\Deal\\003941.jpg"

img = Image.open(path)

plt.imshow(img.filter(ImageFilter.EMBOSS))
plt.show()