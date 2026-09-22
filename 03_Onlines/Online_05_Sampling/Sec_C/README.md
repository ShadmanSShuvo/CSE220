# Section C: Two Is Not Enough

> **Topic:** Linear Interpolation Reconstruction, Oversampling Headroom, and Error Minimization
> **Source Problem:** [`two-is-not-enough.md`](./two-is-not-enough.md)

---

## Overview

The Nyquist-Shannon theorem guarantees lossless reconstruction if sampling rate $f_s > 2 f_{\max}$, but this guarantee assumes an **ideal low-pass filter** (sinc interpolation) with infinite support across past and future time.

Practical low-latency digital-to-analog converters approximate continuous signals using **linear interpolation (first-order hold)** — joining consecutive discrete samples with straight lines. When sampled right at the Nyquist limit ($k=1$), straight line segments fail miserably at approximating smooth sinusoidal curves.

To achieve low reconstruction error with linear interpolation, converters rely on **oversampling** at $f_s = 2 \cdot k \cdot f$ with integer factor $k \ge 1$.

This assignment determines:
1. The peak reconstruction error when a cosine $\cos(2\pi f t + \text{PHASE})$ is reconstructed via linear interpolation (`np.interp`).
2. The minimal integer oversampling factor $k \ge 1$ required to guarantee peak error remains within a specified tolerance $\epsilon$.

---

## Key Theory & Formula

### 1. Taylor Expansion Bound on Linear Interpolation Error
For linear interpolation of any twice-differentiable continuous function $x(t)$ across an interval of duration $T_s = 1/f_s$, the interpolation error is bounded by:
$$|e(t)| \le \frac{T_s^2}{8} \max_{\tau \in [0, T_s]} |x''(\tau)|$$

For $x(t) = \cos(2\pi f t + \phi)$:
$$x''(t) = -(2\pi f)^2 \cos(2\pi f t + \phi) \implies \max |x''(t)| = 4\pi^2 f^2$$

Substituting $T_s = \frac{1}{f_s} = \frac{1}{2 k f}$:
$$\text{error} \le \frac{1}{8 (2 k f)^2} (4\pi^2 f^2) = \frac{4\pi^2 f^2}{32 k^2 f^2} = \frac{\pi^2}{8 k^2}$$

### 2. Minimum Oversampling Factor $k$
To guarantee $\text{error} \le \text{target} = \epsilon$:
$$\frac{\pi^2}{8 k^2} \le \epsilon \iff k^2 \ge \frac{\pi^2}{8 \epsilon} \iff k \ge \frac{\pi}{\sqrt{8 \epsilon}}$$

**Key Insight:** Notice that $f$ cancels out entirely! The minimum required oversampling factor $k$ depends **solely on the target accuracy** $\epsilon$, and is independent of the signal frequency $f$.

---

## Implemented Functions

### 1. `linear_error(f, fs, upsample)`
- Generates samples over `PERIODS = 8` cycles:
  $$N = \text{int}\left(\text{PERIODS} \cdot \frac{f_s}{f}\right), \quad t = \frac{n}{f_s}, \quad \text{samples} = \cos(2\pi f t + \text{PHASE})$$
- Evaluates on a dense grid dividing each of the $(N-1)$ sample intervals into `upsample = 64` steps:
  $$t_{\text{fine}} = \text{np.linspace}(t[0], t[-1], (N-1) \cdot \text{upsample} + 1)$$
- Computes straight-line reconstruction using `np.interp(t_fine, t, samples)`.
- Returns maximum absolute difference: $\max |x_{\text{recon}} - x_{\text{true}}|$.

### 2. `min_oversampling(f, max_error)`
- Searches $k = 1, 2, \dots, \text{MAX\_K}$ at $f_s = 2 \cdot k \cdot f$.
- Returns the first (minimal) integer $k$ meeting `linear_error` $\le \text{max\_error}$.

---

## Test Cases & Expected Results

Fine-grid factor $\text{UPSAMPLE} = 64$, $\text{PHASE} = 0.3$:

| $f$ (Hz) | Target Error ($\epsilon$) | Minimal $k$ | $f_s$ (Hz) | Error at $k$ | Error at $k-1$ | Theoretical $\frac{\pi}{\sqrt{8\epsilon}}$ | Result |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | 0.1 | **4** | 400 | 0.07579 | 0.13067 | 3.51 | `ok` |
| 50 | 0.01 | **12** | 1200 | 0.00852 | 0.01009 | 11.11 | `ok` |
| 50 | 0.001 | **36** | 3600 | 0.00095 | 0.00101 | 35.12 | `ok` |
| 440 | 0.01 | **12** | 10560 | 0.00852 | 0.01009 | 11.11 | `ok` |
| 1000 | 0.001 | **36** | 72000 | 0.00095 | 0.00101 | 35.12 | `ok` |

---

## How to Run

```bash
# Run solution
python3 solution.py

# Or run headroom.py
python3 headroom.py
```
