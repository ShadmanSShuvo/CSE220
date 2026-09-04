import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
plt.plot(t, np.sin(t), label="sin(t)")
plt.plot(t, np.sin(2*t), label="sin(2t)")
plt.legend()
plt.grid(True)
plt.show()
