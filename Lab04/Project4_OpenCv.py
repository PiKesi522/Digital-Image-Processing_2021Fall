import cv2
import numpy as np

def set_color_r(gray):
    if(gray < 127).any():
        return 0
    elif(gray > 191).any():
        return 255
    else:
        return 4 * gray - 510

def set_color_g(gray):
    if(gray <= 63).any():
        return 254 - 4 * gray
    elif(gray >= 64).any() and (gray <= 127).any():
        return (gray - 191) * 4 - 254
    elif(gray >= 128).any() and (gray <= 191).any():
        return 255
    else:
        return 1022 - 4 * gray

def set_color_b(gray):
    if(gray >= 0).any() and (gray <= 63).any():
        return 255
    elif(gray >= 64).any() and (gray <= 127).any():
        return 510 - 4 * gray
    else:
        return 0

def trans_color(image):
    rows = image.shape[0]
    cols = image.shape[1]
    res = np.zeros((rows, cols, 3), np.uint8)
    for i in range(rows):
        for j in range(cols):
            r = set_color_r(image[i, j])
            g = set_color_g(image[i, j])
            b = set_color_b(image[i, j])
            res[i, j, 0] = r
            res[i, j, 1] = g
            res[i, j, 2] = b
    return res


path = "C:\\Unit4\\Fake\\5.png"
img = cv2.imread(path, 0)
img = trans_color(img)
cv2.imshow('Test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

