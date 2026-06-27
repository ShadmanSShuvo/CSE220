import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
r = np.where(t >= 0, t, 0)

plt.plot(t, r)
plt.title("Ramp Signal")
plt.grid(True)
plt.show()
