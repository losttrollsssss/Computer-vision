import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage import color

def get_colors(elements):
    c = {"blue": 0,"crimson": 0,"cobalt": 0,"cyan": 0,"green": 0,"lime": 0,"magenta": 0,"orange": 0,"red" : 0,"turquoise": 0,"violet": 0,"yellow": 0,}
    for color in elements:
        if (0 <= color < 15 or 345 <= color <= 360):
            c['red'] += 1
        if (15 <= color < 45):
            c['orange'] += 1
        if (45 <= color < 75):
            c['yellow'] += 1
        if (75 <= color < 105):
            c['lime'] += 1
        if (105 <= color < 135):
            c['green'] += 1
        if (135 <= color < 165):
            c['turquoise'] += 1
        if (165 <= color < 195):
            c['cyan'] += 1
        if (195 <= color < 225):
            c['cobalt'] += 1
        if (225 <= color < 255):
            c['blue'] += 1
        if (255 <= color < 285):
            c['violet'] += 1
        if (285 <= color < 315):
            c['magenta'] += 1
        if (315 <= color < 345):
            c['crimson'] += 1      
    print(c)

image = plt.imread("balls_and_rects.png")
binary = image.copy()[:, :, 0]
binary[binary > 0] = 1

image = color.rgb2hsv(image)[:, :, 0] * 360

labeled = label(binary)
balls, rects = [], []
print("Number of all forms:", np.max(labeled))

for region in regionprops(labeled):
    v = np.max(image[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]])
    if region.area == (region.image.shape[0] * region.image.shape[1]):
        rects.append(v)
    else:
        balls.append(v)

print("Circles:", len(balls))
get_colors(balls)

print("Rectangles:", len(rects))
get_colors(rects)

plt.figure()
plt.imshow(image)
plt.show()
