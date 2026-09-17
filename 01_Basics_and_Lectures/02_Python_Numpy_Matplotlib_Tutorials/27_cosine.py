import numpy as np
import matplotlib.pyplot as plt

A = 3
f = 2
t = np.linspace(0, 2, 1000)
x = A * np.cos(2 * np.pi * f * t)

plt.plot(t, x)
plt.title("Cosine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
