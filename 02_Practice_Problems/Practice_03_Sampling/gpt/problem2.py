"""
Problem 2: Nyquist Rate Detection
=================================

Problem Statement:
------------------
Consider:
    x(t) = sin(2 * pi * 10 * t) + 0.5 * sin(2 * pi * 25 * t)

Tasks:
------
1. Determine the highest frequency component.
2. Calculate the Nyquist rate.
3. Sample the signal at f_s = 100, 50, 40, and 30 Hz.
4. Plot the sampled signals.
5. Identify the cases where aliasing occurs.
"""

import numpy as np
import matplotlib.pyplot as plt


def solve_problem2():
    # Signal definition
    f1 = 10.0  # Component 1 frequency in Hz
    a1 = 1.0
    f2 = 25.0  # Component 2 frequency in Hz
    a2 = 0.5

    def x_signal(t):
        return a1 * np.sin(2 * np.pi * f1 * t) + a2 * np.sin(2 * np.pi * f2 * t)

    # Task 1: Determine the highest frequency component
    f_max = max(f1, f2)

    # Task 2: Calculate the Nyquist rate
    nyquist_rate = 2 * f_max

    print("=" * 65)
    print("CSE220 Lab — Problem 2: Nyquist Rate Detection")
    print("=" * 65)
    print(f"Signal: x(t) = {a1}*sin(2*pi*{f1}*t) + {a2}*sin(2*pi*{f2}*t)")
    print(f"1. Individual frequencies: f1 = {f1} Hz, f2 = {f2} Hz")
    print(f"   Highest frequency component (f_max) = {f_max} Hz")
    print(f"2. Nyquist rate (2 * f_max) = {nyquist_rate} Hz\n")

    # Task 3: Sample the signal at fs = 100, 50, 40, and 30 Hz
    sampling_rates = [100, 50, 40, 30]
    duration = 0.5  # 0.5 seconds for clear visualization of cycles

    t_cont = np.linspace(0, duration, 2000)
    x_cont = x_signal(t_cont)

    # Task 4: Plot the sampled signals
    fig, axes = plt.subplots(4, 1, figsize=(11, 10), sharex=True)

    print("--- Task 5: Aliasing Identification ---")
    for idx, fs in enumerate(sampling_rates):
        Ts = 1.0 / fs
        t_sample = np.arange(0, duration + Ts / 2, Ts)
        x_sample = x_signal(t_sample)

        # Theoretical alias analysis
        fn = fs / 2.0  # Nyquist frequency / folding frequency
        # Check component 1
        c1_alias = abs(f1 - fs * round(f1 / fs))
        # Check component 2
        c2_alias = abs(f2 - fs * round(f2 / fs))

        aliased = (fs < nyquist_rate)
        if fs > nyquist_rate:
            status = f"No aliasing. fs ({fs} Hz) > Nyquist rate ({nyquist_rate} Hz)."
        elif fs == nyquist_rate:
            status = (
                f"Critical Nyquist rate (fs = {fs} Hz). Notice the 25 Hz component\n"
                f"       falls exactly at fs/2 = 25 Hz. Since sin(25*2*pi*n/50) = sin(n*pi) = 0,\n"
                f"       the 25 Hz component disappears entirely from the samples!"
            )
        else:
            status = (
                f"Aliasing OCCURS! fs ({fs} Hz) < Nyquist rate ({nyquist_rate} Hz).\n"
                f"       * 10 Hz component appears at {c1_alias} Hz (f1 <= fn = {fn} Hz)\n"
                f"       * 25 Hz component aliases to {c2_alias} Hz (f2 > fn = {fn} Hz)"
            )

        print(f"* fs = {fs:3d} Hz (Folding freq fn = {fn:4.1f} Hz):\n       {status}\n")

        ax = axes[idx]
        ax.plot(t_cont, x_cont, label="Continuous x(t)", color="royalblue", alpha=0.6, lw=1.5)
        markerline, stemlines, baseline = ax.stem(
            t_sample,
            x_sample,
            linefmt="crimson",
            markerfmt="ro",
            basefmt="gray",
            label=f"Sampled points (fs={fs} Hz)",
        )
        plt.setp(markerline, markersize=4)

        ax.set_title(f"Sampling at fs = {fs} Hz (fn = {fn:.1f} Hz) | {'ALIASED' if fs < nyquist_rate else 'NO ALIASING'}")
        ax.set_ylabel("Amplitude")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(loc="upper right")

    axes[-1].set_xlabel("Time (seconds)")
    plt.tight_layout()
    print("=" * 65)

    plt.show()


if __name__ == "__main__":
    solve_problem2()
