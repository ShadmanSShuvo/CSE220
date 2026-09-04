"""P04 - Adding and multiplying signals. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

T_MIN, T_MAX, N = 0.0, 1.0, 2000


def x1_of_t(t):  # given: slow cosine
    return np.cos(2 * np.pi * 3 * t)


def x2_of_t(t):  # given: fast cosine
    return np.cos(2 * np.pi * 20 * t)


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def add_signals(a, b):
    """Elementwise sum of two signals."""
    return a+b 


def multiply_signals(a, b):
    """Elementwise product of two signals."""
    return a*b


def main():
    t = np.linspace(T_MIN, T_MAX, N)
    x1, x2 = x1_of_t(t), x2_of_t(t)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))
    ax1.plot(t, x1, label="x1 (3 Hz)")
    ax1.plot(t, x2, label="x2 (20 Hz)", alpha=0.6)
    ax1.plot(t, add_signals(x1, x2), label="x1 + x2", color="k", lw=1.2)
    ax1.set_title("Sum of two signals"); ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3); ax1.set_xlabel("t")

    ax2.plot(t, multiply_signals(x1, x2), color="C3")
    ax2.plot(t, x1, "k--", alpha=0.5, label="x1 (envelope)")
    ax2.plot(t, -x1, "k--", alpha=0.5)
    ax2.set_title("Product of two signals (amplitude modulation)")
    ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3); ax2.set_xlabel("t")
    plt.show()
    assert np.allclose(add_signals(x1, x2), x1 + x2)
    assert np.allclose(multiply_signals(x1, x2), x1 * x2)
    print("[P04] sum and product computed; product rides inside the x1 envelope"
          "  -> passed.")


if __name__ == "__main__":
    main()
