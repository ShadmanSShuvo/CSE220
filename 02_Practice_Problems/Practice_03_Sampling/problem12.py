"""
Problem 12: Design the Minimum Sampling Rate
============================================

Problem Statement:
------------------
Given:
    x(t) = sin(2*pi*8*t) + 2*cos(2*pi*17*t) + cos(2*pi*31*t) + 0.5*sin(2*pi*43*t)

1. Find the minimum sampling frequency that allows perfect reconstruction.
2. Then write a program that automatically determines the required sampling
   rate for an arbitrary list of frequency components.
"""

import numpy as np
import matplotlib.pyplot as plt


def manual_sinc(u):
    """Normalized sinc function: sinc(u) = sin(pi * u) / (pi * u)."""
    u = np.asarray(u, dtype=float)
    out = np.ones_like(u)
    nonzero = u != 0.0
    out[nonzero] = np.sin(np.pi * u[nonzero]) / (np.pi * u[nonzero])
    return out


def sinc_reconstruct(t_eval, t_samples, x_samples, Ts):
    """Reconstructs continuous-time signal from discrete samples."""
    delta = (t_eval[:, np.newaxis] - t_samples[np.newaxis, :]) / Ts
    sinc_matrix = manual_sinc(delta)
    return np.dot(sinc_matrix, x_samples)


def evaluate_signal(t, freqs, amps, phases, wave_types):
    """Evaluates arbitrary multi-tone signal."""
    val = np.zeros_like(t, dtype=float)
    for f, a, ph, w in zip(freqs, amps, phases, wave_types):
        if w == "cos":
            val += a * np.cos(2 * np.pi * f * t + ph)
        else:
            val += a * np.sin(2 * np.pi * f * t + ph)
    return val


def determine_sampling_rate(frequencies, safety_margin_pct=20.0):
    """
    Automatically determines the required sampling rate for an arbitrary list
    of frequency components.

    Parameters:
        frequencies (list of float): Frequency components in Hz.
        safety_margin_pct (float): Optional engineering headroom percentage (default: 20%).

    Returns:
        dict: Summary containing f_max, nyquist_rate, and recommended_fs.
    """
    if not frequencies:
        raise ValueError("Frequency list must not be empty.")

    f_max = max(frequencies)
    nyquist_rate = 2.0 * f_max
    recommended_fs = nyquist_rate * (1.0 + safety_margin_pct / 100.0)

    return {
        "f_max": f_max,
        "nyquist_rate": nyquist_rate,
        "recommended_fs": recommended_fs,
        "safety_margin_pct": safety_margin_pct,
    }


def solve_problem12():
    # Signal definition from problem:
    # x(t) = sin(2*pi*8*t) + 2*cos(2*pi*17*t) + cos(2*pi*31*t) + 0.5*sin(2*pi*43*t)
    freqs = [8.0, 17.0, 31.0, 43.0]
    amps = [1.0, 2.0, 1.0, 0.5]
    phases = [0.0, 0.0, 0.0, 0.0]
    wave_types = ["sin", "cos", "cos", "sin"]

    print("=" * 75)
    print("CSE220 Lab — Problem 12: Design the Minimum Sampling Rate")
    print("=" * 75)
    print("Given Signal:")
    print("  x(t) = sin(2*pi*8*t) + 2*cos(2*pi*17*t) + cos(2*pi*31*t) + 0.5*sin(2*pi*43*t)")
    print(f"Frequency components: {freqs} Hz\n")

    # Task 1 & 2: Automatic determination
    result = determine_sampling_rate(freqs, safety_margin_pct=25.0)

    print("--- Automatic Sampling Rate Design Result ---")
    print(f"1. Maximum Frequency Component (f_max):     {result['f_max']:.1f} Hz")
    print(f"2. Theoretical Minimum Rate (Nyquist Rate): {result['nyquist_rate']:.1f} Hz")
    print(f"   (Strictly requires fs > {result['nyquist_rate']:.1f} Hz for perfect reconstruction)")
    print(f"3. Practical Engineering Recommendation:    {result['recommended_fs']:.1f} Hz")
    print(f"   (Includes {result['safety_margin_pct']:.0f}% guard margin for anti-aliasing filter transition)\n")

    # Demonstrate arbitrary list test
    print("--- Testing determine_sampling_rate on Arbitrary Frequency Lists ---")
    test_signals = [
        {"name": "Speech Baseband", "freqs": [300, 1200, 2400, 3400]},
        {"name": "Hi-Fi Audio", "freqs": [20, 440, 5000, 15000, 20000]},
        {"name": "Seismic Vibration", "freqs": [0.5, 2.3, 7.8]},
    ]
    for ts in test_signals:
        r = determine_sampling_rate(ts["freqs"], safety_margin_pct=10.0)
        print(f"  * {ts['name']} (f_max={r['f_max']} Hz) -> Nyquist: {r['nyquist_rate']} Hz, Rec: {r['recommended_fs']:.0f} Hz")
    print()

    # Numerical Validation via Sinc Reconstruction
    t_start, t_end = 0.0, 0.3
    t_dense = np.linspace(t_start, t_end, 1000)
    x_orig = evaluate_signal(t_dense, freqs, amps, phases, wave_types)

    rates_to_test = [
        {"name": "Undersampled (fs = 70 Hz < 86 Hz)", "fs": 70.0, "color": "crimson"},
        {"name": "Critical Nyquist (fs = 86 Hz == 2*f_max)", "fs": 86.0, "color": "darkorange"},
        {"name": "Properly Sampled (fs = 110 Hz > 86 Hz)", "fs": 110.0, "color": "forestgreen"},
    ]

    fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)

    print("--- Sinc Reconstruction Error Verification ---")
    margin = 0.4
    for idx, r_case in enumerate(rates_to_test):
        fs = r_case["fs"]
        Ts = 1.0 / fs
        t_samples = np.arange(t_start - margin, t_end + margin + Ts / 2, Ts)
        x_samples = evaluate_signal(t_samples, freqs, amps, phases, wave_types)

        x_rec = sinc_reconstruct(t_dense, t_samples, x_samples, Ts)
        rmse = np.sqrt(np.mean((x_rec - x_orig) ** 2))

        print(f"* {r_case['name']}:")
        print(f"    Reconstruction RMSE: {rmse:.4e}")
        if fs < result["nyquist_rate"]:
            print("    Verdict: FAILS reconstruction due to aliasing of the 43-Hz component.")
        elif fs == result["nyquist_rate"]:
            print("    Verdict: Marginal/Degraded. The 43-Hz sine component falls at fs/2 and vanishes.")
        else:
            print("    Verdict: PASSES! Perfect reconstruction achieved.")
        print()

        ax = axes[idx]
        ax.plot(t_dense, x_orig, color="royalblue", lw=1.5, alpha=0.6, label="Original x(t)")
        ax.plot(t_dense, x_rec, color=r_case["color"], lw=1.8, ls="--", label=f"Reconstructed (RMSE={rmse:.2e})")

        mask = (t_samples >= t_start) & (t_samples <= t_end)
        markerline, stemlines, baseline = ax.stem(
            t_samples[mask],
            x_samples[mask],
            linefmt="gray",
            markerfmt="o",
            basefmt="none",
            label="Sample Points",
        )
        plt.setp(markerline, markersize=3, color="gray")

        ax.set_title(r_case["name"])
        ax.set_ylabel("Amplitude")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend(loc="upper right", fontsize=8)

    axes[-1].set_xlabel("Time (seconds)")
    print("=" * 75)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem12()
