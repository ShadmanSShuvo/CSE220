import numpy as np

# Known samples
t = np.array([0, 1, 2, 3, 4])

x = np.array([10, 20, 40, 30, 50])

# Required time
t_query = 1.6


# Find neighboring indices
left_index = int(
    np.floor(t_query)
)

right_index = int(
    np.ceil(t_query)
)


# Get neighboring times
t_left = t[left_index]

t_right = t[right_index]


# Get neighboring signal values
x_left = x[left_index]

x_right = x[right_index]


# Calculate interpolation ratio
ratio = (
    t_query - t_left
) / (
    t_right - t_left
)


# Linear interpolation
x_query = (
    x_left
    + ratio
    * (x_right - x_left)
)


print("Left index:", left_index)

print("Right index:", right_index)

print("Interpolation ratio:", ratio)

print("Interpolated value:", x_query)