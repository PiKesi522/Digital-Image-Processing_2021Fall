from skimage import io
import skimage.morphology as sm
import matplotlib.pyplot as plt

img = io.imread("./data/flower.bmp", as_gray=True)

dst=sm.closing(img,sm.disk(9))  #用边长为5的圆形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')
plt.show()