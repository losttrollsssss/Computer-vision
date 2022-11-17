import numpy as np
from scipy.ndimage import binary_erosion
import matplotlib.pyplot as plt
from skimage.measure import label

img = np.load('C:\\Users\ilyag\Downloads\stars.npy')

mask_pl= np.array([[0,0,1,0,0],
                    [0,0,1,0,0],
                    [1,1,1,1,1],
                    [0,0,1,0,0],
                    [0,0,1,0,0]])

mask_cross=np.array([[1,0,0,0,1],
                    [0,1,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],
                    [1,0,0,0,1]])

labeled4=label(img, connectivity=1)
print(f"Objects = {np.max(labeled4)}")
labeled8=label(img, connectivity=2)
print(f"Objects = {np.max(labeled8)}")

pluses=binary_erosion(img, mask_pl)
labeled=label(pluses)
print(f"Pluses count = {labeled.max()}")

crosses=binary_erosion(img, mask_cross)
labeled=label(crosses)
print(f"Crosses count = {labeled.max()}")

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(labeled8)
plt.show()
