from skimage import io,transform
import matplotlib.pyplot as plt

path = "C:\\第3章\\缩放与插值\\1.png"

ori_img = io.imread(path)
y, x, dims = ori_img.shape
Zoom_img = transform.rescale(ori_img, [1.2, 0.5, 1])
plt.subplot(121)
# (尺寸)1行 2列 (第1张图)
plt.title("Zoom_Pic")
plt.imshow(Zoom_img)

plt.subplot(122)
# (尺寸)1行 2列 (第2张图)
plt.title("Ori_Image")
plt.imshow(ori_img)
plt.show()