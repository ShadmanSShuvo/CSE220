import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
f = 5
square = np.sign(np.sin(2 * np.pi * f * t))

plt.plot(t, square)
plt.title("Square Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
