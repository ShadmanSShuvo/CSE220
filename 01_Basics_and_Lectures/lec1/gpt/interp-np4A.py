import numpy as np
import matplotlib.pyplot as plt

# Original time points
t = np.linspace(
    -2,
    2,
    100
)


# Original sampled signal
x = np.exp(-t**2)


# For y(t) = x(2t),
# query the original signal at 2t

required_times = 2 * t


# Interpolate
y = np.interp(
    required_times,
    t,
    x
)


# Plot
plt.plot(
    t,
    x,
    label="x(t)"
)

plt.plot(
    t,
    y,
    label="x(2t)"
)

plt.axhline(
    0,
    color="black"
)

plt.axvline(
    0,
    color="black"
)

plt.xlabel("t")
plt.ylabel("Amplitude")

plt.title(
    "Time Compression"
)

plt.grid(True)
plt.legend()

plt.show()