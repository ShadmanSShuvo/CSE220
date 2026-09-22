"""Two Is Not Enough: the headroom a straight line needs.

Complete the two functions marked TODO. Do not modify anything below
the divider. Run with:  python headroom.py
"""

import numpy as np


def linear_error(f, fs, upsample):
    """Worst error when cos(2*pi*f*t + PHASE) is joined by straight lines.
    Interpolate the samples onto that grid (np.interp), and return the
    largest absolute difference from the true cosine.
    """
    raise NotImplementedError


def min_oversampling(f, max_error):
    """Smallest oversampling factor a straight-line reconstruction needs.

    Returns the smallest integer k >= 1 for which sampling at k times the
    Nyquist rate, that is at fs = 2 * k * f, keeps linear_error below or
    equal to max_error. Use UPSAMPLE for the fine grid, and give up at
    MAX_K.
    """
    raise NotImplementedError


# --------------------------------------------------------------------------
# Everything below is provided. Do not modify.
# --------------------------------------------------------------------------

PERIODS = 8        # complete periods of the tone in each record
PHASE = 0.3        # radians, so no sample lands exactly on a peak
UPSAMPLE = 64      # fine-grid steps per sample period
MAX_K = 500        # search limit

TEST_CASES = [
    # (f in Hz, largest acceptable error)
    (50, 0.1),
    (50, 0.01),
    (50, 0.001),
    (440, 0.01),
    (1000, 0.001),
]


def main():
    print(f"{'f (Hz)':>8} {'target':>9} {'k':>5} {'fs (Hz)':>10} "
          f"{'err at k':>10} {'err at k-1':>12} {'pi/sqrt(8e)':>12}   result")
    print("-" * 82)

    failures = 0
    for f, target in TEST_CASES:
        k = min_oversampling(f, target)
        fs = 2 * k * f

        at_k = linear_error(f, fs, UPSAMPLE)
        below = linear_error(f, 2 * (k - 1) * f, UPSAMPLE) if k > 1 else float("inf")

        sufficient = at_k <= target
        minimal = below > target
        ok = sufficient and minimal
        failures += not ok

        verdict = "ok" if ok else ("not enough" if not sufficient else "not minimal")
        print(f"{f:>8} {target:>9g} {k:>5} {fs:>10} {at_k:>10.5f} "
              f"{below:>12.5f} {np.pi / np.sqrt(8 * target):>12.2f}   {verdict}")

    print("-" * 82)
    if failures:
        print(f"{failures} of {len(TEST_CASES)} case(s) wrong. A correct k both "
          f"meets the target and is the smallest that does.")
    else:
        print("Every k is the smallest that meets its target.\n"
              "Note that k depends on the accuracy demanded, not on f.")


if __name__ == "__main__":
    main()
