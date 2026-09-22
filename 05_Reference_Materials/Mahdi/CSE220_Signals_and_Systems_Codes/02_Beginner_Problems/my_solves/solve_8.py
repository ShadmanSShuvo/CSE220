"""P08 - Energy of a discrete-time signal. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def pulse(n):
    """Given: a 5-sample rectangular pulse of height 2 (finite energy)."""
    return np.where((n >= 0) & (n < 5), 2.0, 0.0)


def decay(n):
    """Given: a decaying exponential (0.8)^n u[n], truncated to n>=0."""
    return np.where(n >= 0, 0.8 ** n, 0.0)


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def energy_dt(x):
    """Total energy of a discrete-time signal:  sum of |x[n]|^2."""
    # s=0
    # for val in x:
    #     s+=abs(val)**2
    # return s
    return float(np.sum(np.abs(x)**2))


def cumulative_energy(x):
    """Running energy: element k is the energy of x[0..k]."""
    return np.cumsum(np.abs(x)**2)


def main():
    n = np.arange(0, 40)
    xp, xd = pulse(n), decay(n)

    Ep, Ed = energy_dt(xp), energy_dt(xd)
    print(f"[P08] pulse energy   = {Ep:.4f}  (exact 5*2^2 = 20)")
    print(f"[P08] decay energy   = {Ed:.4f}  (exact 1/(1-0.64) = {1/(1-0.64):.4f})")

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(n, cumulative_energy(xp), "o-", label="rect pulse", ms=3)
    ax.plot(n, cumulative_energy(xd), "s-", label="decaying exp", ms=3)
    ax.set_title("Cumulative energy"); ax.set_xlabel("n")
    ax.set_ylabel("energy up to n"); ax.grid(True, alpha=0.3); ax.legend()
    plt.show()
    assert np.isclose(Ep, 20.0)
    assert np.isclose(Ed, 1 / (1 - 0.64), atol=1e-3)
    print("[P08] energies match the exact values  -> passed.")


if __name__ == "__main__":
    main()
