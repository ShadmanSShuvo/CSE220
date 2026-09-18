"""
Problem 3: Demonstrate Aliasing
===============================

Problem Statement:
------------------
Generate:
    x(t) = sin(2 * pi * 35 * t)
with sampling frequency:
    f_s = 50 Hz.

Tasks:
------
1. Sample the signal.
2. Calculate the apparent/aliased frequency.
3. Plot the original and sampled signals.
4. Verify the alias frequency experimentally.

Expected Concept:
-----------------
Students should discover that a 35-Hz sinusoid sampled at 50 Hz appears as a
lower-frequency sinusoid (15 Hz).
"""

import numpy as np
import matplotlib.pyplot as plt


def solve_problem3():
    f0 = 35.0  # Original signal frequency in Hz
    fs = 50.0  # Sampling frequency in Hz
    Ts = 1.0 / fs
    fn = fs / 2.0  # Nyquist frequency = 25 Hz

    print("=" * 65)
    print("CSE220 Lab — Problem 3: Demonstrate Aliasing")
    print("=" * 65)
    print(f"Original Signal: x(t) = sin(2 * pi * {f0} * t)")
    print(f"Sampling Frequency (fs) = {fs} Hz")
    print(f"Nyquist Frequency (fs/2) = {fn} Hz")

    # Task 2: Calculate the apparent / aliased frequency analytically
    # f_alias = |f0 - fs * round(f0 / fs)| = |35 - 50| = 15 Hz
    f_alias = abs(f0 - fs * round(f0 / fs))
    print("\n--- Task 2: Analytical Calculation of Alias Frequency ---")
    print(f"Since f0 ({f0} Hz) > Nyquist frequency ({fn} Hz), aliasing occurs.")
    print(f"Folding formula: f_apparent = |f - fs * round(f / fs)|")
    print(f"               = |{f0} - {fs} * 1| = {f_alias} Hz.")
    print("Trigonometric identity:")
    print("  x[n] = sin(2*pi * 35 * n/50) = sin(2*pi*(1 - 15/50)*n)")
    print("       = sin(2*pi*n - 2*pi*(15/50)*n) = -sin(2*pi * 15 * n/50)")
    print("       = sin(2*pi * 15 * n/50 + pi)")
    print("  -> Apparent frequency is 15 Hz with a 180-degree (pi) phase shift.\n")

    # Task 1 & 3: Sample the signal and plot in time domain
    duration_plot = 0.2  # 200 ms for clear cycle visualization
    t_cont = np.linspace(0, duration_plot, 2000)
    x_cont = np.sin(2 * np.pi * f0 * t_cont)

    t_samples = np.arange(0, duration_plot + Ts / 2, Ts)
    x_samples = np.sin(2 * np.pi * f0 * t_samples)

    # Apparent continuous signal at 15 Hz
    x_apparent = -np.sin(2 * np.pi * f_alias * t_cont)

    # Task 4: Verify alias frequency experimentally using FFT
    # Use longer duration for high spectral resolution
    duration_fft = 4.0  # 4 seconds
    N_fft = int(fs * duration_fft)
    t_fft_samples = np.arange(N_fft) * Ts
    x_fft_samples = np.sin(2 * np.pi * f0 * t_fft_samples)

    # Compute FFT
    X_fft = np.fft.rfft(x_fft_samples)
    freqs = np.fft.rfftfreq(N_fft, d=Ts)
    magnitude = np.abs(X_fft) / (N_fft / 2)

    # Find peak frequency in spectrum
    peak_idx = np.argmax(magnitude)
    measured_alias_freq = freqs[peak_idx]

    print("--- Task 4: Experimental Verification via FFT ---")
    print(f"Number of FFT samples: {N_fft}, Frequency resolution: {freqs[1] - freqs[0]:.3f} Hz")
    print(f"Dominant spectral peak detected at: {measured_alias_freq:.2f} Hz")
    print(f"Theoretical alias frequency:       {f_alias:.2f} Hz")
    if np.isclose(measured_alias_freq, f_alias, atol=0.2):
        print(">> VERIFIED: Experimental FFT peak matches theoretical alias frequency perfectly!")
    print("=" * 65)

    # Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Subplot 1: Time Domain
    ax1.plot(t_cont, x_cont, label="Original x(t) (35 Hz)", color="lightgray", lw=1.5, ls=":")
    ax1.plot(t_cont, x_apparent, label="Apparent Alias Signal (15 Hz)", color="forestgreen", lw=2)
    markerline, stemlines, baseline = ax1.stem(
        t_samples,
        x_samples,
        linefmt="crimson",
        markerfmt="ro",
        basefmt="black",
        label=f"Sampled points (fs={int(fs)} Hz)",
    )
    plt.setp(markerline, markersize=5)
    ax1.set_title("Time-Domain Aliasing: 35 Hz sampled at 50 Hz looks identically like 15 Hz")
    ax1.set_xlabel("Time (seconds)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(loc="upper right")

    # Subplot 2: Frequency Domain (FFT)
    ax2.stem(freqs, magnitude, linefmt="navy", markerfmt="bo", basefmt="gray", label="Discrete Spectrum")
    ax2.axvline(fn, color="red", linestyle="--", lw=1.5, label=f"Nyquist Limit fs/2 = {fn:.0f} Hz")
    ax2.axvline(measured_alias_freq, color="crimson", linestyle=":", lw=2, label=f"Detected Peak ({measured_alias_freq:.1f} Hz)")
    ax2.set_title(f"Experimental Frequency Spectrum (FFT): Peak is at {measured_alias_freq:.1f} Hz (not 35 Hz)")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Normalized Magnitude")
    ax2.set_xlim(0, fn + 5)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem3()
