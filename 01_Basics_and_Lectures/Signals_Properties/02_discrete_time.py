import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11)
x = 2 * n

plt.stem(n, x)
plt.title("Discrete-Time Signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()
