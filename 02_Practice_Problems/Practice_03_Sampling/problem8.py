"""
Problem 8: Undersampling and Reconstruction Failure
===================================================

Problem Statement:
------------------
Given:
    x(t) = sin(2 * pi * 40 * t)
and:
    f_s = 50 Hz.

Tasks:
------
1. Sample the signal.
2. Reconstruct it using sinc interpolation.
3. Compare the reconstructed signal with the original.
4. Explain why perfect reconstruction is impossible even though sinc interpolation is used.
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
    """Reconstructs continuous-time signal using sinc interpolation."""
    delta = (t_eval[:, np.newaxis] - t_samples[np.newaxis, :]) / Ts
    sinc_matrix = manual_sinc(delta)
    return np.dot(sinc_matrix, x_samples)


def solve_problem8():
    f0 = 40.0  # Original frequency = 40 Hz
    fs = 50.0  # Sampling frequency = 50 Hz
    Ts = 1.0 / fs
    nyquist_rate = 2 * f0  # 80 Hz
    fn = fs / 2.0  # Folding frequency = 25 Hz

    # Analytical alias calculation:
    f_alias = abs(f0 - fs * round(f0 / fs))  # |40 - 50| = 10 Hz

    print("=" * 75)
    print("CSE220 Lab — Problem 8: Undersampling and Reconstruction Failure")
    print("=" * 75)
    print(f"Original Signal: x(t) = sin(2 * pi * {f0} * t)")
    print(f"Original Frequency:      {f0} Hz")
    print(f"Sampling Frequency (fs): {fs} Hz")
    print(f"Nyquist Rate (2*f_max):  {nyquist_rate} Hz")
    print(f"Folding Limit (fs/2):    {fn} Hz")
    print(f"Theoretical Alias:       {f_alias} Hz (with 180-deg phase inversion)\n")

    # Time ranges
    t_start, t_end = 0.0, 0.2  # 200 ms
    margin = 0.3
    t_sample_grid = np.arange(t_start - margin, t_end + margin + Ts / 2, Ts)
    x_sample_vals = np.sin(2 * np.pi * f0 * t_sample_grid)

    # Dense time grid for original vs reconstructed signal
    t_dense = np.linspace(t_start, t_end, 1000)
    x_orig = np.sin(2 * np.pi * f0 * t_dense)

    # Task 2: Reconstruct using sinc interpolation
    x_reconstructed = sinc_reconstruct(t_dense, t_sample_grid, x_sample_vals, Ts)

    # Theoretical alias waveform: -sin(2*pi*10*t)
    x_alias_theory = -np.sin(2 * np.pi * f_alias * t_dense)

    # Task 3: Compare reconstructed signal with original
    error = x_reconstructed - x_orig
    rmse = np.sqrt(np.mean(error ** 2))
    max_err = np.max(np.abs(error))

    # Error relative to the alias signal
    err_vs_alias = x_reconstructed - x_alias_theory
    rmse_vs_alias = np.sqrt(np.mean(err_vs_alias ** 2))

    print("--- Task 3: Reconstruction vs Original Comparison ---")
    print(f"Reconstruction Error vs Original 40-Hz signal (RMSE):     {rmse:.4f}")
    print(f"Reconstruction Error vs Theoretical 10-Hz alias (RMSE):  {rmse_vs_alias:.4e}")
    print("-> The reconstructed signal does NOT match the 40 Hz original at all!")
    print("-> Instead, it matches the 10 Hz alias signal with near-zero error.\n")

    # Task 4: Explanation
    print("--- Task 4: Why Perfect Reconstruction Fails ---")
    print(
        "1. Whittaker-Shannon interpolation acts as an ideal low-pass filter (LPF)\n"
        f"   with cutoff frequency fc = fs/2 = {fn} Hz.\n"
        f"2. Because fs ({fs} Hz) < 2 * f_max ({nyquist_rate} Hz), aliasing occurred during sampling.\n"
        f"3. The 40-Hz sinusoid folded irreversibly into the baseband at {f_alias} Hz:\n"
        "      sin(2*pi*40*n/50) = sin(2*pi*n - 2*pi*10*n/50) = -sin(2*pi*10*n/50)\n"
        f"4. Sinc interpolation reconstructs the UNIQUE bandlimited signal in [-{fn}, +{fn}] Hz\n"
        f"   that passes through those sample points. That unique signal is the {f_alias}-Hz wave.\n"
        "5. Once aliasing occurs during sampling, the high-frequency information is permanently lost;\n"
        "   sinc interpolation cannot resurrect information that was not captured."
    )
    print("=" * 75)

    # Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Subplot 1: Waveform comparison
    ax1.plot(t_dense, x_orig, color="lightgray", lw=1.5, ls="--", label="Original x(t) (40 Hz)")
    ax1.plot(t_dense, x_reconstructed, color="crimson", lw=2, label=f"Sinc Reconstructed Signal (~{f_alias} Hz)")
    ax1.plot(t_dense, x_alias_theory, color="navy", lw=1.2, ls=":", label="Theoretical Alias (-sin(2*pi*10*t))")

    display_mask = (t_sample_grid >= t_start) & (t_sample_grid <= t_end)
    markerline, stemlines, baseline = ax1.stem(
        t_sample_grid[display_mask],
        x_sample_vals[display_mask],
        linefmt="forestgreen",
        markerfmt="go",
        basefmt="gray",
        label=f"Sample Points (fs = {int(fs)} Hz)",
    )
    plt.setp(markerline, markersize=6)

    ax1.set_title("Undersampling Failure: Sinc Interpolation Reconstructs the 10-Hz Alias, Not 40 Hz!")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(loc="upper right")

    # Subplot 2: Difference / Error
    ax2.plot(t_dense, error, color="darkorange", lw=1.5, label=f"Error: x_rec(t) - x_orig(t) (RMSE = {rmse:.2f})")
    ax2.set_title("Reconstruction Error vs Original Signal")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Error")
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem8()
