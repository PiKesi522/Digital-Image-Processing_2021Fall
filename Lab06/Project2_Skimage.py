from skimage import io,filters
import numpy as np
import matplotlib.pyplot as plt
import math

path = "C:\\Unit6\\Pics\\4.png"

img = io.imread(path, as_gray=True)
F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
Central_Fourier = np.log(np.abs(Fshift))

cols, rows = img.shape

Radius = 30
HighPass_Filter = np.ones((cols, rows))
for i in range(cols):
    for j in range(rows):
        Distance = abs(cols//2 - i) + abs(rows//2 - j)
        if Distance < Radius:
            HighPass_Filter[i, j] = 1 - math.exp(-Distance ** 2 / (2 * Radius ** 2))

Processed_Img = Fshift * HighPass_Filter
Processed_Img = np.fft.ifftshift(Processed_Img)
Processed_Img = np.fft.ifft2(Processed_Img)
Processed_Img = np.abs(Processed_Img)
Processed_Img = (Processed_Img - np.amin(Processed_Img)) / (np.amax(Processed_Img) - np.amin(Processed_Img))

plt.subplot(131), plt.imshow(img, cmap="gray"), plt.title("Original_Img")
plt.subplot(132), plt.imshow(Central_Fourier, cmap="gray"), plt.title("Central Fourier")
plt.subplot(133), plt.imshow(Processed_Img, cmap="gray"), plt.title("Processed Img")
plt.show()
