import numpy as np
import matplotlib.pyplot as plt

# Time axis
t = np.linspace(-5, 5, 1000)

# Define x(t)
def signal(t):
    return np.sin(t)

# Calculate signal values
x = signal(t)

# Plot
plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.title("Continuous-Time Signal")
plt.xlabel("Time, t")
plt.ylabel("Amplitude")

plt.grid(True)
plt.legend()
plt.show()