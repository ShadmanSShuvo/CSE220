"""P06 - Time shift of a sampled signal via interpolation. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

T_MIN, T_MAX, N = -5.0, 5.0, 2001


def x_of_t(t):
    """Given: a triangular bump centred at 0, width 2 (localised so a shift
    is easy to see)."""
    y = 1.0 - np.abs(t)
    return np.where(np.abs(t) <= 1.0, y, 0.0)


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def shift_signal(t, x, t0):
    """Return y(t) = x(t - t0) sampled on the same grid t, using linear
    interpolation. Values outside the original support are 0.
    A positive t0 DELAYS the signal (moves it to the right)."""
    return np.interp(t-t0,t,x)


def main():
    t = np.linspace(T_MIN, T_MAX, N)
    x = x_of_t(t)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t, x, label="x(t)", lw=1.8)
    ax.plot(t, shift_signal(t, x, 2.0), label="x(t-2)  delay", lw=1.6)
    ax.plot(t, shift_signal(t, x, -2.0), label="x(t+2)  advance", lw=1.6)
    ax.set_title("Time shift by interpolation")
    ax.set_xlabel("t"); ax.set_ylabel("Amplitude")
    ax.grid(True, alpha=0.3); ax.legend()
    plt.show()
    # peak of x is at t=0; after delay by 2 the peak should be near t=2
    y = shift_signal(t, x, 2.0)
    assert abs(t[np.argmax(y)] - 2.0) < 0.05
    ya = shift_signal(t, x, -2.0)
    assert abs(t[np.argmax(ya)] + 2.0) < 0.05
    print("[P06] peak moves to t=+2 for a delay and t=-2 for an advance"
          "  -> passed.")


if __name__ == "__main__":
    main()
