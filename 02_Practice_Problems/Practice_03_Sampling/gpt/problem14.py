"""
Problem 14: Reverse Engineering an Aliased Signal
=================================================

Problem Statement:
------------------
You observe a sampled signal whose apparent frequency is 12 Hz, sampled at:
    f_s = 40 Hz.

Tasks:
------
1. Find possible original frequencies in the range:
       0 < f < 100 Hz
   that could produce the observed 12-Hz component.
2. Write a program that generates all possible frequencies.
"""

import numpy as np
import matplotlib.pyplot as plt


def observed_alias(f, fs):
    """Calculates observed apparent frequency in [0, fs/2]."""
    return np.abs(f - fs * np.round(f / fs))


def find_possible_original_frequencies(fa, fs, f_min=0.0, f_max=100.0):
    """
    Finds all frequencies f in (f_min, f_max) such that
    f = k * fs +/- fa for integer k.
    """
    candidates = set()
    # Determine maximum k needed
    k_max = int(np.ceil((f_max + fa) / fs)) + 1

    for k in range(k_max + 1):
        for sign in [-1, 1]:
            f_cand = k * fs + sign * fa
            if f_min < f_cand < f_max:
                candidates.add(round(f_cand, 6))

    return sorted(list(candidates))


def solve_problem14():
    fa = 12.0  # Apparent frequency in Hz
    fs = 40.0  # Sampling frequency in Hz
    fn = fs / 2.0  # Nyquist frequency = 20 Hz
    f_min, f_max = 0.0, 100.0

    print("=" * 75)
    print("CSE220 Lab — Problem 14: Reverse Engineering an Aliased Signal")
    print("=" * 75)
    print(f"Observed Apparent Frequency (fa): {fa} Hz")
    print(f"Sampling Frequency (fs):          {fs} Hz (Nyquist limit fn = {fn} Hz)")
    print(f"Search Interval:                  {f_min} < f < {f_max} Hz\n")

    # Analytical Formula
    print("--- Analytical Derivation ---")
    print("When sampling at fs, any frequency f satisfying:")
    print("      f = k * fs +/- fa    (for integer k >= 0)")
    print("will produce the identical discrete sequence cos(2*pi * fa * n * Ts).\n")
    print("Evaluating for k = 0, 1, 2, ... within range (0, 100) Hz:")

    possible_freqs = find_possible_original_frequencies(fa, fs, f_min, f_max)

    for f_cand in possible_freqs:
        # Determine k and sign
        k = round(f_cand / fs)
        actual_observed = observed_alias(f_cand, fs)
        diff = f_cand - k * fs
        sign_str = "+" if diff >= 0 else "-"
        print(
            f"  * f = {f_cand:5.1f} Hz  =  {k} * {fs:.0f} {sign_str} {abs(diff):.0f} Hz  "
            f"-> Observed: {actual_observed:.1f} Hz"
        )

    print(f"\nTotal possible frequencies found: {len(possible_freqs)}")
    print(f"Frequencies: {possible_freqs} Hz\n")

    # Experimental Demonstration:
    # All 5 sinusoids evaluated at t = n * Ts = n / 40 produce the EXACT same values!
    Ts = 1.0 / fs
    n_pts = 6
    sample_indices = np.arange(n_pts)
    sample_times = sample_indices * Ts

    print("--- Verification: Sample Values at t = n / 40 s ---")
    header = f"{'n':>3} | {'t (s)':>8} | " + " | ".join([f"f = {f:.0f} Hz" for f in possible_freqs])
    print(header)
    print("-" * len(header))
    for n, t in zip(sample_indices, sample_times):
        vals = [np.cos(2 * np.pi * f * t) for f in possible_freqs]
        vals_str = " | ".join([f"{v:>10.4f}" for v in vals])
        print(f"{n:>3} | {t:>8.4f} | {vals_str}")
    print("-> All signals produce identical sample values at every sampling instant!\n")
    print("=" * 75)

    # Visualization
    t_plot_end = 0.1  # 100 ms to inspect first 4 samples clearly
    t_dense = np.linspace(0, t_plot_end, 2000)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    colors = ["crimson", "dodgerblue", "forestgreen", "darkorange", "purple"]
    linestyles = ["-", "--", "-.", ":", "-"]

    # Subplot 1: Continuous waveforms intersecting at sample points
    for f_cand, c, ls in zip(possible_freqs, colors, linestyles):
        x_dense = np.cos(2 * np.pi * f_cand * t_dense)
        ax1.plot(t_dense, x_dense, label=f"f = {f_cand:.0f} Hz", color=c, ls=ls, lw=1.5, alpha=0.8)

    # Stem the sampled points of the apparent 12 Hz signal
    t_samples_plot = np.arange(0, t_plot_end + Ts / 2, Ts)
    x_samples_plot = np.cos(2 * np.pi * fa * t_samples_plot)
    markerline, stemlines, baseline = ax1.stem(
        t_samples_plot,
        x_samples_plot,
        linefmt="black",
        markerfmt="ko",
        basefmt="none",
        label="Discrete Samples (fs = 40 Hz)",
    )
    plt.setp(markerline, markersize=7, zorder=10)

    ax1.set_title("Time-Domain Aliasing: All 5 Frequencies Intersect at the Exact Same Sample Points!")
    ax1.set_xlabel("Time (seconds)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper right", ncol=2, fontsize=8)

    # Subplot 2: Candidate frequencies and folding diagram
    f_axis = np.linspace(0, 100, 1000)
    fa_axis = observed_alias(f_axis, fs)

    ax2.plot(f_axis, fa_axis, color="teal", lw=1.5, label="Folding Profile (fs = 40 Hz)")
    ax2.axhline(fa, color="crimson", linestyle="--", lw=1.5, label=f"Observed fa = {fa:.0f} Hz")
    ax2.axvline(fn, color="black", linestyle=":", label="Nyquist Limit fn = 20 Hz")

    for f_cand, c in zip(possible_freqs, colors):
        ax2.scatter([f_cand], [fa], color=c, s=70, zorder=5)
        ax2.annotate(
            f"{f_cand:.0f} Hz",
            xy=(f_cand, fa),
            xytext=(f_cand - 2, fa + 1.2),
            fontsize=9,
            fontweight="bold",
            color=c,
        )

    ax2.set_title("Frequency Domain: Intersections with Observed 12 Hz Level")
    ax2.set_xlabel("Original Frequency f (Hz)")
    ax2.set_ylabel("Observed Frequency fa (Hz)")
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 25)
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(loc="lower right", fontsize=8)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem14()
