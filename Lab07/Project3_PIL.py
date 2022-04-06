import numpy as np
from PIL import features, Image
import math
import matplotlib.pyplot as plt

def getClosenessWeight(sigma_g, H, W):
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    closeWeight = np.exp(-0.5*np.power(r, 2) + np.power(c, 2) / math.pow(sigma_g, 2))
    return closeWeight

def BilateralrFilter(I, H, W, sigma_g, sigma_d):
    # 构建空间距离权重模板
    closenessWeight = getClosenessWeight(sigma_g, H, W)

    # 模板的中心点位置
    H_Center = (H - 1) // 2
    W_Center = (W - 1) // 2

    # 图像矩阵的行数和列数
    rows, cols = I.shape

    # 双边滤波后的结果
    bflGrayImage = np.zeros(I.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = I[r][c]
            # 判断边界
            rTop = 0 if r - H_Center < 0 else r - H_Center
            rBottom = rows - 1 if r + H_Center > rows - 1 else r + H_Center
            cLeft = 0 if c - W_Center < 0 else c - W_Center
            cRight = cols - 1 if c + W_Center > cols - 1 else c + W_Center

            # 权重模板作用的区域
            region = I[rTop:rBottom+1, cLeft:cRight+1]

            # 构建灰度值相似性的权重因子
            similarityWeightTemp = np.exp(-0.5*np.power(region-pixel, 2.0) / math.pow(sigma_d, 2))
            closenessWeightTemp = closenessWeight[rTop-r+H_Center:rBottom-r+H_Center+1, cLeft-c+W_Center:cRight-c+W_Center+1]

            # 两个权重模板相乘
            weightTemp= similarityWeightTemp * closenessWeightTemp

            # 归一化权重模板
            weightTemp = weightTemp / np.sum(weightTemp)

            # 权重模板和对应的邻域值相乘求和
            bflGrayImage[r][c] = np.sum(region * weightTemp)
    return bflGrayImage

path = "C:\\Unit7\\pbb.png"

image = Image.open(path).convert('L')
fimage = np.array(image)
bflGrayImage = BilateralrFilter(fimage, fimage.shape[0], fimage.shape[1], 45, 0.02)

plt.subplot(121), plt.title("Original Image"), plt.imshow(Image)
plt.subplot(122), plt.title("Bilateral Image"), plt.imshow(bflGrayImage)
plt.show()