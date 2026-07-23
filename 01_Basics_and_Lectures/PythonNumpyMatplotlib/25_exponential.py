import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
x = np.exp(-t)

plt.plot(t, x)
plt.title("Exponential Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
