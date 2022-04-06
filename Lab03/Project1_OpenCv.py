import cv2
import numpy as np
path1 = "C:\\Unit3\\alg\\add\\1.png"
path2 = "C:\\Unit3\\alg\\add\\2.png"
pic1 = cv2.imread(path1)
pic2 = cv2.imread(path2)
pic1 = cv2.resize(pic1, (279, 189))

cols, rows = pic1.shape[:2]
board = np.full((rows, cols, 3), (255, 255, 255), np.uint8)

board = cv2.add(pic1, pic2)
cv2.imshow("Add", board)
cv2.waitKey(0)
board = cv2.subtract(pic1, pic2)
cv2.imshow("Substract", board)
cv2.waitKey(0)

board = cv2.multiply(pic1, pic2)
cv2.imshow("Multiply", board)
cv2.waitKey(0)
board = cv2.divide(pic1, pic2)
cv2.imshow("Divide", board)
cv2.waitKey(0)