import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(t) * np.cos(t)

plt.plot(t, x)
plt.title("Signal Multiplication")
plt.grid(True)
plt.show()
