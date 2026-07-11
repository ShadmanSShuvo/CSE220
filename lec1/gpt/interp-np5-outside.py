import numpy as np

t = np.array([
    0, 1, 2, 3
])

x = np.array([
    10, 20, 40, 30
])

query_times = np.array([
    -2,
    1.5,
    5
])

values = np.interp(
    query_times,
    t,
    x
)

print(values)

# if we want 0 outside the range, we can use the left and right parameters
values_with_bounds = np.interp(
    query_times,
    t,
    x,
    left=0,
    right=0
)

print(values_with_bounds)

"""
values = np.interp(
    query_times,
    t,
    x,
    left=0,
    right=0
)


y = np.interp(
    transformed_time,
    original_time,
    original_signal,
    left=0,
    right=0
)
"""
