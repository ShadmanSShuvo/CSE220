import numpy as np
import matplotlib.pyplot as plt

steps = np.random.choice([-1, 1], 1000)
walk = np.cumsum(steps)

plt.plot(walk)
plt.title("Random Walk")
plt.grid(True)
plt.show()
