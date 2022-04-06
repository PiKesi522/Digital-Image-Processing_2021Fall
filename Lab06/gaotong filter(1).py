# 理想高通滤波实现
import numpy as np
import cv2
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
I = cv2.imread('../image/1.png')
cv2.imshow('original',I)
(r,g,b) = cv2.split(I)
I = cv2.merge([b,g,r])
J = np.double(cv2.cvtColor(I,cv2.COLOR_RGB2GRAY))
D1 = 30
D2 = 60
D3 = 160
Fuv = np.fft.fftshift(np.fft.fft2(J))
print('Fuv',Fuv)
print(I.shape)
m,n = I.shape[0],I.shape[1]
xo = np.floor(m/2)
yo = np.floor(n/2)
h1 = np.zeros((m,n))
h2 = np.zeros((m,n))
h3 = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        D = np.sqrt((i-xo)**2+(j-yo)**2)
        if D>=D1:
            h1[i,j]=1
        else:
            h1[i,j]=0
        if D>=D2:
            h2[i,j]=1
        else:
            h2[i,j]=0
        if D>=D3:
            h3[i,j]=1
        else:
            h3[i,j]=0
Guv1 = h1*Fuv
Guv2 = h2*Fuv
Guv3 = h3*Fuv
g1 = np.fft.ifftshift(Guv1)
g1 = np.uint8(np.real(np.fft.ifft2(g1)))
print('g1',g1)
g2 = np.fft.ifftshift(Guv2)
g2 = np.uint8(np.real(np.fft.ifft2(g2)))
print('g2',g2)
g3 = np.fft.ifftshift(Guv3)
g3 = np.uint8(np.real(np.fft.ifft2(g3)))
print('g3',g3)
plt.subplot(2,2,1),plt.imshow(I),plt.title('原图像')
plt.subplot(2,2,2),plt.imshow(g1),plt.title('D0=30')
plt.subplot(2,2,3),plt.imshow(g2),plt.title('D0=60')
plt.subplot(2,2,4),plt.imshow(g3),plt.title('D0=160')
plt.show()
