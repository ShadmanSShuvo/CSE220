"""
Problem 15: Sampling + Quantization
===================================

Problem Statement:
------------------
Generate:
    x(t) = sin(2 * pi * 5 * t).

Sample it at f_s = 50 Hz and quantize the samples using:
    * 2 bits
    * 3 bits
    * 4 bits
    * 8 bits

Tasks:
------
1. Plot the quantized signals.
2. Calculate quantization error: e[n] = x_q[n] - x[n].
3. Calculate Mean Squared Error (MSE).
4. Compare the effect of increasing the number of bits.

This introduces the distinction between sampling (time discretization) and
quantization (amplitude discretization).
"""

import numpy as np
import matplotlib.pyplot as plt


def quantize_signal(x, bits):
    """
    Performs uniform mid-riser quantization over the dynamic range [-1, 1].

    Parameters:
        x    : array_like, input samples in range [-1, 1]
        bits : int, number of quantization bits (levels = 2^bits)

    Returns:
        x_q  : ndarray, quantized values
        delta: float, step size
    """
    levels = 2 ** bits
    delta = 2.0 / levels  # Step size across full range [-1, 1]
    # Map [-1, 1] to indices 0 to levels-1
    indices = np.floor((x + 1.0) / delta).astype(int)
    indices = np.clip(indices, 0, levels - 1)
    # Quantized value is the center of each bin (mid-riser)
    x_q = -1.0 + (indices + 0.5) * delta
    return x_q, delta


def solve_problem15():
    f0 = 5.0   # Signal frequency = 5 Hz
    fs = 50.0  # Sampling rate = 50 Hz
    Ts = 1.0 / fs
    duration = 0.6  # 3 full cycles

    bit_depths = [2, 3, 4, 8]

    # Continuous reference
    t_cont = np.linspace(0, duration, 2000)
    x_cont = np.sin(2 * np.pi * f0 * t_cont)

    # Sampled signal (time discretization)
    t_samples = np.arange(0, duration + Ts / 2, Ts)
    x_samples = np.sin(2 * np.pi * f0 * t_samples)
    P_signal = np.mean(x_samples ** 2)  # Theoretical power = 0.5

    print("=" * 80)
    print("CSE220 Lab — Problem 15: Sampling + Quantization")
    print("=" * 80)
    print(f"Signal: x(t) = sin(2*pi*{f0}*t), fs = {fs} Hz")
    print("Sampling converts continuous time into discrete time:   x(t) -> x[n]")
    print("Quantization converts continuous amplitude into discrete levels: x[n] -> x_q[n]\n")

    print(f"{'Bits':>4} | {'Levels':>6} | {'Step Size (Delta)':>18} | {'Experimental MSE':>18} | {'Theoretical MSE':>16} | {'SQNR (dB)':>10}")
    print("-" * 80)

    results = []

    for b in bit_depths:
        x_q, delta = quantize_signal(x_samples, b)
        error = x_q - x_samples
        mse_exp = np.mean(error ** 2)
        mse_theo = (delta ** 2) / 12.0
        sqnr_db = 10 * np.log10(P_signal / mse_exp) if mse_exp > 0 else float("inf")

        results.append({
            "bits": b,
            "levels": 2 ** b,
            "delta": delta,
            "x_q": x_q,
            "error": error,
            "mse_exp": mse_exp,
            "mse_theo": mse_theo,
            "sqnr_db": sqnr_db,
        })

        print(
            f"{b:>4d} | {2**b:>6d} | {delta:>18.5f} | {mse_exp:>18.5e} | {mse_theo:>16.5e} | {sqnr_db:>10.2f}"
        )

    print("=" * 80)
    print("\n--- Task 4: Observations & Comparison ---")
    print("1. Relationship between Bits and Step Size (Delta):")
    print("   Each additional bit doubles the number of quantization levels (2^B) and HALVES the step size.")
    print("2. Effect on Mean Squared Error (MSE):")
    print("   Since MSE ~ Delta^2 / 12, adding 1 bit reduces the noise power by a factor of 4 (~6.02 dB improvement).")
    print(f"   - 2 bits (4 levels) MSE:   {results[0]['mse_exp']:.2e}  (Coarse staircase approximation)")
    print(f"   - 8 bits (256 levels) MSE: {results[3]['mse_exp']:.2e}  (Visually indistinguishable from analog)")
    print("3. Rule of thumb for sinusoidal SQNR: SQNR ~ 6.02 * B + 1.76 dB.")
    print("=" * 80)

    # Visualization
    fig, axes = plt.subplots(4, 2, figsize=(14, 11), sharex=True)

    for i, res in enumerate(results):
        b = res["bits"]
        x_q = res["x_q"]
        err = res["error"]

        # Left column: Quantized signal vs original
        ax_sig = axes[i, 0]
        ax_sig.plot(t_cont, x_cont, color="royalblue", alpha=0.5, lw=1.2, label="Original x(t)")
        # Plot staircase for quantization
        ax_sig.step(t_samples, x_q, where="mid", color="crimson", lw=1.5, label=f"{b}-bit Quantized ({res['levels']} levels)")
        ax_sig.scatter(t_samples, x_q, color="crimson", s=15, zorder=5)

        ax_sig.set_title(f"{b}-Bit Quantization ({res['levels']} levels, Delta = {res['delta']:.3f})")
        ax_sig.set_ylabel("Amplitude")
        ax_sig.grid(True, linestyle="--", alpha=0.5)
        ax_sig.legend(loc="upper right", fontsize=8)

        # Right column: Quantization error e[n]
        ax_err = axes[i, 1]
        markerline, stemlines, baseline = ax_err.stem(
            t_samples,
            err,
            linefmt="darkorange",
            markerfmt="o",
            basefmt="gray",
            label=f"Error e[n] (MSE={res['mse_exp']:.2e})",
        )
        plt.setp(markerline, markersize=3, color="darkorange")
        ax_err.axhline(res["delta"] / 2, color="red", linestyle=":", alpha=0.7, label="+/- Delta / 2")
        ax_err.axhline(-res["delta"] / 2, color="red", linestyle=":", alpha=0.7)

        ax_err.set_title(f"{b}-Bit Error | MSE = {res['mse_exp']:.2e} | SQNR = {res['sqnr_db']:.1f} dB")
        ax_err.set_ylabel("Error")
        ax_err.grid(True, linestyle="--", alpha=0.5)
        ax_err.legend(loc="upper right", fontsize=8)

    axes[-1, 0].set_xlabel("Time (seconds)")
    axes[-1, 1].set_xlabel("Time (seconds)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_problem15()
