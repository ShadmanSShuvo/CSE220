import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 1000)
x = t**3 + t
x_neg = (-t)**3 + (-t)

xe = (x + x_neg) / 2
xo = (x - x_neg) / 2

plt.plot(t, xe, label="Even Part")
plt.plot(t, xo, label="Odd Part")
plt.legend()
plt.grid(True)
plt.show()
