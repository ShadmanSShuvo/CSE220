"""
Problem 10: Audio Sampling Problem ⭐⭐
======================================

Problem Statement:
------------------
Generate a signal containing:
    f_1 = 500 Hz,  f_2 = 3000 Hz,  f_3 = 7000 Hz.

Sample it at:
    * 8 kHz (8000 Hz)
    * 12 kHz (12000 Hz)
    * 16 kHz (16000 Hz)

Tasks:
------
1. Determine the Nyquist frequency for each sampling rate.
2. Determine which frequency components alias.
3. Calculate their alias frequencies.
4. Verify your calculations using FFT plots.
"""

import numpy as np
import matplotlib.pyplot as plt


def audio_signal(t):
    """Multi-tone audio signal containing 500 Hz, 3000 Hz, and 7000 Hz tones."""
    return (
        np.cos(2 * np.pi * 500.0 * t)
        + np.cos(2 * np.pi * 3000.0 * t)
        + np.cos(2 * np.pi * 7000.0 * t)
    )


def solve_problem10():
    tone_freqs = [500.0, 3000.0, 7000.0]
    sampling_rates = [8000.0, 12000.0, 16000.0]

    print("=" * 75)
    print("CSE220 Lab — Problem 10: Audio Sampling Problem")
    print("=" * 75)
    print(f"Audio Tones: f1 = {tone_freqs[0]} Hz, f2 = {tone_freqs[1]} Hz, f3 = {tone_freqs[2]} Hz")
    print(f"Maximum tone frequency: f_max = {max(tone_freqs)} Hz\n")

    duration = 0.05  # 50 ms duration for FFT (gives 20 Hz bin resolution)

    fig, axes = plt.subplots(3, 1, figsize=(11, 10))

    for idx, fs in enumerate(sampling_rates):
        # Task 1: Determine Nyquist frequency
        fn = fs / 2.0
        Ts = 1.0 / fs

        print(f"--- Sampling Rate #{idx+1}: fs = {fs/1000:.1f} kHz ({fs:.0f} Hz) ---")
        print(f"1. Nyquist Frequency (fn = fs/2) = {fn/1000:.1f} kHz ({fn:.0f} Hz)")

        # Tasks 2 & 3: Identify aliasing and compute alias frequencies
        print("2 & 3. Tone analysis:")
        expected_peaks = []
        for f in tone_freqs:
            if f <= fn:
                print(f"   * {f:5.0f} Hz: Intact (f <= fn) -> Observed at {f:.0f} Hz")
                expected_peaks.append((f, False))
            else:
                f_alias = abs(f - fs * round(f / fs))
                print(f"   * {f:5.0f} Hz: ALIASES (f > fn) -> Folded to |{f:.0f} - {fs:.0f}| = {f_alias:.0f} Hz")
                expected_peaks.append((f_alias, True))
        print()

        # Task 4: FFT verification
        N = int(fs * duration)
        t = np.arange(N) * Ts
        x_samples = audio_signal(t)

        X = np.fft.rfft(x_samples)
        freqs = np.fft.rfftfreq(N, d=Ts)
        mag = np.abs(X) / (N / 2)

        ax = axes[idx]
        markerline, stemlines, baseline = ax.stem(
            freqs,
            mag,
            linefmt="royalblue",
            markerfmt="o",
            basefmt="gray",
            label="Observed FFT Spectrum",
        )
        plt.setp(markerline, markersize=4)

        # Mark expected peak lines
        for peak_f, is_aliased in expected_peaks:
            c = "crimson" if is_aliased else "forestgreen"
            lbl = f"Alias ({peak_f:.0f} Hz)" if is_aliased else f"Clean ({peak_f:.0f} Hz)"
            ax.axvline(peak_f, color=c, linestyle=":", lw=1.5, label=lbl)

        ax.axvline(fn, color="black", linestyle="--", lw=1.5, label=f"Nyquist limit ({fn/1000:.1f} kHz)")

        ax.set_title(f"Sampling at fs = {fs/1000:.1f} kHz (Nyquist Limit = {fn/1000:.1f} kHz)")
        ax.set_ylabel("Magnitude")
        ax.set_xlim(0, fn + 500)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend(loc="upper right", fontsize=8)

    axes[-1].set_xlabel("Frequency (Hz)")
    print("=" * 75)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem10()
