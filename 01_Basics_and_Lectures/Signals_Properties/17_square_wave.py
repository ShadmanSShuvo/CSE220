import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
x = np.sign(np.sin(2 * np.pi * 5 * t))

plt.plot(t, x)
plt.title("Square Wave")
plt.grid(True)
plt.show()
