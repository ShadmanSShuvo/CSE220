import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Time axis
# ----------------------------
T_MIN, T_MAX, N = -4.0, 4.0, 4001


def x_of_t(t: np.ndarray) -> np.ndarray:
    """
    Base signal x(t): sinusoidal signal
    """
    return (
        np.sin(2 * np.pi * 0.5 * t)
        + 0.5 * np.sin(2 * np.pi * 1.5 * t)
    )


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================

def interpolate_signal(
    t_original: np.ndarray,
    x_original: np.ndarray,
    t_query: np.ndarray
) -> np.ndarray:
    """
    Interpolate using average of two neighboring samples.
    """

    result = np.empty_like(t_query, dtype=float)

    # Find nearest sample on right
    right_indices = np.searchsorted(
        t_original,
        t_query
    )

    # Keep indices valid
    right_indices = np.clip(
        right_indices,
        0,
        len(t_original) - 1
    )

    # Detect already available samples
    exact_match = np.isclose(
        t_original[right_indices],
        t_query
    )

    # Copy exact values
    result[exact_match] = x_original[
        right_indices[exact_match]
    ]

    # Interpolate missing samples
    non_exact = ~exact_match

    left_indices = right_indices - 1

    result[non_exact] = 0.5 * (
        x_original[left_indices[non_exact]]
        + x_original[right_indices[non_exact]]
    )

    return result


def time_scale(
    t: np.ndarray,
    x: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Time sub-scaling:
        y(t) = x(t / k)
    """

    if not isinstance(k, int) or k <= 0:
        raise ValueError(
            "k must be a positive integer"
        )

    # Required original signal times
    t_query = t / k

    # Find corresponding signal values
    y = interpolate_signal(
        t,
        x,
        t_query
    )

    return y


def plot_pair(
    t: np.ndarray,
    x: np.ndarray,
    y: np.ndarray,
    title: str
):
    """
    Plot graphs.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        t,
        x,
        label="x(t)"
    )

    plt.plot(
        t,
        y,
        label="y(t) = x(t / k)"
    )
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")

    plt.title(title)

    plt.grid(True)
    plt.legend()

    plt.tight_layout()


# ----------------------------
# Main
# ----------------------------
def main():

    t = np.linspace(
        T_MIN,
        T_MAX,
        N
    )

    x = x_of_t(t)

    k = 4

    y = time_scale(
        t,
        x,
        k
    )

    plot_pair(
        t,
        x,
        y,
        title=f"Time Sub-scaling: y(t) = x(t / {k})"
    )

    plt.show()


if __name__ == "__main__":
    main()