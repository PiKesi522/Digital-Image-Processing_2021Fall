# 交互式选择种子点
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

def get_location(img):
    clicks = []
    img *= 255
    img = img.astype(np.uint8)
    def on_mouse(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('Start Mouse Position: ' + str(x) + ', ' + str(y))
            s_box = x, y
            print(s_box)
            clicks.append(s_box)
    cv2.namedWindow('input')
    cv2.setMouseCallback('input', on_mouse, 0)
    cv2.imshow('input', img)
    cv2.waitKey()
    return clicks


img = io.imread('./img2.png', as_gray=True)
seeds = get_location(img)
mask = Region_Growing(img, seeds, 40)
plt.imshow(mask, cmap='gray')
plt.show()