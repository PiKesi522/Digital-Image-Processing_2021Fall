from skimage import io, exposure, img_as_float
import matplotlib.pyplot as plt

path = "C:\\Unit4\\enhance\\2.png"
img = io.imread(path)
img = img_as_float(img)

img1 = exposure.adjust_gamma(img, 2)
img2 = exposure.adjust_gamma(img, 0.5)

plt.subplot(121)
plt.title("gamma = 2")
plt.imshow(img1)
plt.subplot(122)
plt.title("gamma = 0.5")
plt.imshow(img2)
plt.show()