import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(
    -2,
    5,
    1000
)


# Asymmetric signal
x = (
    np.exp(-t)
    * (t >= 0)
)


# Calculate x(-t)
x_reversed = np.interp(
    -t,
    t,
    x,
    left=0,
    right=0
)


plt.plot(
    t,
    x,
    label="x(t)"
)

plt.plot(
    t,
    x_reversed,
    label="x(-t)"
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