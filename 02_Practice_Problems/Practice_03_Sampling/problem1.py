"""
Problem 1: Basic Sampling of a Sinusoid
=======================================

Problem Statement:
------------------
Given:
    x(t) = sin(2 * pi * 5 * t)

Sample the signal at:
    * f_s = 50 Hz
    * f_s = 10 Hz
    * f_s = 7 Hz

Tasks:
------
1. Generate the continuous-time approximation.
2. Generate the sampled signals.
3. Plot all three cases.
4. Determine which sampling frequencies satisfy the Nyquist criterion.
5. Explain what happens when f_s < 2 * f_max.
"""

import numpy as np
import matplotlib.pyplot as plt


def solve_problem1():
    # Signal parameters
    f0 = 5.0  # Signal frequency in Hz
    f_max = f0
    nyquist_rate = 2 * f_max  # Nyquist rate = 10 Hz

    duration = 1.0  # 1 second duration
    sampling_rates = [50, 10, 7]  # in Hz

    # Task 1: Generate continuous-time approximation (dense grid)
    f_cont = 2000  # High sampling rate to simulate continuous time
    t_cont = np.linspace(0, duration, int(f_cont * duration) + 1)
    x_cont = np.sin(2 * np.pi * f0 * t_cont)

    print("=" * 60)
    print("CSE220 Lab — Problem 1: Basic Sampling of a Sinusoid")
    print("=" * 60)
    print(f"Original Signal: x(t) = sin(2 * pi * {f0} * t)")
    print(f"Maximum frequency (f_max) = {f_max} Hz")
    print(f"Nyquist Rate (2 * f_max)   = {nyquist_rate} Hz\n")

    # Task 2 & 3: Sample the signals and plot
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    for idx, fs in enumerate(sampling_rates):
        Ts = 1.0 / fs
        t_sample = np.arange(0, duration + Ts / 2, Ts)
        x_sample = np.sin(2 * np.pi * f0 * t_sample)

        ax = axes[idx]
        # Continuous-time approximation
        ax.plot(t_cont, x_cont, label="Continuous x(t)", color="royalblue", alpha=0.7, lw=1.5)
        # Discrete sampled points
        markerline, stemlines, baseline = ax.stem(
            t_sample,
            x_sample,
            linefmt="crimson",
            markerfmt="ro",
            basefmt="gray",
            label=f"Sampled points (fs={fs} Hz)",
        )
        plt.setp(markerline, markersize=4)

        # Plot apparent alias if fs < Nyquist
        if fs < nyquist_rate:
            f_alias = abs(f0 - fs)
            # sin(2*pi*5*n/7) = sin(2*pi*(7-2)*n/7) = -sin(2*pi*2*n/7) = sin(2*pi*2*n/7 + pi)
            x_alias = np.sin(2 * np.pi * f_alias * t_cont + np.pi)
            ax.plot(
                t_cont,
                x_alias,
                "--",
                color="darkorange",
                lw=1.8,
                label=f"Apparent Alias ({f_alias} Hz)",
            )

        ax.set_title(f"Sampling at fs = {fs} Hz")
        ax.set_ylabel("Amplitude")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(loc="upper right")

    axes[-1].set_xlabel("Time (seconds)")
    plt.tight_layout()

    # Task 4: Determine which sampling frequencies satisfy the Nyquist criterion
    print("--- Task 4: Nyquist Criterion Evaluation ---")
    for fs in sampling_rates:
        if fs > nyquist_rate:
            status = f"Satisfies Nyquist criterion (fs = {fs} Hz > 2*f_max = {nyquist_rate} Hz) -> Oversampled, no aliasing."
        elif fs == nyquist_rate:
            status = (
                f"Borderline / Critical Nyquist rate (fs = {fs} Hz == 2*f_max = {nyquist_rate} Hz).\n"
                f"  NOTE: Because x(t) = sin(2*pi*5*t), sampling at t = n*(1/10) gives sin(n*pi) = 0 for all n!\n"
                f"  The samples evaluate to identically 0, illustrating why strictly fs > 2*f_max is needed."
            )
        else:
            status = f"Violates Nyquist criterion (fs = {fs} Hz < 2*f_max = {nyquist_rate} Hz) -> Undersampled, aliasing occurs."
        print(f"* fs = {fs:2d} Hz: {status}")

    # Task 5: Explanation of undersampling (fs < 2*f_max)
    print("\n--- Task 5: Theoretical Explanation ---")
    print(
        "When fs < 2 * f_max (Nyquist criterion violated):\n"
        "1. High-frequency components cannot be uniquely distinguished from lower frequencies.\n"
        "2. The signal folds into the baseband (-fs/2 to +fs/2), creating an 'alias' frequency.\n"
        f"3. For f = 5 Hz and fs = 7 Hz: f_alias = |5 - 7| = 2 Hz.\n"
        "4. As seen in the bottom plot, the discrete samples taken from the 5 Hz wave\n"
        "   lie precisely on an apparent 2 Hz sinusoid with a phase shift of 180 degrees.\n"
        "5. Perfect reconstruction of the original signal is impossible once aliasing occurs."
    )
    print("=" * 60)

    plt.show()


if __name__ == "__main__":
    solve_problem1()
