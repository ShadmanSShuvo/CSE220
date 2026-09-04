import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

# Use an asymmetric signal so reversal is visible
def signal(t):
    return np.where(
        (0 <= t) & (t <= 2),
        2 - t,
        0
    )

x = signal(t)

# Replace t with -t
x_reversed = signal(-t)

plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")
plt.plot(t, x_reversed, label="x(-t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Time Reversal")

plt.grid(True)
plt.legend()
plt.show()