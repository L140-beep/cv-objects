import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.morphology as snm
from skimage.measure import label

figures = np.array(([
                np.array(
                  ([1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],)),
                
                np.array(([1, 1, 1, 1],
                   [1, 1, 1, 1],
                   [1, 1, 0, 0],
                   [1, 1, 0, 0],
                   [1, 1, 1, 1],
                   [1, 1, 1, 1],)),
                   
                   np.array(
                  ([1, 1, 1, 1],
                   [1, 1, 1, 1],
                   [0, 0, 1, 1],
                   [0, 0, 1, 1],
                   [1, 1, 1, 1],
                   [1, 1, 1, 1],)),
                   
                   np.array(
                  ([1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1],)),
                   
                   np.array(
                  (
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   ))])
                  )

image = np.load("objects/files/ps.npy")

squere_count = label(snm.binary_erosion(image, figures[0])).max()

result = []
result.append(squere_count)

for figure in range(1, len(figures)):
    new_image = snm.binary_erosion(image, figures[figure])
    labeled = label(new_image)

    if (figure in [3, 4]):
        result.append(labeled.max() - squere_count)
        continue
    
    result.append(labeled.max())

print(result, np.array(result).sum(), label(image).max())
# plt.subplot(121)
# plt.title("До обработки")
# plt.imshow(image)
# plt.subplot(122)
# plt.title("После")
# plt.imshow(labeled)
# plt.show()