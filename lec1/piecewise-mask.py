import numpy as np
import matplotlib.pyplot as plt


def piecewise_continuous_signal(t):
    """
    x(t) = 1      for 0 <= t < 1
    x(t) = 2 - t  for 1 <= t <= 2
    x(t) = 0      otherwise
    """

    t = np.asarray(t)

    # Default value: zero
    x = np.zeros_like(
        t,
        dtype=float
    )

    # Boolean masks
    mask1 = (
        (t >= 0)
        &
        (t < 1)
    )

    mask2 = (
        (t >= 1)
        &
        (t <= 2)
    )

    # Apply piecewise equations
    x[mask1] = 1

    x[mask2] = (
        2 - t[mask2]
    )

    return x


# Generate time values
t = np.linspace(
    -1,
    3,
    1000
)


# Calculate x(t)
x = piecewise_continuous_signal(t)


# Plot
plt.figure(
    figsize=(8, 4)
)

plt.plot(
    t,
    x,
    label="x(t)"
)

plt.axhline(
    0,
    color="black",
    linewidth=0.8
)

plt.axvline(
    0,
    color="black",
    linewidth=0.8
)

plt.xlabel("Time, t")

plt.ylabel(
    "Amplitude, x(t)"
)

plt.title(
    "Piecewise Continuous Signal"
)

plt.grid(True)

plt.legend()

plt.show()