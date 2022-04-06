from PIL import ImageFilter, Image
import matplotlib.pyplot as plt

path = "C:\\Unit8\\Deal\\003971.jpg"
img = Image.open(path)
col, row = img.size

R, G, B = img.split()
Rp = R.load()
Gp = G.load()
Bp = B.load()

strike = 11

for start_x in range(120, 400, strike):
    for start_y in range(150, 250, strike):

        SR = 0; SG = 0; SB = 0

        for i in range(start_x, min(start_x + strike, 400)):
            for j in range(start_y, min(start_y + strike, 250)):
                # print(i, j)
                SR += Rp[i, j]; SG += Gp[i, j]; SB += Bp[i, j]

        SR /= strike * strike
        SG /= strike * strike
        SB /= strike * strike

        for i in range(start_x, min(start_x + strike, 400)):
            for j in range(start_y, min(start_y + strike, 250)):
                Rp[i, j] = int(SR); Gp[i, j] = int(SG); Bp[i, j] = int(SB)

new_img = Image.merge('RGB', (R, G, B))
plt.imshow(new_img)
plt.show()