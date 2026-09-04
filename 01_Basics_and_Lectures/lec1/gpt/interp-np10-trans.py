import numpy as np
import matplotlib.pyplot as plt
alpha = -3

beta = 2

t = np.array([
    -2,
    -1,
    0,
    1,
    2
])

x = np.array([
    0,
    1,
    2,
    1,
    0
])

required_times = (
    alpha * t
    + beta
)


y = np.interp(
    required_times,
    t,
    x,
    left=0,
    right=0
)

transformed_time = (
    alpha * t
    + beta
)

# y = np.interp(
#     transformed_time,
#     t,
#     x,
#     left=0,
#     right=0
# )

plt.plot(
    t,
    x,
    label="x(t)"
)

plt.plot(
    t,
    y,
    label=f"x({alpha}t + {beta})"   
)
plt.show()