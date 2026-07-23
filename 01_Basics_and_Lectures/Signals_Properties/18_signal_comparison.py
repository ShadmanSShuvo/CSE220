import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)

plt.plot(t, np.sin(t), label="sin")
plt.plot(t, np.cos(t), label="cos")
plt.plot(t, np.exp(-t), label="exp")
plt.plot(t, t, label="ramp")

plt.legend()
plt.grid(True)
plt.show()
