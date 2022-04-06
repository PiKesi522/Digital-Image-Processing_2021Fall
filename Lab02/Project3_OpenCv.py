# 启动pycharm, 建立一个简单的工程project3，编写代码
# 完成对上述图像处理，实现截取部分图像功能，然后显示编辑后的结果。

import cv2

path = "C:\\Unit2\\flower.jpg"
img = cv2.imread(path)
part = img[100:200, 100:200]
cv2.imshow("part_Flower", part)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = cv2.imread(path)
part = img[100:200, 100:200]
cv2.imshow("part_Dog", part)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = cv2.imread(path)
part = img[100:200, 100:200]
cv2.imshow("part_Cat"
           "", part)
cv2.waitKey(0)
cv2.destroyAllWindows()


