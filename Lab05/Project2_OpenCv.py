import cv2
import numpy as np

path = "C:\\Unit5\\Sharpen\\1.jpg"
img = cv2.imread(path)

Sharpen_Filter = np.array([
    [0 , -1, 0 ],
    [-1, 5 , -1],
    [0 , -1, 0 ],
])

Sharpen_Img = cv2.filter2D(img, -1, Sharpen_Filter)
cv2.imshow("test",Sharpen_Img)
cv2.waitKey(0)