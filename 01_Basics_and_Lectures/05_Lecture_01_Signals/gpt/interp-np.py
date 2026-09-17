import numpy as np

t = np.array([0, 1, 2, 3])

x = np.array([10, 20, 40, 30])

value = np.interp(
    1.5,  # Required time
    t,    # Known times
    x     # Known signal values
)

print(value)


