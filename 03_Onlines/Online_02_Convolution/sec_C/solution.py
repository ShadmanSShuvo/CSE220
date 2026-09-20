"""
Solution for Online 02 Convolution - Section C1, C2
Computes system output via block-by-block operations and via a single combined impulse response,
and verifies both produce identical results.
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
    """Helper: build a DiscreteSignal from a list of values"""
    signal = DiscreteSignal(start_time, end_time)
    for offset, value in enumerate(values):
        signal.set_value_at_time(start_time + offset, value)
    return signal


def max_absolute_difference(first_signal, second_signal):
    """Helper: largest |difference| between two signals over their combined range."""
    start = min(first_signal.start_time, second_signal.start_time)
    end = max(first_signal.end_time, second_signal.end_time)
    max_diff = 0.0
    for n in range(start, end + 1):
        diff = abs(first_signal.get_value_at_time(n) - second_signal.get_value_at_time(n))
        if diff > max_diff:
            max_diff = diff
    return float(max_diff)


def main():
    # ---- Given: input signal and impulse responses (do not change) ----
    x = make_signal(-2, 4, [0, 0, 1, 0, -1, 0, 0])
    x.plot("Input signal x[n]", save_path="input_x.png")

    h1 = make_signal(0, 0, [1.0])
    h2 = make_signal(1, 1, [0.5])
    h3 = make_signal(0, 1, [1.0, 1.0])
    h4 = make_signal(0, 1, [0.7, -0.2])
    h5 = make_signal(0, 2, [0.5, 0.2, -0.1])

    # ---- Part 1: block-by-block output ----
    # According to the block diagram:
    # Path 1: x -> h1
    # Path 2: x -> h2
    # Combined at adder: w1 = (x * h1) + (x * h2)
    # Then through h3: w2 = w1 * h3 = ((x * h1) + (x * h2)) * h3
    # Path 3: x -> h4 -> h5: w3 = (x * h4) * h5
    # Final output at second adder (+ from w2, - from w3): y_block = w2 - w3

    sys1 = LTISystem(h1)
    sys2 = LTISystem(h2)
    sys3 = LTISystem(h3)
    sys4 = LTISystem(h4)
    sys5 = LTISystem(h5)

    y_h1 = sys1.output(x)
    y_h2 = sys2.output(x)
    w1 = y_h1.add(y_h2)
    w2 = sys3.output(w1)

    w3_step1 = sys4.output(x)
    w3 = sys5.output(w3_step1)

    y_block = w2.add(w3.multiply(-1.0))
    y_block.plot("Output via block-by-block system", save_path="y_block.png")

    # ---- Part 2: h_combined ----
    # Single equivalent impulse response:
    # h_combined = (h1 + h2) * h3 - (h4 * h5)
    h12 = h1.add(h2)
    h_upper = sys3.output(h12)
    h_lower = sys5.output(h4)
    h_combined = h_upper.add(h_lower.multiply(-1.0))

    sys_combined = LTISystem(h_combined)
    y_combined = sys_combined.output(x)
    y_combined.plot("Output via combined impulse response", save_path="y_combined.png")

    # ---- Part 3: verification ----
    max_diff = max_absolute_difference(y_block, y_combined)
    print(f"Maximum absolute difference: {max_diff:.2e}")
    print("Outputs match:", max_diff < 1e-9)

    print("\nSample values of y_block:")
    for t in y_block.times():
        print(f"n={t:2d}: {y_block.get_value_at_time(t):.4f}")

    print("\nSample values of y_combined:")
    for t in y_combined.times():
        print(f"n={t:2d}: {y_combined.get_value_at_time(t):.4f}")


if __name__ == "__main__":
    main()
