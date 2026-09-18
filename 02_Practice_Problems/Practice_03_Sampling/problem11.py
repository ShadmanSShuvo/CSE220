"""
Problem 11: Unknown Sampling Frequency
======================================

Problem Statement:
------------------
A sinusoidal signal has frequency:
    f = 17 Hz.

After sampling, the observed frequency is 13 Hz.

Find all possible sampling frequencies below 100 Hz that could produce this alias.

Write a program to search for the possible values.
"""

import numpy as np
import matplotlib.pyplot as plt


def observed_frequency(f, fs):
    """Computes observed baseband frequency in [0, fs/2]."""
    return np.abs(f - fs * np.round(f / fs))


def solve_problem11():
    f_orig = 17.0
    f_target_alias = 13.0
    fs_max = 100.0

    print("=" * 75)
    print("CSE220 Lab — Problem 11: Unknown Sampling Frequency")
    print("=" * 75)
    print(f"Original Signal Frequency (f):    {f_orig} Hz")
    print(f"Target Observed Frequency (fa):   {f_target_alias} Hz")
    print(f"Sampling Frequency Search Range: 0 < fs < {fs_max} Hz\n")

    # Analytical Derivation:
    print("--- Analytical Derivation ---")
    print("1. An observed frequency fa requires fs >= 2 * fa (Nyquist folding bound):")
    print(f"      fs >= 2 * {f_target_alias} = {2 * f_target_alias} Hz.")
    print("2. The observed alias occurs when |f - k * fs| = fa for some integer k >= 1:")
    print("      k * fs = f +/- fa  =>  k * fs in {17 - 13, 17 + 13} = {4, 30}")
    print("3. Evaluating candidates:")
    print("   - For k*fs = 4:   fs = 4/k <= 4 Hz  -> VIOLATES fs >= 26 Hz.")
    print("   - For k*fs = 30:")
    print("       k = 1 => fs = 30 Hz  (30 >= 26 Hz -> VALID!)")
    print("       k = 2 => fs = 15 Hz  (15 < 26 Hz  -> INVALID, folding limit is 7.5 Hz < 13 Hz)")
    print("       k >= 3 => fs <= 10 Hz (INVALID, folding limit < 13 Hz)")
    print("Conclusion: fs = 30 Hz is the UNIQUE sampling frequency below 100 Hz!\n")

    # Programmatic Grid Search
    print("--- Programmatic Numerical Search (Resolution: 0.01 Hz) ---")
    # Search grid from 1.0 to 100.0 Hz with step 0.01 Hz
    fs_candidates = np.arange(1.0, 100.0, 0.01)
    fa_computed = observed_frequency(f_orig, fs_candidates)

    # Find candidates matching 13 Hz within numerical tolerance
    tolerance = 0.05  # Hz
    matches = fs_candidates[np.isclose(fa_computed, f_target_alias, atol=tolerance)]

    # Find exact best candidate minimizing error
    best_idx = np.argmin(np.abs(fa_computed - f_target_alias))
    best_fs = fs_candidates[best_idx]
    clusters = [best_fs]
    actual_fa = observed_frequency(f_orig, best_fs)

    print(f"Identified Candidate Sampling Frequency below 100 Hz:")
    print(f"  -> fs = {best_fs:.2f} Hz  (Observed fa = {actual_fa:.2f} Hz, Folding limit = {best_fs/2:.2f} Hz)")
    print()

    # Experimental Verification via Signal Simulation & FFT
    fs_test = 30.0
    duration = 5.0
    N = int(fs_test * duration)
    t = np.arange(N) / fs_test
    x = np.sin(2 * np.pi * f_orig * t)

    X = np.fft.rfft(x)
    freqs = np.fft.rfftfreq(N, d=1.0 / fs_test)
    mag = np.abs(X) / (N / 2)
    measured_peak = freqs[np.argmax(mag)]

    print("--- Experimental Verification via FFT Simulation ---")
    print(f"Simulating x(t) = sin(2*pi*17*t) sampled at fs = {fs_test:.1f} Hz:")
    print(f"  Dominant FFT Peak Measured: {measured_peak:.2f} Hz")
    if np.isclose(measured_peak, f_target_alias, atol=0.2):
        print(f"  >> Confirmed: Sampling at {fs_test:.0f} Hz produces exactly the 13 Hz alias!")
    print("=" * 75)

    # Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))

    # Top plot: fa as a function of fs
    fs_plot = np.linspace(20, 100, 2000)
    fa_plot = observed_frequency(f_orig, fs_plot)

    ax1.plot(fs_plot, fa_plot, color="royalblue", lw=1.5, label="Observed Frequency fa(fs)")
    ax1.axhline(f_target_alias, color="crimson", linestyle="--", lw=1.5, label=f"Target Alias = {int(f_target_alias)} Hz")
    ax1.axvline(2 * f_target_alias, color="gray", linestyle=":", label=f"Nyquist Threshold 2*fa = {int(2*f_target_alias)} Hz")

    for sol in clusters:
        ax1.scatter([sol], [f_target_alias], color="crimson", s=80, zorder=5)
        ax1.annotate(
            f"Unique Solution:\nfs = {sol:.0f} Hz",
            xy=(sol, f_target_alias),
            xytext=(sol + 5, f_target_alias + 2),
            arrowprops=dict(arrowstyle="->", color="crimson", lw=1.2),
            fontweight="bold",
        )

    ax1.set_title("Search for Unknown Sampling Frequency (f = 17 Hz, fa = 13 Hz)")
    ax1.set_xlabel("Sampling Frequency fs (Hz)")
    ax1.set_ylabel("Observed Frequency (Hz)")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend(loc="upper right")

    # Bottom plot: FFT Spectrum at fs = 30 Hz
    ax2.stem(freqs, mag, linefmt="navy", markerfmt="bo", basefmt="gray", label="FFT at fs = 30 Hz")
    ax2.axvline(f_target_alias, color="crimson", linestyle="--", lw=2, label=f"Detected 13 Hz Peak")
    ax2.axvline(fs_test / 2, color="black", linestyle=":", label="Nyquist Limit fn = 15 Hz")
    ax2.set_title(f"Experimental Verification: Discrete Spectrum for fs = {int(fs_test)} Hz")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Magnitude")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem11()
