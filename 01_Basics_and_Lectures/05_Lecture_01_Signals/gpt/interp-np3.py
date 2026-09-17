import numpy as np
import matplotlib.pyplot as plt

# Original samples
t_original = np.array([
    0, 1, 2, 3, 4
])

x_original = np.array([
    0, 2, 1, 4, 2
])


# Create a denser time axis
t_new = np.linspace(
    0,
    4,
    500
)


# Interpolate signal values
x_new = np.interp(
    t_new,
    t_original,
    x_original
)


# Plot interpolated signal
plt.plot(
    t_new,
    x_new,
    label="Interpolated signal"
)


# Show original samples
plt.scatter(
    t_original,
    x_original,
    label="Original samples"
)


plt.xlabel("Time, t")
plt.ylabel("Amplitude")

plt.title(
    "Signal Interpolation"
)

plt.grid(True)
plt.legend()

plt.show()