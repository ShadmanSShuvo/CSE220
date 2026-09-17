import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2000)

def signal(t):
    return np.exp(-t**2)

x = signal(t)

# x(2t): compressed
x_compressed = signal(2 * t)

# x(t/2): expanded
x_expanded = signal(t / 2)

plt.figure(figsize=(10, 5))

plt.plot(t, x, label="x(t)")
plt.plot(t, x_compressed, label="x(2t): compressed")
plt.plot(t, x_expanded, label="x(t/2): expanded")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Time Scaling")

plt.grid(True)
plt.legend()
plt.show()