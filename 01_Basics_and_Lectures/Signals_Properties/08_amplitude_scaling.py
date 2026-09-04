import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x = np.cos(t)

plt.plot(t, x, label="Original")
plt.plot(t, 3*x, label="Scaled")
plt.legend()
plt.grid(True)
plt.show()
