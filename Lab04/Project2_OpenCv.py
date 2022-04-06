import cv2

path = "C:\\Unit4\\enhance\\1.jpg"

img = cv2.imread(path)
cols, rows = img.shape[:2]

for i in range(cols):
    for j in range(rows):
        for k in range(3):
            color = 0.005 * pow(img[i, j, k], 2)
            if color < 0:
                color = 0
            elif color > 255:
                color = 255

            img[i, j, k] = color

cv2.imshow("test",img)
cv2.waitKey(0)