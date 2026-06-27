import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.zeros_like(t)

for n in [1, 3, 5, 7, 9]:
    y += (1 / n) * np.sin(n * t)

y = (4 / np.pi) * y

plt.plot(t, y)
plt.title("Fourier Square Wave")
plt.grid(True)
plt.show()
