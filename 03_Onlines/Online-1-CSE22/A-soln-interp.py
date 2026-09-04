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
    Interpolate signal values at queried time points
    using NumPy linear interpolation.
    """

    return np.interp(
        t_query,
        t_original,
        x_original
    )


def time_scale(
    t: np.ndarray,
    x: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Time sub-scaling:
        y(t) = x(t / k)
    """

    if k <= 0:
        raise ValueError(
            "k must be a positive integer"
        )

    # Find corresponding original time values
    t_query = t / k

    # Interpolate x(t / k)
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
    Plot x(t) and y(t) on same figure.
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

    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")

    plt.title(title)

    plt.legend()
    plt.grid(True)

    plt.tight_layout()


# ----------------------------
# Main
# ----------------------------
def main():

    # Generate time samples
    t = np.linspace(
        T_MIN,
        T_MAX,
        N
    )

    # Generate original signal
    x = x_of_t(t)

    # Time sub-scaling factor
    k = 2

    # Calculate y(t) = x(t / k)
    y = time_scale(
        t,
        x,
        k
    )

    # Plot both signals
    plot_pair(
        t,
        x,
        y,
        title=f"Time Sub-scaling: y(t) = x(t / {k})"
    )

    plt.show()


if __name__ == "__main__":
    main()
