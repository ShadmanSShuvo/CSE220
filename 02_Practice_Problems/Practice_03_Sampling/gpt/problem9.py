"""
Problem 9: ECG-Like Signal Sampling
===================================

Problem Statement:
------------------
Generate a synthetic signal:
    x(t) = sin(2*pi*1.2*t) + 0.3*sin(2*pi*15*t) + 0.1*sin(2*pi*40*t)

Treat it as a simplified physiological signal.

Tasks:
------
1. Determine its maximum frequency.
2. Calculate the Nyquist rate.
3. Sample it at f_s = 100, 60, and 50 Hz.
4. Plot the signals.
5. Compare their FFT spectra.
6. Discuss which components become distorted due to aliasing.
"""

import numpy as np
import matplotlib.pyplot as plt


def ecg_signal(t):
    """Generates the simplified physiological ECG-like signal."""
    return (
        np.sin(2 * np.pi * 1.2 * t)
        + 0.3 * np.sin(2 * np.pi * 15.0 * t)
        + 0.1 * np.sin(2 * np.pi * 40.0 * t)
    )


def solve_problem9():
    components = [
        {"name": "Cardiac Base Rhythm (1.2 Hz)", "f": 1.2, "amp": 1.0},
        {"name": "P/T Wave Dynamics (15 Hz)", "f": 15.0, "amp": 0.3},
        {"name": "QRS Sharp Feature (40 Hz)", "f": 40.0, "amp": 0.1},
    ]
    freqs_list = [c["f"] for c in components]

    # Task 1: Maximum frequency component
    f_max = max(freqs_list)

    # Task 2: Nyquist rate
    nyquist_rate = 2 * f_max  # 80 Hz

    print("=" * 75)
    print("CSE220 Lab — Problem 9: ECG-Like Signal Sampling")
    print("=" * 75)
    print("Signal: x(t) = sin(2*pi*1.2*t) + 0.3*sin(2*pi*15*t) + 0.1*sin(2*pi*40*t)")
    print(f"1. Maximum frequency component (f_max): {f_max} Hz")
    print(f"2. Nyquist rate (2 * f_max):            {nyquist_rate} Hz\n")

    sampling_rates = [100.0, 60.0, 50.0]
    duration_time = 1.5  # 1.5 s for time-domain display
    duration_fft = 10.0  # 10 s for fine frequency resolution (0.1 Hz)

    t_cont = np.linspace(0, duration_time, 3000)
    x_cont = ecg_signal(t_cont)

    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    print("--- Tasks 5 & 6: FFT Spectra Comparison & Distortion Discussion ---")
    for idx, fs in enumerate(sampling_rates):
        Ts = 1.0 / fs
        fn = fs / 2.0

        # Time samples for plot
        t_samples = np.arange(0, duration_time + Ts / 2, Ts)
        x_samples = ecg_signal(t_samples)

        # High-resolution FFT
        N_fft = int(fs * duration_fft)
        t_fft = np.arange(N_fft) * Ts
        x_fft = ecg_signal(t_fft)
        X = np.fft.rfft(x_fft)
        fft_freqs = np.fft.rfftfreq(N_fft, d=Ts)
        mag = np.abs(X) / (N_fft / 2)

        # Predict aliases
        print(f"* Sampling rate fs = {fs:.0f} Hz (Nyquist folding limit fn = {fn:.1f} Hz):")
        if fs > nyquist_rate:
            print("  Status: NO ALIASING (fs > 80 Hz). All 3 components preserved accurately.")
        else:
            print(f"  Status: ALIASING DETECTED (fs < {nyquist_rate} Hz).")

        for c in components:
            f_comp = c["f"]
            if f_comp <= fn:
                print(f"    - {c['name']} remains intact at {f_comp:.1f} Hz.")
            else:
                f_alias = abs(f_comp - fs * round(f_comp / fs))
                print(
                    f"    - {c['name']} ALIASES to {f_alias:.1f} Hz! "
                    f"(Appears as false low-frequency artifact in baseband)."
                )
        print()

        # Left: Time Domain
        ax_time = axes[idx, 0]
        ax_time.plot(t_cont, x_cont, color="royalblue", alpha=0.5, lw=1.2, label="Analog ECG x(t)")
        markerline, stemlines, baseline = ax_time.stem(
            t_samples,
            x_samples,
            linefmt="crimson" if fs < nyquist_rate else "forestgreen",
            markerfmt="o",
            basefmt="gray",
            label=f"Sampled at {int(fs)} Hz",
        )
        plt.setp(markerline, markersize=3)
        ax_time.set_title(f"Time Domain: fs = {int(fs)} Hz ({'Aliased' if fs < nyquist_rate else 'Clean'})")
        ax_time.set_ylabel("Amplitude (mV)")
        ax_time.set_xlabel("Time (s)")
        ax_time.grid(True, linestyle="--", alpha=0.5)
        ax_time.legend(loc="upper right", fontsize=8)

        # Right: Frequency Domain (FFT)
        ax_freq = axes[idx, 1]
        markerline2, stemlines2, baseline2 = ax_freq.stem(
            fft_freqs,
            mag,
            linefmt="navy",
            markerfmt="o",
            basefmt="gray",
            label="FFT Spectrum",
        )
        plt.setp(markerline2, markersize=4)
        ax_freq.axvline(fn, color="red", linestyle="--", label=f"Folding limit fn = {fn:.1f} Hz")
        ax_freq.set_xlim(0, 50)
        ax_freq.set_title(f"FFT Spectrum (fs = {int(fs)} Hz)")
        ax_freq.set_xlabel("Frequency (Hz)")
        ax_freq.set_ylabel("Normalized Magnitude")
        ax_freq.grid(True, linestyle="--", alpha=0.5)
        ax_freq.legend(loc="upper right", fontsize=8)

    print("Discussion Summary:")
    print(
        "In physiological signals like ECG, high-frequency components (e.g. 40 Hz) capture\n"
        "rapid electrical depolarizations (the QRS complex). When sampled below 80 Hz:\n"
        "- At 60 Hz, the 40-Hz feature folds back to 20 Hz, falsely inflating mid-band power.\n"
        "- At 50 Hz, the 40-Hz feature folds to 10 Hz, overlapping near typical heart rate harmonics.\n"
        "- Such aliasing irreversibly blurs sharp physiological transients and introduces\n"
        "  misleading low-frequency artifacts that can corrupt diagnostic algorithms."
    )
    print("=" * 75)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem9()
