import numpy as np
import matplotlib.pyplot as plt

# Discrete indices
n = np.arange(0, 4)

# Signal samples
x = np.array([1, -2, 2, -1])

plt.figure(figsize=(8, 4))

plt.stem(n, x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("Sample index, n")
plt.ylabel("x[n]")
plt.title("Discrete-Time Signal")

plt.grid(True)
plt.show()