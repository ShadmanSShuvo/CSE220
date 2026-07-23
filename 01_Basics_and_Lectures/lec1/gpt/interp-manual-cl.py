"""
Manual interpolation of a discrete-time signal x[n] to reconstruct
an approximate continuous-time signal x(t), WITHOUT using
np.interp / scipy.interpolate.

Implements:
  1. Manual linear interpolation
  2. Manual zero-order hold (sample-and-hold) reconstruction
  3. Manual nearest-neighbor interpolation
"""

import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Discrete samples: n (integer indices) and x[n] (values)
# ----------------------------------------------------------------------
n = np.array([0, 1, 2, 3, 4, 5])
xn = np.array([1, -2, 2, -1, 3, 0], dtype=float)


# ----------------------------------------------------------------------
# 1. Manual linear interpolation
# ----------------------------------------------------------------------
def linear_interp_manual(t_query, n_samples, x_samples):
    """
    For each point in t_query, manually find the two neighboring
    samples n_samples[i] <= t < n_samples[i+1] and linearly interpolate.

    Equivalent to np.interp, but done by hand.
    """
    t_query = np.atleast_1d(t_query).astype(float)
    y = np.zeros_like(t_query)

    for idx, t in enumerate(t_query):
        # Clamp to the edges (like np.interp default behavior)
        if t <= n_samples[0]:
            y[idx] = x_samples[0]
            continue
        if t >= n_samples[-1]:
            y[idx] = x_samples[-1]
            continue

        # Find the interval [n_samples[i], n_samples[i+1]] containing t
        for i in range(len(n_samples) - 1):
            x0, x1 = n_samples[i], n_samples[i + 1]
            if x0 <= t <= x1:
                y0, y1 = x_samples[i], x_samples[i + 1]
                # Linear interpolation formula:
                # y = y0 + (y1 - y0) * (t - x0) / (x1 - x0)
                frac = (t - x0) / (x1 - x0)
                y[idx] = y0 + frac * (y1 - y0)
                break

    return y


# ----------------------------------------------------------------------
# 2. Manual zero-order hold (step/staircase reconstruction)
# ----------------------------------------------------------------------
def zoh_interp_manual(t_query, n_samples, x_samples):
    """
    Holds each sample's value constant until the next sample index.
    x_reconstructed(t) = x[n]  for  n <= t < n+1
    """
    t_query = np.atleast_1d(t_query).astype(float)
    y = np.zeros_like(t_query)

    for idx, t in enumerate(t_query):
        if t < n_samples[0]:
            y[idx] = x_samples[0]
            continue
        if t >= n_samples[-1]:
            y[idx] = x_samples[-1]
            continue

        for i in range(len(n_samples) - 1):
            if n_samples[i] <= t < n_samples[i + 1]:
                y[idx] = x_samples[i]
                break

    return y


# ----------------------------------------------------------------------
# 3. Manual nearest-neighbor interpolation
# ----------------------------------------------------------------------
def nearest_interp_manual(t_query, n_samples, x_samples):
    """
    Picks the value of whichever sample index is closest to t.
    """
    t_query = np.atleast_1d(t_query).astype(float)
    y = np.zeros_like(t_query)

    for idx, t in enumerate(t_query):
        # Manually compute distances to all sample points
        distances = np.abs(n_samples - t)
        closest_i = np.argmin(distances)   # index of smallest distance
        y[idx] = x_samples[closest_i]

    return y


# ----------------------------------------------------------------------
# Demo: compare all three against the discrete samples
# ----------------------------------------------------------------------
def demo():
    t_dense = np.linspace(n[0], n[-1], 500)

    y_linear = linear_interp_manual(t_dense, n, xn)
    y_zoh = zoh_interp_manual(t_dense, n, xn)
    y_nearest = nearest_interp_manual(t_dense, n, xn)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)

    for ax, y, title in zip(
        axes,
        [y_linear, y_zoh, y_nearest],
        ["Manual Linear Interpolation", "Manual Zero-Order Hold", "Manual Nearest-Neighbor"]
    ):
        ax.stem(n, xn, linefmt="C1-", markerfmt="C1o", basefmt=" ", label="x[n] samples")
        ax.plot(t_dense, y, "C0-", lw=2, label="reconstructed x(t)")
        ax.set_title(title)
        ax.set_xlabel("t / n")
        ax.grid(alpha=0.3)
        ax.legend()

    axes[0].set_ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/manual_interpolation_demo.png", dpi=150)
    plt.show()

    # Sanity check: interpolated value AT the sample points should equal x[n]
    y_check = linear_interp_manual(n.astype(float), n, xn)
    print("Linear interp at sample points:", y_check)
    print("Original samples:              ", xn)
    print("Match:", np.allclose(y_check, xn))


if __name__ == "__main__":
    demo()