"""P01 - Generating and plotting basic signals. Reference solution."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def make_sine(t, A, f, phi):
    """A sine wave: A * sin(2*pi*f*t + phi)."""
    return A * np.sin(2 * np.pi * f * t + phi)


def make_cosine(t, A, f, phi):
    """A cosine wave: A * cos(2*pi*f*t + phi)."""
    return A * np.cos(2 * np.pi * f * t + phi)


def make_exp(t, A, a):
    """An exponential: A * exp(a*t)  (decaying when a < 0)."""
    return A * np.exp(a * t)


def plot_signals(t, signals, title):
    """signals is a dict {label: array}. Plot each on one figure."""
    fig, ax = plt.subplots(figsize=(9, 4))
    for label, y in signals.items():
        ax.plot(t, y, label=label, lw=1.6)
    ax.set_title(title); ax.set_xlabel("t"); ax.set_ylabel("Amplitude")
    ax.grid(True, alpha=0.3); ax.legend()
    plt.show()


def main():
    t = np.linspace(0, 2, 1000)
    s = make_sine(t, A=1.0, f=2.0, phi=0.0)
    c = make_cosine(t, A=1.0, f=1.0, phi=0.0)
    e = make_exp(t, A=1.0, a=-1.0)
    plot_signals(t, {"sin 2Hz": s, "cos 1Hz": c, "exp(-t)": e},
                 "Basic signals")

    # self-checks
    assert np.isclose(make_sine(np.array([0.0]), 1, 2, 0)[0], 0.0)
    assert np.isclose(make_cosine(np.array([0.0]), 1, 1, 0)[0], 1.0)
    assert np.isclose(make_exp(np.array([0.0]), 3, -1)[0], 3.0)
    print("[P01] sin(0)=0, cos(0)=1, exp(0)*3=3  -> all checks passed.")


if __name__ == "__main__":
    main()
