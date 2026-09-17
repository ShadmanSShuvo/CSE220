import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
original = np.sin(t)
shifted = np.sin(t - np.pi / 4)

plt.plot(t, original, label="Original")
plt.plot(t, shifted, label="Shifted")

plt.legend()
plt.grid(True)
plt.show()
