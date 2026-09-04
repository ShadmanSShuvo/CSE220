import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(
    -5,
    5,
    1000
)

x = np.exp(-t**2)


# Required input times
transformed_time = t - 2


# Calculate x(t - 2)
y = np.interp(
    transformed_time,
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
    y,
    label="x(t - 2)"
)

plt.grid(True)
plt.legend()

plt.show()