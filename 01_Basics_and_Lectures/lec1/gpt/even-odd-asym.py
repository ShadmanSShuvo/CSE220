import numpy as np
import matplotlib.pyplot as plt

# Asymmetric time axis
t = np.linspace(-2, 5, 1000)

# Define x(t) as a function
def signal(t):
    return np.exp(-t) * (t >= 0)

# Evaluate the function at t and -t
x_t = signal(t)
x_negative_t = signal(-t)

# Even part
x_even = (x_t + x_negative_t) / 2

# Odd part
x_odd = (x_t - x_negative_t) / 2

# Verify reconstruction
x_reconstructed = x_even + x_odd


# Plot
plt.figure(figsize=(10, 8))


# Original signal
plt.subplot(2, 2, 1)

plt.plot(t, x_t)

plt.title("Original Signal: x(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True)


# Even part
plt.subplot(2, 2, 2)

plt.plot(t, x_even)

plt.title("Even Part")
plt.xlabel("t")
plt.ylabel("Amplitude")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True)


# Odd part
plt.subplot(2, 2, 3)

plt.plot(t, x_odd)

plt.title("Odd Part")
plt.xlabel("t")
plt.ylabel("Amplitude")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True)


# Reconstruction
plt.subplot(2, 2, 4)

plt.plot(
    t,
    x_t,
    label="Original x(t)"
)

plt.plot(
    t,
    x_reconstructed,
    "--",
    label="x_even + x_odd"
)

plt.title("Reconstruction")
plt.xlabel("t")
plt.ylabel("Amplitude")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()