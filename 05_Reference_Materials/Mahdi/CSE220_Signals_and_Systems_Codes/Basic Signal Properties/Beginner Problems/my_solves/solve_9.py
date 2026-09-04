"""P09 - Average power of a periodic discrete-time signal. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

N0 = 8   # fundamental period


def x_of_n(n):
    """Given: a periodic cosine with period N0 = 8."""
    return np.cos(2 * np.pi * n / N0)


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def average_power_one_period(x_period):
    """Average power over exactly one period:  (1/N0) * sum |x|^2."""
    return float(np.mean(np.abs(x_period) ** 2))


def average_power(x):
    """Average power over the whole array:  mean of |x|^2."""
    return np.mean(np.abs(x)**2)


def main():
    n_one = np.arange(0, N0)               # one period
    n_many = np.arange(0, 5 * N0)          # five periods

    p1 = average_power_one_period(x_of_n(n_one))
    pK = average_power(x_of_n(n_many))
    print(f"[P09] power over 1 period  = {p1:.6f}")
    print(f"[P09] power over 5 periods = {pK:.6f}")
    print(f"[P09] exact value for a cosine = 0.5")

    fig, ax = plt.subplots(figsize=(9, 3.6))
    ml, sl, bl = ax.stem(n_many, x_of_n(n_many)); bl.set_visible(False)
    ax.axvspan(0, N0 - 1, color="orange", alpha=0.15, label="one period")
    ax.set_title("Periodic cosine (period N0=8)")
    ax.set_xlabel("n"); ax.grid(True, alpha=0.3); ax.legend(fontsize=8)
    plt.show()
    assert np.isclose(p1, pK)          # one period is enough
    assert np.isclose(p1, 0.5)         # matches the exact cosine power
    print("[P09] one-period power equals full power equals 0.5  -> passed.")


if __name__ == "__main__":
    main()
