import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,300)

y = np.exp(x)

plt.plot(x,y)

plt.title("Exponential Function")

plt.xlabel("x")

plt.ylabel("exp(x)")

plt.grid()

plt.show()