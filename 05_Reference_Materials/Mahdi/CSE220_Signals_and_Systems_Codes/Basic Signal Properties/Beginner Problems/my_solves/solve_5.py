"""P05 - Discrete-time building blocks. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def unit_impulse(n):
    """delta[n] = 1 at n==0, else 0."""
    x = np.zeros_like(n)
    m1 = n==0
    x[m1]=1
    return x


def unit_step(n):
    """u[n] = 1 for n >= 0, else 0."""
    x = np.zeros_like(n)
    m1 = n>=0
    x[m1]=1
    return x


def rect_pulse_dt(n, N):
    """Rectangular pulse: 1 for 0 <= n < N, else 0. Build as u[n] - u[n-N]."""
    x = np.zeros_like(n)
    m1 = (n>=0) & (n<N)
    x[m1]=1
    return x


def stem(ax, n, x, title):
    ml, sl, bl = ax.stem(n, x)
    bl.set_visible(False)
    ax.set_title(title); ax.set_xlabel("n"); ax.grid(True, alpha=0.3)


def main():
    n = np.arange(-10, 11)
    fig, axs = plt.subplots(3, 1, figsize=(9, 7))
    stem(axs[0], n, unit_impulse(n), "unit impulse  delta[n]")
    stem(axs[1], n, unit_step(n), "unit step  u[n]")
    stem(axs[2], n, rect_pulse_dt(n, 5), "rect pulse (N=5)  u[n]-u[n-5]")
    plt.show()
    assert unit_impulse(n).sum() == 1.0
    assert unit_step(np.array([-1, 0, 3])).tolist() == [0.0, 1.0, 1.0]
    assert rect_pulse_dt(n, 5).sum() == 5.0    # ones at n=0..4
    print("[P05] impulse sums to 1, step correct, rect has 5 ones  -> passed.")


if __name__ == "__main__":
    main()
