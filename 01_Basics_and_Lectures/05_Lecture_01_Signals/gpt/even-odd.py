import numpy as np
import matplotlib.pyplot as plt

# Symmetric time axis is important
t = np.linspace(-5, 5, 1000)

# Define the original signal
def signal(t):
    return np.exp(-t) * (t >= 0)

# Original and reversed signals
x = signal(t)
x_reversed = signal(-t)

# Even part
x_even = (x + x_reversed) / 2

# Odd part
x_odd = (x - x_reversed) / 2

# Reconstruction
x_reconstructed = x_even + x_odd

# Plot
plt.figure(figsize=(10, 8))

# Original
plt.subplot(2, 2, 1)
plt.plot(t, x)
plt.title("Original Signal: x(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)

# Even part
plt.subplot(2, 2, 2)
plt.plot(t, x_even)
plt.title("Even Part")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)

# Odd part
plt.subplot(2, 2, 3)
plt.plot(t, x_odd)
plt.title("Odd Part")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)

# Reconstruction
plt.subplot(2, 2, 4)
plt.plot(t, x, label="x(t)")
plt.plot(
    t,
    x_reconstructed,
    "--",
    label="x_even + x_odd"
)

plt.title("Verification")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()