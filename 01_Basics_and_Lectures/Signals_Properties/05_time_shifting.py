import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
x = np.sin(t)
shifted = np.sin(t - 2)

plt.plot(t, x, label="Original")
plt.plot(t, shifted, label="Shifted")
plt.legend()
plt.grid(True)
plt.show()
