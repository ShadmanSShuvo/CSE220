import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
x = np.sin(t)

plt.plot(t, x, label="sin(t)")
plt.plot(t, 2 * x, label="2sin(t)")
plt.plot(t, 0.5 * x, label="0.5sin(t)")

plt.legend()
plt.grid(True)
plt.show()
