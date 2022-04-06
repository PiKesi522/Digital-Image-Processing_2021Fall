import cv2  # 此为opencv的Python包

path = "C:\\Pics_Unit1\\BMP\\flower.bmp"

img_flower = cv2.imread(path, 1)

# 第一个参数为路径,第二个参数为显示模式
#               1   (default)   3通道RGB
#               0               单通道灰度图
#               -1              4通道RGB + 透明通道

cv2.namedWindow('WindowsName', cv2.WINDOW_NORMAL)

# 第一个参数为窗口名，第二个参数代表窗口尺寸
#                   默认是cv2.WINDOW_AUTOSIZE,表示窗口自适应
#                        cv2.WINDOW_NORMAL，表示窗口大小可变
# 此处我们并不使用

cv2.imshow("ImageName", img_flower)

# 第一个参数为图片名，第二个参数代表图片对象

cv2.waitKey(0)

# 直到由键盘输入，一直显示


# 同理获得其他图像

path = "C:\\Pics_Unit1\\BMP\\boatssmall.bmp"
img_boats = cv2.imread(path)
path = "C:\\Pics_Unit1\\BMP\\fruits.bmp"
img_fruits = cv2.imread(path)
path = "C:\\Pics_Unit1\\BMP\\cornfield.bmp"
img_cornfield = cv2.imread(path)


cv2.imshow("ImageName", img_cornfield)
cv2.waitKey(0)
cv2.imshow("ImageName", img_boats)
cv2.waitKey(0)
cv2.imshow("ImageName", img_fruits)
cv2.waitKey(0)

cv2.destroyAllWindows()