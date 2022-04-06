# 提前选择种子点
from skimage import io, exposure, filters
import matplotlib.pyplot as plt
import numpy as np
import queue
import cv2

def Region_Growing(img, seed = [(134, 14)], threshold = 30):
    [m, n] = img.shape
    result = np.zeros((m, n))  # 建立等大小空矩阵
    min = np.min(img)
    max = np.max(img)
    k = ((max - min) / 255) * threshold
    mean = 0
    q = queue.Queue()

    for i in range(len(seed)):
        result[seed[i][1]][seed[i][0]] = 1  # 设立种子点
        q.put((seed[i][1], seed[i][0]))
        mean = 0
        num = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                mean += img[seed[i][1] + x][seed[i][0] + y]
                num += 1

    mean = mean / num
    count = len(seed)
    while not q.empty() :
        now = q.get()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x + now[0] >= 0 and x + now[0] < m:
                    if y + now[1] >= 0 and y + now[1] < n:
                        if abs(img[now[0]+x][now[1]+y] - mean) <= k and result[now[0]+x][now[1]+y] != 1:
                            result[now[0] + x][now[1] + y] = 1.0
                            q.put([now[0]+x, now[1]+y])
                            mean = (mean * count + img[now[0]+x][now[1]+y])/(count+1) # 通过新加入点更新平均值
                            count += 1
    return result


img = io.imread('./img1.png', as_gray=True)
seeds = [(250, 250)] #该点需要自己设定
mask = Region_Growing(img, seeds, 40)
plt.imshow(mask, cmap='gray')
plt.show()