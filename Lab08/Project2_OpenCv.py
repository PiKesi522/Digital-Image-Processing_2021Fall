import cv2

path = "C:\\Unit8\\Deal\\003941.jpg"

img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

col, row = img.shape[:2]

for i in range(1, col):
    for j in range(row):
        prev = img[i - 1, j, 0]
        pres = img[i, j, 0]
        new = pres - prev + 200
        if new > 255:
            new = 255

        if new < 0:
            new = 0

        img[i-1, j] = new

cv2.imshow("test", img)
cv2.waitKey(0)
