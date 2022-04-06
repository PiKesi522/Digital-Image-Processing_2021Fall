import cv2

path = "C:\\Unit3\\zoom\\1.png"
img = cv2.imread(path)
y, x = img.shape[0:2]
Zoom_img1 = cv2.resize(img, (int(x/2), int(y/2)))
Zoom_img2 = cv2.resize(img, (int(x*2), int(y*2)), interpolation=cv2.INTER_NEAREST)
cv2.imshow('1/2', Zoom_img1)
cv2.imshow('1', img)
cv2.imshow('2',Zoom_img2)
cv2.waitKey(0)