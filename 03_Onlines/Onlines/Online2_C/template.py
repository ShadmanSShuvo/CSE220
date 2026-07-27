"""
Instructions:
- x[n] and the four impulse responses h1..h4 are already given below.
- Complete the TODOs
- Do NOT use numpy.convolve / scipy.signal / any built-in convolution.
"""

import numpy as np
import matplotlib.pyplot as plt


def make_signal(start_time, end_time, values):
    """Helper: build a DiscreteSignal from a list of values"""
    signal = DiscreteSignal(start_time, end_time)
    for offset, value in enumerate(values):
        signal.set_value_at_time(start_time + offset, value)
    return signal


def max_absolute_difference(first_signal, second_signal):
    """Helper: largest |difference| between two signals over their combined range."""
    # TODO: reuse your offline implementation of this function.
    raise NotImplementedError


def main():
    # ---- Given: input signal and impulse responses (do not change) ----
    x = make_signal(-2, 4, [0, 0, 1, 0, -1, 0, 0])
    # TODO: plot input signal

    h1 = make_signal(0, 0, [1])
    h2 = make_signal(1, 1, [0.5])
    h3 = make_signal(0, 1, [1, 1])
    h4 = make_signal(0, 1, [0.7, -0.2])
    h5 = make_signal(0, 2, [0.5, 0.2, -0.1])


    # TODO: ---- Part 1: block-by-block output ----

    y_block = None
    y_block.plot("Output via block-by-block system")

    # TODO: ---- Part 2: h_combined ----

    h_combined = None

    # TODO: y_combined
    y_combined = None
    y_combined.plot("Output via combined impulse response")

    # TODO: ---- Part 3: verification ----

    max_diff = None
    print("Maximum absolute difference:", max_diff)
    print("Outputs match:", max_diff < 1e-9)


if __name__ == "__main__":
    main()
