# sine & cosine
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(t, np.sin(t))
plt.title("Sine")

plt.subplot(2, 1, 2)
plt.plot(t, np.cos(t))
plt.title("Cosine")

plt.tight_layout()
plt.show()
