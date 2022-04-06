from skimage import io,data,filters
import matplotlib.pyplot as plt

path = "C:\\Unit8\\Deal\\003971.jpg"
img = io.imread(path)
col, row = img.shape[:2]
plt.subplot(121);plt.title("Ori");plt.imshow(img)

strike = 11

for start_x in range(150, 250, strike):
    for start_y in range(120, 400, strike):

        sum = [0, 0, 0]

        for i in range(start_x,min(start_x + strike,250)):
            for j in range(start_y,min(start_y + strike, 400)):
                for k in range(3):
                    sum[k] += img[i, j, k]

        for k in range(3):
            sum[k] = sum[k] / (strike * strike)

        for i in range(start_x,min(start_x + strike,250)):
            for j in range(start_y,min(start_y + strike, 400)):
                for k in range(3):
                    img[i, j, k] = sum[k]

plt.subplot(122);plt.title("Mas, M=11");plt.imshow(img)
plt.show()