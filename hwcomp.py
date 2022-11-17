import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology

mask1=np.array ([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
    ])

mask2=np.array ([
    [1,1,1,1],
    [1,1,1,1],
    [1,1,0,0],
    [1,1,0,0],
    [1,1,1,1],
    [1,1,1,1]
    ])

mask3=np.array ([
    [1,1,1,1],
    [1,1,1,1],
    [0,0,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ])

mask4=np.array ([
    [1,1,0,0,1,1],
    [1,1,0,0,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
    ])

mask5=np.array ([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,0,0,1,1],
    [1,1,0,0,1,1]
    ])

img = np.load('C:\\ps.npy.txt')

f1= morphology.binary_hit_or_miss(img, mask1)
f2= morphology.binary_hit_or_miss(img, mask2)
f3= morphology.binary_hit_or_miss(img, mask3)
f4= morphology.binary_hit_or_miss(img, mask4)
f5= morphology.binary_hit_or_miss(img, mask5)

print('Type 1: ', np.sum(f1))
print('Type 2: ', np.sum(f2))
print('Type 3: ', np.sum(f3))
print('Type 4: ', np.sum(f4))
print('Type 5: ', np.sum(f5))
print('All obj: ', np.sum([f1,f2,f3,f4,f5]))

plt.figure()
plt.subplot(121)
plt.imshow(img)
plt.show()
