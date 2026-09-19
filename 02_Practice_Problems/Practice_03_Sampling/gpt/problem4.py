"""
Problem 4: Aliasing Frequency Calculator
========================================

Problem Statement:
------------------
Write a Python function:
    def alias_frequency(f, fs):
        ...

that returns the frequency observed after sampling a sinusoid of frequency f
at sampling frequency fs.

Test it for:
    |      f |     fs |
    |  35 Hz |  50 Hz |
    |  60 Hz | 100 Hz |
    |  75 Hz | 100 Hz |
    | 125 Hz | 100 Hz |
    | 230 Hz | 100 Hz |

Plot the original frequency and corresponding alias frequency.
"""

import numpy as np
import matplotlib.pyplot as plt


def alias_frequency(f, fs):
    """
    Calculates the apparent/observed frequency in [0, fs/2] when a sinusoid
    of frequency f is sampled at rate fs.

    Parameters:
        f  : float or array_like, original signal frequency (Hz)
        fs : float, sampling frequency (Hz)

    Returns:
        f_alias : float or ndarray, observed frequency in range [0, fs/2]
    """
    f = np.asarray(f, dtype=float)
    # The discrete-time frequency is folded into the baseband [0, fs/2].
    # Analytical formula: |f - fs * round(f / fs)|
    return np.abs(f - fs * np.round(f / fs))


def solve_problem4():
    # Test cases from problem statement
    test_cases = [
        (35, 50),
        (60, 100),
        (75, 100),
        (125, 100),
        (230, 100),
    ]

    print("=" * 60)
    print("CSE220 Lab — Problem 4: Aliasing Frequency Calculator")
    print("=" * 60)
    print(f"{'f (Hz)':>10} | {'fs (Hz)':>10} | {'Alias Frequency (Hz)':>22} | {'Aliased?':>10}")
    print("-" * 60)

    results = []
    for f, fs in test_cases:
        fa = alias_frequency(f, fs)
        is_aliased = "YES" if (f > fs / 2) else "NO"
        results.append((f, fs, fa, is_aliased))
        print(f"{f:>10.1f} | {fs:>10.1f} | {fa:>22.1f} | {is_aliased:>10}")
    print("=" * 60)

    # Plotting:
    # 1. Comparison bar chart of (f vs f_alias) for all test cases
    # 2. Continuous folding curve for fs = 100 Hz showing triangular folding pattern
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Subplot 1: Bar chart comparison
    labels = [f"f={f}\nfs={fs}" for f, fs in test_cases]
    f_origs = [f for f, fs in test_cases]
    f_aliases = [fa for f, fs, fa, _ in results]

    x_indices = np.arange(len(test_cases))
    width = 0.35

    ax1.bar(x_indices - width / 2, f_origs, width, label="Original Frequency (f)", color="steelblue")
    ax1.bar(x_indices + width / 2, f_aliases, width, label="Observed Alias (fa)", color="coral")

    for i in range(len(test_cases)):
        ax1.text(x_indices[i] - width / 2, f_origs[i] + 3, f"{f_origs[i]}", ha="center", fontsize=9)
        ax1.text(x_indices[i] + width / 2, f_aliases[i] + 3, f"{f_aliases[i]:.0f}", ha="center", fontsize=9, fontweight="bold")

    ax1.set_xticks(x_indices)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("Frequency (Hz)")
    ax1.set_title("Test Cases: Original vs Observed Frequency")
    ax1.legend()
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Subplot 2: Continuous folding diagram for fs = 100 Hz
    fs_ref = 100.0
    f_range = np.linspace(0, 300, 1000)
    fa_curve = alias_frequency(f_range, fs_ref)

    ax2.plot(f_range, fa_curve, label=f"Folding Curve (fs = {int(fs_ref)} Hz)", color="teal", lw=2)
    ax2.axhline(fs_ref / 2, color="red", linestyle="--", alpha=0.7, label=f"Nyquist Limit (fs/2 = {int(fs_ref/2)} Hz)")

    # Mark the fs=100 test cases on the curve
    cases_100 = [(f, fa) for f, fs, fa, _ in results if fs == fs_ref]
    for f_pt, fa_pt in cases_100:
        ax2.scatter(f_pt, fa_pt, color="red", s=60, zorder=5)
        ax2.annotate(
            f"({f_pt} -> {fa_pt:.0f} Hz)",
            xy=(f_pt, fa_pt),
            xytext=(f_pt - 15, fa_pt + 4),
            fontsize=8,
            arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
        )

    ax2.set_xlabel("Original Frequency f (Hz)")
    ax2.set_ylabel("Observed Frequency fa (Hz)")
    ax2.set_title("Frequency Folding Triangle Waveform (fs = 100 Hz)")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem4()
