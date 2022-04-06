import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import io,data, img_as_float,color
from skimage.util import random_noise



path = "C:\\Unit7\\Recover\\3.png"
image = io.imread(path)
image = color.rgba2rgb(image)
image = color.rgb2gray(image)
plt.subplot(131), plt.title("Original"), plt.imshow(image, cmap="gray")

image_pepper = random_noise(image, mode="pepper", seed=100, clip=True)
plt.subplot(132), plt.title("PepperNoise"), plt.imshow(image_pepper, cmap="gray")


image_bilateral = denoise_bilateral(image, sigma_color=0.05, sigma_spatial=15)
plt.subplot(133), plt.title("Bilateral") , plt.imshow(image_bilateral, cmap="gray")

plt.show()