# This file is the solution
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

    dt = t_original[1]-t_original[0]

    idx = (t_query - t_original[0])/dt 

    idx_left = np.floor(idx).astype(int)
    idx_right = np.ceil(idx).astype(int)

    idx_left = np.clip(idx_left,0,len(t_original)-1)
    idx_right = np.clip(idx_right,0,len(t_original)-1)

    return 0.5*(x_original[idx_left]+x_original[idx_right])

    #return np.interp(t_query,t_original,x_original,left=0.0,right = 0.0)


def time_scale(
    t: np.ndarray,
    x: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Time sub-scaling:
        y(t) = x(t / k)
    """
    return interpolate_signal(t,x,t/k)


def plot_pair(t: np.ndarray, x: np.ndarray, y: np.ndarray, title: str):
    """
    Plot graphs.
    """
    plt.plot(t,x, color = 'blue', label = 'x(t)')
    plt.plot(t,y,color = 'red',label = 'y(t)')
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.6)
    plt.xlabel("Time")
    plt.ylabel("signal")


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
