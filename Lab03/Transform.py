import cv2
import numpy as np

path = 'C:\\Unit3\\trans\\1.png'
im_bgr = cv2.imread(path)  # 读入图像
im_gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)  # 转灰度
im_gray = cv2.GaussianBlur(im_gray, (3, 3), 0)  # 滤波降噪
im_edge = cv2.Canny(im_gray, 30, 50)  # 边缘检测
cv2.imshow('Go', im_edge)  # 显示边缘检测结果
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(im_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 提取轮廓
rect, area = None, 0  # 找到的最大四边形及其面积
for item in contours:
    hull = cv2.convexHull(item)  # 寻找凸包
    epsilon = 0.1 * cv2.arcLength(hull, True)  # 忽略弧长10%的点
    approx = cv2.approxPolyDP(hull, epsilon, True)  # 将凸包拟合为多边形
    if len(approx) == 4 and cv2.isContourConvex(approx):  # 如果是凸四边形
        ps = np.reshape(approx, (4, 2))
        ps = ps[np.lexsort((ps[:, 0],))]
        lt, lb = ps[:2][np.lexsort((ps[:2, 1],))]
        rt, rb = ps[2:][np.lexsort((ps[2:, 1],))]
        a = cv2.contourArea(approx)  # 计算四边形面积
        if a > area:
            area = a
            rect = (lt, lb, rt, rb)

im = np.copy(im_bgr)
for p in rect:
    im = cv2.line(im, (p[0] - 10, p[1]), (p[0] + 10, p[1]), (0, 0, 255), 1)
    im = cv2.line(im, (p[0], p[1] - 10), (p[0], p[1] + 10), (0, 0, 255), 1)

cv2.imshow('go', im)
cv2.waitKey(0)

lt, lb, rt, rb = rect
pts1 = np.float32([(10,10), (10,270), (150,10), (150,270)])
pts2 = np.float32([lt, lb, rt, rb])
m = cv2.getPerspectiveTransform(pts2, pts1) # 生成透视矩阵
board_gray = cv2.warpPerspective(im_gray, m, (160, 260)) # 对灰度图执行透视变换
board_bgr = cv2.warpPerspective(im_bgr, m, (160, 260)) # 对彩色图执行透视变换
cv2.imshow('go', board_gray)
cv2.waitKey(0)
