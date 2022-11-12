import numpy as np
import matplotlib.pyplot as plt
# pip install scikit-image
from skimage.measure import regionprops, label

def count_lakes_and_bays(region):
  symbol = ~region.image
  lb = label(symbol)
  lakes = 0
  bays = 0
  for reg in regionprops(lb):
    for y, x in reg.coords:
      if (y == 0 or x == 0 or y == region.image.shape[0]-1
          or x == region.image.shape[1]-1):
          bays += 1
      else:
          lakes += 1
          break     
  return lakes, bays
  
def recognize(im_region):
  return None
  
im = plt.imread("alphabet.png")
im = np.mean(im, 2)
im[im > 0] = 1

lb = label(im)
regions = regionprops(lb)
for reg in regions:
  lakes, _ = count_lakes_and_bays(reg)
  if lakes == 2:
      plt.figure()
      plt.imshow(reg.image)
#print(recognize(regions[50]))

#plt.imshow(regions[50].image)
plt.show()