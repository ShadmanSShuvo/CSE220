"""
Problem 5: Sampling a Composite Signal
======================================

Problem Statement:
------------------
Given:
    x(t) = 2*cos(2*pi*5*t) + cos(2*pi*15*t) + 0.5*sin(2*pi*30*t)

Tasks:
------
1. Find the minimum sampling frequency required to avoid aliasing.
2. Sample at exactly the Nyquist rate.
3. Sample above the Nyquist rate.
4. Sample below the Nyquist rate.
5. Compare the resulting plots.
"""

import numpy as np
import matplotlib.pyplot as plt


def composite_signal(t):
    """Evaluates continuous-time signal x(t)."""
    return (
        2.0 * np.cos(2 * np.pi * 5 * t)
        + 1.0 * np.cos(2 * np.pi * 15 * t)
        + 0.5 * np.sin(2 * np.pi * 30 * t)
    )


def solve_problem5():
    # Signal frequency components
    frequencies = [5.0, 15.0, 30.0]
    f_max = max(frequencies)

    # Task 1: Minimum sampling frequency
    nyquist_rate = 2 * f_max  # 60 Hz

    print("=" * 70)
    print("CSE220 Lab — Problem 5: Sampling a Composite Signal")
    print("=" * 70)
    print("Given: x(t) = 2*cos(2*pi*5*t) + cos(2*pi*15*t) + 0.5*sin(2*pi*30*t)")
    print(f"Frequency components: {frequencies} Hz")
    print(f"1. Maximum frequency component (f_max) = {f_max} Hz")
    print(f"   Minimum sampling frequency (Nyquist rate = 2*f_max) = {nyquist_rate} Hz\n")

    # Rates for tasks 2, 3, 4:
    # Task 2: Exactly Nyquist rate (60 Hz)
    # Task 3: Above Nyquist rate (e.g., 150 Hz)
    # Task 4: Below Nyquist rate (e.g., 35 Hz)
    sampling_scenarios = [
        {"name": "Above Nyquist Rate (Oversampled)", "fs": 150.0, "color": "forestgreen"},
        {"name": "Exactly Nyquist Rate (Critical)", "fs": 60.0, "color": "darkorange"},
        {"name": "Below Nyquist Rate (Undersampled)", "fs": 35.0, "color": "crimson"},
    ]

    duration = 0.5
    t_cont = np.linspace(0, duration, 2000)
    x_cont = composite_signal(t_cont)

    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    for idx, sc in enumerate(sampling_scenarios):
        fs = sc["fs"]
        Ts = 1.0 / fs
        fn = fs / 2.0

        # Time domain samples
        t_samples = np.arange(0, duration + Ts / 2, Ts)
        x_samples = composite_signal(t_samples)

        # Theoretical alias analysis
        aliases = [abs(f - fs * round(f / fs)) for f in frequencies]

        print(f"--- Scenario {idx+1}: {sc['name']} (fs = {fs} Hz, fn = {fn} Hz) ---")
        for orig_f, a_f in zip(frequencies, aliases):
            status = "Intact" if orig_f <= fn else f"ALIASED to {a_f} Hz"
            print(f"  * Component {orig_f:4.1f} Hz -> {status}")

        if fs == 60.0:
            print("  Special Note: The 30 Hz component is at exactly fs/2 (sin(30*2*pi*n/60) = sin(n*pi) = 0).")
            print("  It vanishes completely from the sampled signal in time domain!")
        elif fs == 35.0:
            print("  Special Note: The 30 Hz component aliases to |30 - 35| = 5 Hz.")
            print("  It directly collides with and corrupts the genuine 5 Hz component!")
        print()

        # FFT computation for spectral comparison
        duration_fft = 4.0
        N_fft = int(fs * duration_fft)
        t_fft = np.arange(N_fft) * Ts
        x_fft = composite_signal(t_fft)
        X = np.fft.rfft(x_fft)
        freqs = np.fft.rfftfreq(N_fft, d=Ts)
        mag = np.abs(X) / (N_fft / 2)

        # Plot Time Domain (Left Column)
        ax_time = axes[idx, 0]
        ax_time.plot(t_cont, x_cont, label="Continuous x(t)", color="royalblue", alpha=0.5, lw=1.2)
        markerline, stemlines, baseline = ax_time.stem(
            t_samples,
            x_samples,
            linefmt=sc["color"],
            markerfmt="o",
            basefmt="gray",
            label=f"Samples (fs = {int(fs)} Hz)",
        )
        plt.setp(markerline, color=sc["color"], markersize=4)
        ax_time.set_title(f"{sc['name']}: Time Domain (fs = {int(fs)} Hz)")
        ax_time.set_ylabel("Amplitude")
        ax_time.set_xlabel("Time (s)")
        ax_time.grid(True, linestyle="--", alpha=0.5)
        ax_time.legend(loc="upper right", fontsize=8)

        # Plot Frequency Domain (Right Column)
        ax_freq = axes[idx, 1]
        markerline2, stemlines2, baseline2 = ax_freq.stem(
            freqs,
            mag,
            linefmt=sc["color"],
            markerfmt="o",
            basefmt="gray",
            label="Observed Spectrum",
        )
        plt.setp(markerline2, color=sc["color"], markersize=4)
        ax_freq.axvline(fn, color="black", linestyle="--", alpha=0.7, label=f"Nyquist Limit (fn={fn:.1f} Hz)")
        ax_freq.set_xlim(0, max(45, fn + 5))
        ax_freq.set_title(f"Observed Magnitude Spectrum (0 to {fn:.1f} Hz)")
        ax_freq.set_ylabel("Magnitude")
        ax_freq.set_xlabel("Frequency (Hz)")
        ax_freq.grid(True, linestyle="--", alpha=0.5)
        ax_freq.legend(loc="upper right", fontsize=8)

    print("=" * 70)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem5()
