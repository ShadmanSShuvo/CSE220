import numpy as np
import matplotlib.pyplot as plt

image = np.random.randint(0, 256, (256, 256))

plt.imshow(image, cmap="gray")
plt.title("Random Grayscale Image")
plt.colorbar()
plt.show()
