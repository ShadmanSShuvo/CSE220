import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)

y = 2*x + 3

plt.plot(x,y)

plt.title("Straight Line")

plt.xlabel("x")

plt.ylabel("y")

plt.grid(True)

plt.show()