# 启动pycharm, 建立一个简单的工程project2，编写代码
# 完成对上述图像处理，实现灰度化处理的功能，然后显示编辑后的结果

import cv2

path = "C:\\Unit2\\flower.jpg"
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Flower", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------

path = "C:\\Unit2\\dog.jpg"
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Dog", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------

path = "C:\\Unit2\\cat.jpg"
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Cat", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

