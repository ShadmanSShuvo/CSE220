import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2000)

def signal(t):
    return np.exp(-t**2)

t0 = 2

# Original
x = signal(t)

# Delay: shift right by 2
x_delay = signal(t - t0)

# Advance: shift left by 2
x_advance = signal(t + t0)

plt.figure(figsize=(10, 5))

plt.plot(t, x, label="x(t)")
plt.plot(t, x_delay, label="x(t - 2): right shift")
plt.plot(t, x_advance, label="x(t + 2): left shift")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Time Shifting")

plt.grid(True)
plt.legend()
plt.show()