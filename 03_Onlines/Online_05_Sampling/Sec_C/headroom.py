"""Two Is Not Enough: the headroom a straight line needs - Solution.

Determines the minimum oversampling factor required for linear interpolation
(first-order hold) reconstruction of a sinusoid to meet a specified error tolerance.
Run with:  python3 solution.py  or  python3 headroom.py
"""

import numpy as np


def linear_error(f, fs, upsample):
    """Worst error when cos(2*pi*f*t + PHASE) is joined by straight lines.

    Samples the tone at rate fs over a duration of PERIODS complete cycles.
    The samples are then linearly interpolated onto a fine evaluation grid
    constructed with `upsample` steps per sample period (Ts = 1/fs) using np.interp.
    Returns the maximum absolute difference between the linear reconstruction
    and the true continuous-time cosine.

    Parameters
    ----------
    f : float
        Frequency of the cosine wave in Hz.
    fs : float
        Sampling frequency in Hz.
    upsample : int
        Number of fine-grid steps per sample period.

    Returns
    -------
    float
        Largest absolute error max|recon - true|.
    """
    # Sample count covering PERIODS full cycles
    n_samples = int(PERIODS * fs / f)
    t = np.arange(n_samples) / fs
    samples = np.cos(2 * np.pi * f * t + PHASE)

    # Fine grid: (n_samples - 1) intervals, each divided into `upsample` steps
    t_fine = np.linspace(t[0], t[-1], (n_samples - 1) * upsample + 1)
    true_cosine = np.cos(2 * np.pi * f * t_fine + PHASE)

    # Linear interpolation (connecting samples with straight lines)
    reconstructed = np.interp(t_fine, t, samples)

    return float(np.max(np.abs(reconstructed - true_cosine)))


def min_oversampling(f, max_error):
    """Smallest oversampling factor a straight-line reconstruction needs.

    Returns the smallest integer k >= 1 for which sampling at k times the
    Nyquist rate, that is at fs = 2 * k * f, keeps linear_error below or
    equal to max_error. Uses UPSAMPLE for the fine grid, and gives up at
    MAX_K.

    Theoretical Context:
    For linear interpolation of x(t) = cos(2*pi*f*t + phi), the maximum
    interpolation error on an interval of length Ts = 1/fs is bounded by:
        error <= (Ts^2 / 8) * max|x''(t)|
    Since max|x''(t)| = (2*pi*f)^2 and Ts = 1 / (2*k*f), we have:
        error <= (1 / (8 * 4 * k^2 * f^2)) * 4 * pi^2 * f^2 = pi^2 / (8 * k^2)
    Requiring error <= max_error yields:
        k >= pi / sqrt(8 * max_error)
    This explains why the minimum required factor k depends on the desired
    accuracy tolerance, but is independent of frequency f.

    Parameters
    ----------
    f : float
        Frequency of the cosine wave in Hz.
    max_error : float
        Maximum acceptable peak error.

    Returns
    -------
    int
        Smallest integer k >= 1 satisfying the error bound, up to MAX_K.
    """
    for k in range(1, MAX_K + 1):
        fs = 2 * k * f
        err = linear_error(f, fs, UPSAMPLE)
        if err <= max_error:
            return k
    return MAX_K


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
