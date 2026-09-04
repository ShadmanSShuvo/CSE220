import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
signal = np.sin(2 * np.pi * 5 * t)
noise = 0.3 * np.random.randn(len(t))
noisy = signal + noise

plt.plot(t, signal, label="Original")
plt.plot(t, noisy, label="Noisy")
plt.legend()
plt.title("Original vs Noisy Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
