import numpy as np
import matplotlib.pyplot as plt


# Original sparse samples
t_old = np.arange(
    0,
    11,
    1
)

x_old = np.sin(t_old)


# New dense time axis
t_new = np.arange(
    0,
    10.1,
    0.1
)


# Resampled signal
x_new = np.interp(
    t_new,
    t_old,
    x_old
)


plt.scatter(
    t_old,
    x_old,
    label="Original samples"
)

plt.plot(
    t_new,
    x_new,
    color="orange",
    label="Interpolated samples"
)

plt.grid(True)
plt.legend()

plt.show()