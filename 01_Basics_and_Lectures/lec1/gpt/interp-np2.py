import numpy as np

t = np.array([0, 1, 2, 3])

x = np.array([10, 20, 40, 30])

query_times = np.array([
    0.5,
    1.5,
    2.5
])

values = np.interp(
    query_times,
    t,
    x
)

print(values)