import numpy as np

def interpolate_signal(t, x, t_query):

    # Find nearest left index
    left_index = int(
        np.floor(t_query)
    )

    # Find nearest right index
    right_index = int(
        np.ceil(t_query)
    )


    # Exact sample exists
    if left_index == right_index:

        return x[left_index]


    # Neighboring times
    t_left = t[left_index]

    t_right = t[right_index]


    # Neighboring values
    x_left = x[left_index]

    x_right = x[right_index]


    # Relative position
    ratio = (
        t_query - t_left
    ) / (
        t_right - t_left
    )


    # Interpolated value
    return (
        x_left
        + ratio
        * (
            x_right
            - x_left
        )
    )