import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

# Define x(t)
def signal(t):
    return np.exp(-t) * (t >= 0)

# Calculate x(t) and x(-t)
x = signal(t)
x_negative = signal(-t)

# Even and odd decomposition
x_even = (x + x_negative) / 2
x_odd = (x - x_negative) / 2

# Plot
plt.plot(t, x, label="x(t)")
plt.plot(t, x_even, label="Even part")
plt.plot(t, x_odd, label="Odd part")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Even-Odd Decomposition")

plt.grid()
plt.legend()
plt.show()