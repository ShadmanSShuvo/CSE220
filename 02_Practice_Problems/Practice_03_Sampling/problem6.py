"""
Problem 6: Frequency-Domain View of Sampling ⭐
================================================

Problem Statement:
------------------
Consider:
    x(t) = cos(2 * pi * 10 * t).

Sample it using an impulse train:
    p(t) = sum_{n=-inf}^{inf} delta(t - n * Ts).

The sampled signal is:
    x_s(t) = x(t) * p(t).

Tasks:
------
1. Explain why sampling creates repeated spectra.
2. Numerically approximate the FFT of the sampled signal.
3. Plot the magnitude spectrum.
4. Repeat for:
    * f_s = 100 Hz
    * f_s = 30 Hz
    * f_s = 15 Hz
5. Identify spectral overlap.
"""

import numpy as np
import matplotlib.pyplot as plt


def solve_problem6():
    f0 = 10.0  # Signal frequency = 10 Hz
    nyquist_rate = 2 * f0  # 20 Hz
    sampling_rates = [100.0, 30.0, 15.0]

    print("=" * 75)
    print("CSE220 Lab — Problem 6: Frequency-Domain View of Sampling")
    print("=" * 75)
    print(f"Original Signal: x(t) = cos(2 * pi * {f0} * t)")
    print(f"Nyquist Rate (2 * f_max): {nyquist_rate} Hz\n")

    # Task 1: Explanation
    print("--- Task 1: Mathematical Theory of Repeated Spectra ---")
    print(
        "1. Multiplication in time corresponds to convolution in frequency:\n"
        "      x_s(t) = x(t) * p(t)  <--->  X_s(f) = (1 / Ts) * sum_k X(f - k * fs)\n"
        "2. The Fourier transform of an impulse train p(t) is itself an impulse train in frequency:\n"
        "      P(f) = (1 / Ts) * sum_k delta(f - k * fs)\n"
        "3. Convolving X(f) = 0.5 * [delta(f - f0) + delta(f + f0)] with P(f) replicates the\n"
        "   original two spectral spikes (at +/- 10 Hz) periodically at intervals of fs:\n"
        "      Spikes appear at: f = +/- f0 + k * fs,  for all k in Z.\n"
        "4. If fs >= 2 * f0, adjacent replicas do not overlap (guard band >= 0).\n"
        "5. If fs < 2 * f0, adjacent replicas overlap, corrupting the baseband (Aliasing).\n"
    )

    # Numerical simulation parameters
    # Simulate continuous time using a very high sampling rate f_cont
    f_cont = 2000.0  # Dense grid rate (Hz)
    dt_cont = 1.0 / f_cont
    duration = 2.0   # 2 seconds duration
    t_cont = np.arange(0, duration, dt_cont)
    N_cont = len(t_cont)

    x_cont = np.cos(2 * np.pi * f0 * t_cont)

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))

    print("--- Tasks 4 & 5: Spectral Analysis & Overlap Identification ---")
    for idx, fs in enumerate(sampling_rates):
        Ts = 1.0 / fs
        fn = fs / 2.0

        # Create impulse train on the dense time grid
        # In discrete representation of continuous delta: delta(t) -> 1/dt_cont at sample instants
        sample_indices = np.round(np.arange(0, duration, Ts) * f_cont).astype(int)
        sample_indices = sample_indices[sample_indices < N_cont]

        p_t = np.zeros(N_cont)
        p_t[sample_indices] = f_cont  # Scale to approximate unit impulse area

        # Sampled signal in continuous time
        x_s = x_cont * p_t * dt_cont  # Sampled impulse train x_s(t)

        # Two-sided FFT of sampled signal
        X_s = np.fft.fftshift(np.fft.fft(x_s))
        freqs = np.fft.fftshift(np.fft.fftfreq(N_cont, d=dt_cont))
        magnitude = np.abs(X_s) / (len(sample_indices))

        # Identify overlap
        has_overlap = fs < nyquist_rate
        guard_band = fs - 2 * f0

        print(f"* fs = {fs:3.0f} Hz (Nyquist limit fn = {fn:4.1f} Hz):")
        print(f"    Guard band (fs - 2*f0) = {guard_band:4.1f} Hz")
        if has_overlap:
            overlap_desc = (
                f"SPECTRAL OVERLAP DETECTED (fs < 2*f0).\n"
                f"    Replica from k=1 (centered at {fs} Hz) has component at {fs - f0} Hz.\n"
                f"    This folds into baseband [-{fn}, +{fn}] Hz, causing irreversible distortion!"
            )
        else:
            overlap_desc = (
                f"No spectral overlap (fs >= 2*f0).\n"
                f"    Guard band of {guard_band} Hz cleanly separates replicas centered at k*{fs} Hz."
            )
        print(f"    Status: {overlap_desc}\n")

        ax = axes[idx]
        # Restrict plot to [-120, 120] Hz
        mask = (freqs >= -120) & (freqs <= 120)
        ax.plot(freqs[mask], magnitude[mask], color="navy", lw=1.2, label=f"|X_s(f)| (fs={int(fs)} Hz)")

        # Mark replica centers (k * fs)
        max_k = int(120 // fs) + 1
        for k in range(-max_k, max_k + 1):
            center = k * fs
            if -120 <= center <= 120:
                ax.axvline(center, color="gray", linestyle=":", alpha=0.5)
                ax.text(center, np.max(magnitude[mask]) * 0.9, f"k={k}\n({int(center)}Hz)",
                        ha="center", fontsize=7, color="dimgray")

        # Mark baseband Nyquist boundaries [-fn, +fn]
        ax.axvline(-fn, color="red", linestyle="--", alpha=0.7, label=f"Nyquist limits (+/-{fn:.1f} Hz)" if k == 0 else "")
        ax.axvline(fn, color="red", linestyle="--", alpha=0.7)

        # Highlight overlap zone if aliasing occurs
        if has_overlap:
            ax.axvspan(-fn, fn, color="salmon", alpha=0.2, label="Baseband with Aliased Overlap")
        else:
            ax.axvspan(-fn, fn, color="lightgreen", alpha=0.15, label="Clean Baseband")

        ax.set_title(
            f"Magnitude Spectrum for fs = {int(fs)} Hz "
            f"({'SPECTRAL OVERLAP / ALIASING' if has_overlap else 'NO OVERLAP'})"
        )
        ax.set_ylabel("Magnitude")
        ax.set_xlim(-120, 120)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend(loc="upper right", fontsize=8)

    axes[-1].set_xlabel("Frequency (Hz)")
    print("=" * 75)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem6()
