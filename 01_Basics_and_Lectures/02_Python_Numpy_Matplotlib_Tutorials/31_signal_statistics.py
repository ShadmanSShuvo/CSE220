import numpy as np
import matplotlib.pyplot as plt

A = 2
f = 5
t = np.linspace(0, 2, 1000)
signal = A * np.sin(2 * np.pi * f * t)

print("Maximum =", np.max(signal))
print("Minimum =", np.min(signal))
print("Mean =", np.mean(signal))

rms = np.sqrt(np.mean(signal**2))
print("RMS =", rms)

plt.plot(t, signal)
plt.title("Sine Wave")
plt.grid(True)
plt.show()
