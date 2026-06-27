import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
x = np.exp(-2*t)

plt.plot(t, x)
plt.title("Exponential Signal")
plt.grid(True)
plt.show()
