from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

path = "C:\\Unit5\\Sharpen\\1.jpg"

img = Image.open(path)

sharpen_img = img.filter(ImageFilter.SHARPEN)

sharpen_img2 = sharpen_img.filter(ImageFilter.SHARPEN)

plt.subplot(131)
plt.title("Origin_Img")
plt.imshow(img)

plt.subplot(132)
plt.title("Sharpen_Once_Img")
plt.imshow(sharpen_img)

plt.subplot(133)
plt.title("Sharpen_Twice_Img")
plt.imshow(sharpen_img2)

plt.show()