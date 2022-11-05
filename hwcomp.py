import numpy as np
import matplotlib.pyplot as plt
# pip install scikit-image
from skimage.measure import regionprops, label
from skimage.filters.thresholding import (threshold_li, threshold_otsu, threshold_local, threshold_yen, gaussian)

image = plt.imread("coins.jpg")
gray = np.mean(image, 2).astype("int")
g = gaussian(gray, 201)
gray = gray / g

th1 = threshold_local(gray, 101)
th2 = threshold_otsu(gray)
th3 = threshold_li(gray)
th4 = threshold_yen(gray)
plt.subplot(221)
plt.title("Local")
plt.imshow(gray > th1)
plt.subplot(222)
plt.title("Otsu")
plt.imshow(gray > th2)
plt.subplot(223)
plt.title("Li")
plt.imshow(gray > th3)
plt.subplot(224)
plt.title("Yen")
plt.imshow(gray > th4)
plt.show()