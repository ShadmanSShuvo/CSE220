import numpy as np


def linear_interpolation(
    t,
    x,
    t_query
):

    # Ensure query is inside range
    if (
        t_query < t[0]
        or
        t_query > t[-1]
    ):

        return 0


    # Find right neighbor
    right_index = np.searchsorted(
        t,
        t_query
    )


    # Exact first sample
    if right_index == 0:

        return x[0]


    # Exact existing sample
    if (
        right_index < len(t)
        and
        t[right_index] == t_query
    ):

        return x[right_index]


    # Find left neighbor
    left_index = right_index - 1


    # Neighboring times
    t_left = t[left_index]

    t_right = t[right_index]


    # Neighboring signal values
    x_left = x[left_index]

    x_right = x[right_index]


    # Interpolation ratio
    ratio = (
        t_query - t_left
    ) / (
        t_right - t_left
    )


    # Linear interpolation
    return (
        (1 - ratio) * x_left
        +
        ratio * x_right
    )
    
    
t = np.array(
    [-3, -2, -1, 0, 1, 2, 3]
)

x = np.array(
    [2, 4, 6, 8, 10, 12, 14]
)

answer = linear_interpolation(
    t,
    x,
    -1.5
)

print(answer)