import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
u = np.where(t >= 0, 1, 0)

plt.plot(t, u)
plt.title("Unit Step Signal")
plt.grid(True)
plt.show()
