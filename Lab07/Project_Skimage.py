import matplotlib.pyplot as plt

from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet, estimate_sigma)
from skimage import io, data, img_as_float, color
from skimage.util import random_noise
from scipy.signal import wiener, invresz
import numpy as np
from numpy import fft
import math


def motion_process(image_size, motion_angle):
    PSF = np.zeros(image_size)
    center_position = (image_size[0] - 1) / 2

    slope_tan = math.tan(motion_angle * math.pi / 180)
    slope_cot = 1 / slope_tan
    if slope_tan <= 1:
        for i in range(15):
            offset = round(i * slope_tan)  # ((center_position-i)*slope_tan)
            PSF[int(center_position + offset), int(center_position - offset)] = 1
        return PSF / PSF.sum()  # 对点扩散函数进行归一化亮度
    else:
        for i in range(15):
            offset = round(i * slope_cot)
            PSF[int(center_position - offset), int(center_position + offset)] = 1
        return PSF / PSF.sum()


# 对图片进行运动模糊
def make_blurred(input, PSF, eps):
    input_fft = fft.fft2(input)  # 进行二维数组的傅里叶变换
    PSF_fft = fft.fft2(PSF) + eps
    blurred = fft.ifft2(input_fft * PSF_fft)
    blurred = np.abs(fft.fftshift(blurred))
    return blurred


path = "C:\\Unit7\\Recover\\3.png"
image = io.imread(path)
image = color.rgba2rgb(image)
image = color.rgb2gray(image)
print(image.shape)
PSF = motion_process(image.shape[:2], 30)
blurred = make_blurred(image, PSF, 1e-3)

image_wiener = wiener(image, image.shape[:2], PSF)


def Inverse_blurred(input, PSF, eps):
    input_fft = fft.fft2(input)  # 进行二维数组的傅里叶变换
    PSF_fft = fft.fft2(PSF) + eps
    restoration = fft.ifft2(input_fft / PSF_fft)
    restoration = np.abs(fft.fftshift(restoration))
    return restoration


image_inverse = Inverse_blurred(blurred, PSF, 1e-3)

plt.subplot(221), plt.title("Original"), plt.imshow(image, cmap="gray")
plt.subplot(222), plt.title("Blurred"), plt.imshow(blurred, cmap="gray")
plt.subplot(223), plt.title("Wiener"), plt.imshow(image_wiener, cmap="gray")
plt.subplot(224), plt.title("Inverse"), plt.imshow(image_inverse, cmap="gray")
plt.show()
