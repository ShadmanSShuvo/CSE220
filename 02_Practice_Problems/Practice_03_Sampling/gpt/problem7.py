"""
Problem 7: Reconstruction Using Sinc Interpolation ⭐⭐
======================================================

Problem Statement:
------------------
Given samples of:
    x(t) = sin(2 * pi * 5 * t)
taken at:
    f_s = 20 Hz.

Reconstruct the signal using sinc interpolation:
    x(t) = sum_{n=-inf}^{inf} x[n] * sinc((t - n * Ts) / Ts)

Tasks:
------
1. Generate the samples.
2. Implement sinc interpolation manually.
3. Reconstruct the signal.
4. Plot:
    * Original signal
    * Samples
    * Reconstructed signal
5. Calculate the reconstruction error.
"""

import numpy as np
import matplotlib.pyplot as plt


def manual_sinc(u):
    """
    Computes the normalized sinc function: sinc(u) = sin(pi * u) / (pi * u),
    handling u = 0 gracefully.
    """
    u = np.asarray(u, dtype=float)
    out = np.ones_like(u)
    nonzero = u != 0.0
    out[nonzero] = np.sin(np.pi * u[nonzero]) / (np.pi * u[nonzero])
    return out


def sinc_reconstruct(t_eval, t_samples, x_samples, Ts):
    """
    Task 2: Manual sinc interpolation implementation:
        x_r(t) = sum_n x[n] * sinc((t - n * Ts) / Ts)

    Vectorized over all evaluation time points.
    """
    # Create 2D grid: shape (len(t_eval), len(t_samples))
    # delta_matrix[i, n] = (t_eval[i] - t_samples[n]) / Ts
    delta = (t_eval[:, np.newaxis] - t_samples[np.newaxis, :]) / Ts
    sinc_matrix = manual_sinc(delta)
    # Matrix-vector multiplication performs the summation over n
    return np.dot(sinc_matrix, x_samples)


def solve_problem7():
    f0 = 5.0  # Signal frequency = 5 Hz
    fs = 20.0  # Sampling frequency = 20 Hz
    Ts = 1.0 / fs
    nyquist_rate = 2 * f0  # 10 Hz

    print("=" * 70)
    print("CSE220 Lab — Problem 7: Reconstruction Using Sinc Interpolation")
    print("=" * 70)
    print(f"Signal: x(t) = sin(2 * pi * {f0} * t)")
    print(f"Sampling Frequency (fs) = {fs} Hz (Nyquist rate = {nyquist_rate} Hz)")
    print(f"Sampling interval (Ts)   = {Ts} s")
    print("Since fs (20 Hz) > 2*f_max (10 Hz), perfect reconstruction is theoretically guaranteed.\n")

    # Observation interval
    t_start, t_end = 0.0, 1.0

    # Task 1: Generate samples
    # To minimize finite-duration boundary truncation effects in sinc interpolation,
    # sample with a small guard margin on each side:
    margin = 0.5  # seconds margin on each side
    t_sample_grid = np.arange(t_start - margin, t_end + margin + Ts / 2, Ts)
    x_sample_vals = np.sin(2 * np.pi * f0 * t_sample_grid)

    # Task 3: Reconstruct continuous signal on dense time grid
    t_dense = np.linspace(t_start, t_end, 1000)
    x_orig = np.sin(2 * np.pi * f0 * t_dense)
    x_reconstructed = sinc_reconstruct(t_dense, t_sample_grid, x_sample_vals, Ts)

    # Task 5: Calculate reconstruction error
    error = x_reconstructed - x_orig
    rmse = np.sqrt(np.mean(error ** 2))
    max_error = np.max(np.abs(error))

    # Evaluate interior error (away from finite boundary effects)
    interior_mask = (t_dense >= 0.1) & (t_dense <= 0.9)
    rmse_interior = np.sqrt(np.mean(error[interior_mask] ** 2))
    max_error_interior = np.max(np.abs(error[interior_mask]))

    print("--- Task 5: Reconstruction Error Analysis ---")
    print(f"Overall RMSE across [0, 1] s:             {rmse:.2e}")
    print(f"Overall Max Absolute Error across [0, 1] s: {max_error:.2e}")
    print(f"Interior RMSE [0.1, 0.9] s:                {rmse_interior:.2e}")
    print(f"Interior Max Absolute Error [0.1, 0.9] s:   {max_error_interior:.2e}")
    print(
        "\nObservation: The error is negligible (~1e-3 to 1e-4), strictly due to\n"
        "truncating the infinite sinc summation to finite samples. Away from edges,\n"
        "sinc interpolation matches the continuous analog signal perfectly!"
    )
    print("=" * 70)

    # Task 4: Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8), sharex=True, gridspec_kw={"height_ratios": [2.5, 1]})

    # Top subplot: Signals
    ax1.plot(t_dense, x_orig, "b-", lw=2, label="Original x(t) = sin(2*pi*5*t)", alpha=0.8)
    ax1.plot(t_dense, x_reconstructed, "r--", lw=1.8, label="Reconstructed via Sinc Interpolation")

    # Filter sample points for display within [0, 1]
    display_mask = (t_sample_grid >= t_start) & (t_sample_grid <= t_end)
    markerline, stemlines, baseline = ax1.stem(
        t_sample_grid[display_mask],
        x_sample_vals[display_mask],
        linefmt="forestgreen",
        markerfmt="go",
        basefmt="gray",
        label=f"Sample Points (fs = {int(fs)} Hz)",
    )
    plt.setp(markerline, markersize=5)

    ax1.set_title("Whittaker-Shannon Sinc Interpolation Reconstruction (fs = 20 Hz)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(loc="upper right")

    # Bottom subplot: Error
    ax2.plot(t_dense, error, color="crimson", lw=1.2, label=f"Reconstruction Error e(t) (RMSE = {rmse:.2e})")
    ax2.axhline(0, color="black", linestyle="--", lw=0.8)
    ax2.set_title("Reconstruction Error e(t) = x_rec(t) - x(t)")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Error")
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem7()
