# Assignment: Two Is Not Enough

## Background

The Nyquist-Shannon sampling theorem sets the floor at `2·f_max`: sample any faster than twice the highest frequency present and nothing is lost. But the theorem promises recovery by an ideal low-pass filter, which in the time domain means replacing every sample with a sinc pulse and adding them all up. That filter has infinite support and reaches backwards in time, so no converter implements it.

What converters do instead is join the dots with straight lines. And a straight line is not an ideal low-pass filter. Sampling at 2.01 times the highest frequency satisfies the theorem and still reconstructs badly, because the chord across a half-period of a sinusoid looks nothing like the sinusoid.

The fix is oversampling: sample at `k` times the Nyquist rate, with `k` large enough that consecutive samples are close enough together for a straight line between them to be a decent approximation. This is why audio converters run their internal rate far above what the theorem requires.

Your job is to find out how large `k` has to be.

## Your task

The starter file contains two functions with their bodies removed. Fill in both. `main()` is already written; do not modify it.

### Part 1 — `linear_error(f, fs, upsample)`

Measure the damage: sample the tone at `fs`, join the samples with straight lines, and return the largest absolute difference between that reconstruction and the true cosine. The docstring fixes the sample count and the fine grid; follow it exactly, or your numbers will not match.

### Part 2 — `min_oversampling(f, max_error)`

Search for the smallest integer `k ≥ 1` such that sampling at `fs = 2·k·f` keeps `linear_error` within `max_error`. A plain upward search from `k = 1` is fine.

Running `python headroom.py` should then print a table of five cases. `main()` checks each `k` twice: that it meets the target, and that `k − 1` does not, so a `k` that is merely large enough will be rejected as not minimal. The last column shows `π/√(8·target)` for comparison.


## Starter file — `headroom.py`

```python
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


```

## Expected output

```
  f (Hz)    target     k    fs (Hz)   err at k   err at k-1  pi/sqrt(8e)   result
----------------------------------------------------------------------------------
      50       0.1     4        400    0.07579      0.13067         3.51   ok
      50      0.01    12       1200    0.00852      0.01009        11.11   ok
      50     0.001    36       3600    0.00095      0.00101        35.12   ok
     440      0.01    12      10560    0.00852      0.01009        11.11   ok
    1000     0.001    36      72000    0.00095      0.00101        35.12   ok
----------------------------------------------------------------------------------

