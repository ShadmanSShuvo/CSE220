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
    dt=t_original[1]-t_original[0]
    float_indices=(t_query-t_original[0])/dt
    left=np.floor(float_indices).astype(int)
    right=np.ceil(float_indices).astype(int)
    max_idx=len(x_original)-1
    left = np.clip(left, 0, max_idx)
    right = np.clip(right, 0, max_idx)

    y=0.5*(x_original[left]+x_original[right])

    return y


def time_scale(
    t: np.ndarray,
    x: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Time sub-scaling:
        y(t) = x(t / k)
    """
    t_query=t/k
    y=interpolate_signal(t,x,t_query)
    return y


def plot_pair(t: np.ndarray, x: np.ndarray, y: np.ndarray, title: str, figsize=(8, 6)):
    """
    Plot graphs.
    """
    fig,axes=plt.subplots(2,1,figsize=figsize)

    axes[0].plot(t,x)
    axes[1].plot(t,y)
    fig.suptitle(title)
    plt.tight_layout()


# ----------------------------
# Main
# ----------------------------
def main():
    t = np.linspace(T_MIN, T_MAX, N)
    x = x_of_t(t)

    k = 2   # sub-scaling factor
    y = time_scale(t, x, k)

    plot_pair(
        t,
        x,
        y,
        title=f"Time Sub-scaling: y(t) = x(t / {k})"
    )
    plt.show()


if __name__ == "__main__":
    main()
