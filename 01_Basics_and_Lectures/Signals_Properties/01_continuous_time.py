import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
x = 3 * np.sin(2 * np.pi * t)

plt.plot(t, x)
plt.title("Continuous-Time Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
