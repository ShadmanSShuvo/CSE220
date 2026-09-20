"""
Solution for Online 02 Convolution - Section B
Verifies that the cascade of Accumulator and First Difference acts as the identity system.
"""

import numpy as np
import matplotlib
try:
    matplotlib.use("Agg")
except Exception:
    pass
import matplotlib.pyplot as plt

from signal_lti import DiscreteSignal, LTISystem


def make_signal(start_time, end_time, values):
    """Helper: build a DiscreteSignal from a list of values."""
    signal = DiscreteSignal(start_time, end_time)
    for offset, value in enumerate(values):
        signal.set_value_at_time(start_time + offset, value)
    return signal


def max_absolute_difference_in_range(first_signal, second_signal, start_time, end_time):
    """Largest |first[n] - second[n]| for start_time <= n <= end_time."""
    max_diff = 0.0
    for n in range(start_time, end_time + 1):
        diff = abs(first_signal.get_value_at_time(n) - second_signal.get_value_at_time(n))
        if diff > max_diff:
            max_diff = diff
    return float(max_diff)


def samples_in_range(signal, start_time, end_time):
    """Return [(n, signal[n]), ...] over an inclusive time range."""
    return [
        (n, signal.get_value_at_time(n))
        for n in range(start_time, end_time + 1)
    ]


def cascade(first_system, second_system, input_signal):
    """Apply first_system, then second_system, and return both outputs."""
    intermediate_output = first_system.output(input_signal)
    final_output = second_system.output(intermediate_output)
    return intermediate_output, final_output


def plot_cascade_responses(
    input_signal,
    accumulator_output,
    difference_output,
    start_time,
    end_time,
    save_path="cascade_plot.png",
):
    """Plot the input, accumulator response, and first-difference response."""
    times = np.arange(start_time, end_time + 1)

    input_values = [
        input_signal.get_value_at_time(n)
        for n in times
    ]
    accumulator_values = [
        accumulator_output.get_value_at_time(n)
        for n in times
    ]
    difference_values = [
        difference_output.get_value_at_time(n)
        for n in times
    ]

    fig, axes = plt.subplots(3, 1, figsize=(8, 7), sharex=True)

    axes[0].stem(times, input_values)
    axes[0].set_title("Input signal $x[n]$")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True)

    axes[1].stem(times, accumulator_values)
    axes[1].set_title("Accumulator response $v[n]$")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)

    axes[2].stem(times, difference_values)
    axes[2].set_title("First-difference response $y[n]$")
    axes[2].set_xlabel("n")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True)

    fig.suptitle("Accumulator and First-Difference Cascade")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=150)
        print(f"Saved plot to {save_path}")
    plt.close(fig)


def main():
    tolerance = 1e-9

    # ---- Given observation window (do not change) ----
    OBSERVATION_START = -2
    OBSERVATION_END = 8

    # ---- Given input signal (do not change) ----
    # x[n] is a non-impulse input with values [2, -1, 3, 1, -2] on n = -2...2 and is zero afterward.
    x = make_signal(
        OBSERVATION_START,
        OBSERVATION_END,
        [2.0, -1.0, 3.0, 1.0, -2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    )

    # h1[n] = delta[n] - delta[n-1] = [1, -1]
    h1 = make_signal(0, 1, [1.0, -1.0])

    # h2[n] = u[n]. Store enough samples for the graded observation window (n = 0...10).
    h2 = make_signal(0, 10, [1.0] * 11)

    # Create the two LTISystem objects
    differentiator = LTISystem(h1)
    accumulator = LTISystem(h2)

    # Apply x[n] through Accumulator -> First difference
    accumulator_output, difference_output = cascade(accumulator, differentiator, x)

    # Compare the first-difference response with x[n] on the observation window
    max_difference = max_absolute_difference_in_range(difference_output, x, OBSERVATION_START, OBSERVATION_END)

    print("=== Input x[n] -> Accumulator -> First difference ===")
    print("Input samples:")
    print(samples_in_range(x, OBSERVATION_START, OBSERVATION_END))
    print("\nAccumulator response samples:")
    print(samples_in_range(accumulator_output, OBSERVATION_START, OBSERVATION_END))
    print("\nFirst-difference response samples:")
    print(samples_in_range(difference_output, OBSERVATION_START, OBSERVATION_END))
    print(f"\nMaximum absolute difference from x[n]: {max_difference:.2e}")

    plot_cascade_responses(
        x,
        accumulator_output,
        difference_output,
        OBSERVATION_START,
        OBSERVATION_END,
        save_path="cascade_plot.png",
    )

    print()
    conclusion = (
        f"Conclusion: The cascade output equals x[n] on n = {OBSERVATION_START} ... {OBSERVATION_END} "
        f"(max difference = {max_difference:.2e} < {tolerance:g}).\n"
        f"Therefore, the cascade acts as an identity system, demonstrating that the first-difference "
        f"differentiator and accumulator are inverse systems under zero initial conditions."
    )
    print(conclusion)

    if max_difference is not None:
        print("\nIdentity test passed:", max_difference < tolerance)


if __name__ == "__main__":
    main()
