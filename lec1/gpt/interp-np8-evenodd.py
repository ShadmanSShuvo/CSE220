import numpy as np
import matplotlib.pyplot as plt


# Asymmetric time axis
t = np.linspace(
    -2,
    5,
    1000
)


# Original signal samples
x = (
    np.exp(-t)
    * (t >= 0)
)


# Estimate x(-t)
x_negative = np.interp(
    -t,
    t,
    x,
    left=0,
    right=0
)


# Even part
x_even = (
    x + x_negative
) / 2


# Odd part
x_odd = (
    x - x_negative
) / 2


# Plot
plt.plot(
    t,
    x,
    label="x(t)"
)

plt.plot(
    t,
    x_even,
    label="Even part"
)

plt.plot(
    t,
    x_odd,
    label="Odd part"
)

plt.axhline(
    0,
    color="black"
)

plt.axvline(
    0,
    color="black"
)

plt.grid(True)
plt.legend()

plt.show()