import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x1 = np.sin(t)
x2 = np.cos(t)
x3 = x1 + x2

plt.plot(t, x1, label="sin")
plt.plot(t, x2, label="cos")
plt.plot(t, x3, label="sum")
plt.legend()
plt.grid(True)
plt.show()
