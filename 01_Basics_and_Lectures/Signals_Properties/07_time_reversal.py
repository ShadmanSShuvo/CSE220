import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 1000)
original = np.exp(-t)
reversed_signal = np.exp(t)

plt.plot(t, original, label="x(t)")
plt.plot(t, reversed_signal, label="x(-t)")
plt.legend()
plt.grid(True)
plt.show()
