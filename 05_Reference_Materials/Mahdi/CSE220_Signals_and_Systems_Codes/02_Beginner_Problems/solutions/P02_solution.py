"""P02 - Amplitude scaling and DC offset  y = A*x + B. Reference solution."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

T_MIN, T_MAX, N = 0.0, 2.0, 1000


def x_of_t(t):
    """Base signal (given): a 1 Hz sine."""
    return np.sin(2 * np.pi * 1.0 * t)


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def amplitude_scale(x, A):
    """Multiply every sample by A."""
    return A * x


def add_offset(x, B):
    """Add the constant B to every sample (a DC offset)."""
    return x + B


def transform(x, A, B):
    """Combined amplitude scaling and offset: A*x + B."""
    return add_offset(amplitude_scale(x, A), B)


def main():
    t = np.linspace(T_MIN, T_MAX, N)
    x = x_of_t(t)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t, x, label="x(t)")
    ax.plot(t, amplitude_scale(x, 2.0), label="2x(t)")
    ax.plot(t, add_offset(x, 1.0), label="x(t)+1")
    ax.plot(t, transform(x, 2.0, 1.0), label="2x(t)+1")
    ax.set_title("Amplitude scaling and DC offset")
    ax.set_xlabel("t"); ax.set_ylabel("Amplitude")
    ax.grid(True, alpha=0.3); ax.legend()
    plt.show()

    assert np.allclose(transform(x, 2.0, 1.0), 2 * x + 1)
    assert np.isclose(add_offset(x, 1.0).mean(), 1.0, atol=1e-2)  # mean of sine ~0 +1
    print("[P02] transform matches 2x+1; offset raises the mean to ~1  -> passed.")


if __name__ == "__main__":
    main()
