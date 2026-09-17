import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

def signal(t):
    return np.sin(t)

A = 2

x = signal(t)
y = A * signal(t)

plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")
plt.plot(t, y, label=f"{A}x(t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.title("Amplitude Scaling")
plt.xlabel("Time, t")
plt.ylabel("Amplitude")

plt.grid(True)
plt.legend()
plt.show()