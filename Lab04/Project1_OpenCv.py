import cv2

path = "C:\\Unit4\\gray\\1.jpg"

img = cv2.imread(path)

cols, rows = img.shape[:2]

for i in range(cols):
    for j in range(rows):
        for k in range(3):
            img[i, j, k] = 255 - img[i, j, k]

cv2.imshow("test", img)
cv2.waitKey(0)