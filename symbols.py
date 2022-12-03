import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import regionprops, label

def count_lakes_and_bays(image):
    symbol= ~image
    lb = label(symbol)
    lakes=0
    bays=0
    for reg in regionprops(lb):
        is_lake = True
        for y, x in reg.coords:
            if y==0 or x == 0 or y == image.shape[0]-1 or x == image.shape[1]-1:
                is_lake = False
                break
        lakes += is_lake
        bays += not is_lake
    return lakes, bays

def has_vline(image):
    lines = np.sum(image, 0) // image.shape[0]
    return 1 in lines

def recognize(region):
    if np.all(region.image):
        return '-'
    lakes, bays = count_lakes_and_bays(region.image)
    if lakes == 2:
        if has_vline(region.image):
            return "B"
        else:
            return "8"
    elif lakes == 1:
        if bays == 3:
            return "A"
        if bays == 2:
            cy = region.image.shape[0] // 2
            cx = region.image.shape[1] // 2
            if region.image[cy, cx] > 0:
                return "P"
            return "D"
        else:
            return "0"
    elif lakes == 0:
        if bays == 2:
            return "/"
        elif bays == 3 and has_vline(region.image):
            return "1"
        cut_lakes,cut_bays = count_lakes_and_bays(region.image[2:-2, 2:-2])
        if cut_bays == 4:
            return "X"
        elif cut_bays == 5:
            cy = region.image.shape[0] // 2
            cx = region.image.shape[1] // 2
            if region.image[cy, cx] > 0:
                return "*"
            return "W"
    return None

image = plt.imread("symbols.png")
im = np.sum(image, 2)
im[im > 0] = 1 

labeled = label(im)
print(f"Objects = {np.max(labeled)}")

regions=regionprops(labeled)
result = {None:0}
for region in regions:
    symbol = recognize(region)
    if symbol is not None:
        labeled[np.where(labeled == region.label)] = 0
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1

print(result)
print(round((1. - result[None] / sum(result.values())) * 100, 2))

#plt.imshow(labeled)
#print(recognize(regions[35])) #1 - B, 3 - 8, 35 - 0, 
#plt.imshow(regions[35].image)
#plt.show()