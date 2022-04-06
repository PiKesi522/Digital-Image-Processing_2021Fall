from PIL import ImageFilter, Image
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Unit6\\Pics\\2.png"

img = Image.open(path).convert('L')
F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
Central_Fourier = np.log(np.abs(Fshift))

cols, rows = img.size[:2]
Radius = 20
N = 4

LowPass_Filter = np.ones((rows, cols))
for i in range(rows):
    for j in range(cols):
        Distance = abs(cols//2 - i) + abs(rows//2 - j)
        if Distance > Radius:
            LowPass_Filter[i, j] = 1 / (1 + (0.414 * Distance / Radius)**(2*N))

Processed_Img = Fshift * LowPass_Filter
Processed_Img = np.fft.ifftshift(Processed_Img)
Processed_Img = np.fft.ifft2(Processed_Img)
Processed_Img = np.abs(Processed_Img)
Processed_Img = (Processed_Img - np.amin(Processed_Img)) / (np.amax(Processed_Img) - np.amin(Processed_Img))

plt.subplot(131), plt.imshow(img, cmap="gray"), plt.title("Original_Img")
plt.subplot(132), plt.imshow(Central_Fourier, cmap="gray"), plt.title("Central Fourier")
plt.subplot(133), plt.imshow(Processed_Img, cmap="gray"), plt.title("Processed Img")
plt.show()
