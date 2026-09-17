import numpy as np
import matplotlib.pyplot as plt

A = 2
f = 5
t = np.linspace(0, 2, 1000)
x = A * np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
