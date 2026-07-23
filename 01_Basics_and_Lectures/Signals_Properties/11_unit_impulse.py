import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 1000)
impulse = np.zeros_like(t)
impulse[500] = 1

plt.stem(t, impulse)
plt.title("Unit Impulse Approximation")
plt.grid(True)
plt.show()
