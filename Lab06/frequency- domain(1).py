# 基于numpy傅立叶变换的低通滤波
#导入相关库
import cv2
import numpy as np
import matplotlib.pyplot as plt

#使用cv2 读入图片
new_img=cv2.imread('../image/1.png',0)

#numpy中的傅立叶变化
f1=np.fft.fft2(new_img)
f1_shift=np.fft.fftshift(f1)
#np.fft.fftshift()函数来实现平移,让直流分量在输出图像的重心

rows,cols=new_img.shape
crow,ccol=int(rows/2),int(cols/2) #计算频谱中心
mask=np.zeros((rows,cols),np.uint8) #生成rows行cols的矩阵，数据格式为uint8
mask[crow-30:crow+30,ccol-30:ccol+30]=1 #将靠近频谱中心的部分低通信息 设置为1，属于低通滤波
f1_shift=f1_shift*mask

#傅立叶逆变换
f_ishift=np.fft.ifftshift(f1_shift)
img_back=np.fft.ifft2(f_ishift)
img_back=np.abs(img_back)
img_back=(img_back-np.amin(img_back))/(np.amax(img_back)-np.amin(img_back))

plt.figure(figsize=(15,15))
plt.subplot(121),plt.imshow(new_img,cmap='gray'),plt.title('input image')
plt.subplot(122),plt.imshow(img_back,cmap='gray'),plt.title('output image')
plt.show()

