import cv2

path = "C:\\Unit8\\Deal\\003941.jpg"

img = cv2.imread(path)

col, row = img.shape[:2]

for i in range(col):
    for j in range(row):
        for k in range(3):
            img[i, j, k] = 255 - img[i, j, k]

cv2.imshow("test",img)
cv2.waitKey(0)