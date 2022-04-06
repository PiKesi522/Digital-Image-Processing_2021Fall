import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
import math
import cv2
from PIL import Image

path = "C:\\Unit7\\qb.png"

Image = cv2.imread(path)
BilImage = cv2.bilateralFilter(Image, 0, 50, 50)
Image = cv2.cvtColor(Image, cv2.COLOR_BGRA2RGB)
BilImage = cv2.cvtColor(BilImage, cv2.COLOR_BGRA2RGB)

plt.subplot(121), plt.title("Image"), plt.imshow(Image)
plt.subplot(122), plt.title("Bilateral"), plt.imshow(BilImage)
plt.show()