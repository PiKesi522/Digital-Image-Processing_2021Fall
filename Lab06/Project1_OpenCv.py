import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Unit6\\Pics\\5.png"

img = cv2.imread(path, 0)

F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
Central_Fourier = np.log(np.abs(Fshift))

cols, rows = img.shape
Radius = 20
LowPass_Filter = np.zeros((cols, rows))
LowPass_Filter[cols//2 - Radius:cols//2 + Radius, rows//2 - Radius:rows//2 + Radius] = 1

Processed_Img = Fshift * LowPass_Filter
Processed_Img = np.fft.ifftshift(Processed_Img)
Processed_Img = np.fft.ifft2(Processed_Img)
Processed_Img = np.abs(Processed_Img)
Processed_Img = (Processed_Img - np.amin(Processed_Img)) / (np.amax(Processed_Img) - np.amin(Processed_Img))

plt.subplot(131), plt.imshow(img, cmap="gray"), plt.title("Original_Img")
plt.subplot(132), plt.imshow(Central_Fourier, cmap="gray"), plt.title("Central Fourier")
plt.subplot(133), plt.imshow(Processed_Img, cmap="gray"), plt.title("Processed Img")
plt.show()