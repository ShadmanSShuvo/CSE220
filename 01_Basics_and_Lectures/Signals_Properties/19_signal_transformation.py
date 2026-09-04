import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
x = np.sin(t)

plt.figure(figsize=(10, 6))
plt.plot(t, x, label="x(t)")
plt.plot(t, np.sin(t-2), label="x(t-2)")
plt.plot(t, np.sin(2*t), label="x(2t)")
plt.plot(t, 2*np.sin(t), label="2x(t)")
plt.plot(t, np.sin(-t), label="x(-t)")

plt.title("Signal Transformations")
plt.legend()
plt.grid(True)
plt.show()
