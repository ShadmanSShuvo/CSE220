"""
Solution for Online 02 Convolution - Section A1, A2
Tests Linearity and Time-Invariance on System A (LTI) and System B (Time-varying).
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


# ---- Generic property testers ----

def test_linearity(apply_system, x1, x2, a, b):
    """Return max| apply_system(a*x1 + b*x2)  -  (a*apply_system(x1) + b*apply_system(x2)) |"""
    # Left side: T{a*x1 + b*x2}
    ax1_plus_bx2 = x1.multiply(a).add(x2.multiply(b))
    y_lhs = apply_system(ax1_plus_bx2)

    # Right side: a*T{x1} + b*T{x2}
    y_x1 = apply_system(x1)
    y_x2 = apply_system(x2)
    y_rhs = y_x1.multiply(a).add(y_x2.multiply(b))

    return max_absolute_difference(y_lhs, y_rhs)


def test_time_invariance(apply_system, x, k):
    """Return max| apply_system(x shifted by k)  -  (apply_system(x) shifted by k) |"""
    # Left side: T{x[n - k]}
    x_shifted = x.shift(k)
    y_lhs = apply_system(x_shifted)

    # Right side: y[n - k] where y[n] = T{x[n]}
    y_unshifted = apply_system(x)
    y_rhs = y_unshifted.shift(k)

    return max_absolute_difference(y_lhs, y_rhs)


# ---- System B: y[n] = n * x[n] ----

def system_b(input_signal):
    """Build and return a DiscreteSignal where output[n] = n * input_signal[n]"""
    output_signal = DiscreteSignal(input_signal.start_time, input_signal.end_time)
    for n in input_signal.times():
        output_signal.set_value_at_time(n, n * input_signal.get_value_at_time(n))
    return output_signal


def main():
    tolerance = 1e-9

    # ---- Given signals and scalars (do not change) ----
    x1 = make_signal(-2, 2, [1, 0, 2, -1, 3])
    x2 = make_signal(-1, 3, [2, -3, 0, 1, 1])
    a, b = 2.0, -3.0
    k = 3

    h = make_signal(0, 2, [1.0, 0.5, 0.25])
    system_a = LTISystem(h)

    print("=== System A: genuine LTI system (LTISystem.output) ===")
    diff_linear_a = test_linearity(system_a.output, x1, x2, a, b)
    diff_ti_a = test_time_invariance(system_a.output, x1, k)
    print(f"Linearity max diff:        {diff_linear_a:.2e}")
    print(f"Time-invariance max diff:  {diff_ti_a:.2e}")
    print(f"System A is Linear:         {diff_linear_a < tolerance}")
    print(f"System A is Time-Invariant: {diff_ti_a < tolerance}")

    print()

    print("=== System B: y[n] = n * x[n] ===")
    diff_linear_b = test_linearity(system_b, x1, x2, a, b)
    diff_ti_b = test_time_invariance(system_b, x1, k)
    print(f"Linearity max diff:        {diff_linear_b:.2e}")
    print(f"Time-invariance max diff:  {diff_ti_b:.2e}")
    print(f"System B is Linear:         {diff_linear_b < tolerance}")
    print(f"System B is Time-Invariant: {diff_ti_b < tolerance}")

    print()
    # Conclusion
    if diff_linear_b < tolerance and diff_ti_b >= tolerance:
        print("Conclusion: System B satisfies Linearity, but FAILS Time-Invariance.")
        print("Because the time-varying scaling factor n depends explicitly on the time index, System B is a time-varying linear system.")
    elif diff_linear_b >= tolerance and diff_ti_b < tolerance:
        print("Conclusion: System B fails Linearity, but satisfies Time-Invariance.")
    else:
        print("Conclusion: System B fails both Linearity and Time-Invariance.")


if __name__ == "__main__":
    main()
