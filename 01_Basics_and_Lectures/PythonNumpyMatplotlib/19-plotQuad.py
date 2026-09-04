import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,200)

y = x**2

plt.plot(x,y)

plt.title("Quadratic Function")

plt.xlabel("x")

plt.ylabel("y")

plt.grid()

plt.show()