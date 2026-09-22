# Section A: Two Tones, One Sample Set

> **Topic:** Aliasing, Frequency Folding, and Ambiguity in Sampled Cosines
> **Source Problem:** [`Two_Tones_One_Sample_Set.md`](./Two_Tones_One_Sample_Set.md)

---

## Overview

Sampling a sinusoid at rate $f_s$ cannot distinguish between frequency $f$ and frequencies of the form $| \pm f + k f_s |$ for integer $k$. Because of this periodic spectral replication, every tone has alias partner frequencies that produce **numerically identical** discrete sample values when evaluated on the uniform grid $t_n = n / f_s$.

This assignment demonstrates:
1. Identifying the lowest positive partner frequency $f_2 \ne f_1$ that produces identical discrete samples.
2. Empirically sampling both cosines and verifying that the maximum difference between their sample arrays is negligible ($< 10^{-9}$, bounded only by floating-point precision).

---

## Key Theory & Formula

For a cosine tone $x(t) = \cos(2\pi f t)$ sampled at rate $f_s$ where $0 < f < \frac{f_s}{2}$:
- The alias frequencies in the continuous domain are given by:
  $$f_{\text{alias}} = | \pm f + k f_s |, \quad k \in \mathbb{Z}$$
- For $k = 1$ using the $-f$ branch:
  $$f_{\text{partner}} = f_s - f$$
- Proof of identical samples:
  $$\cos\left(2\pi(f_s - f)\frac{n}{f_s}\right) = \cos(2\pi n - 2\pi f \frac{n}{f_s}) = \cos\left(-2\pi f \frac{n}{f_s}\right) = \cos\left(2\pi f \frac{n}{f_s}\right)$$

---

## Implemented Functions

### 1. `lowest_alias_pair(f, fs)`
Returns the smallest positive frequency partner:
$$\text{return } f_s - f$$

### 2. `max_sample_difference(f1, f2, fs, duration)`
1. Computes total samples: $N = \text{int}(\text{duration} \cdot f_s)$.
2. Generates time vector: $t = n / f_s$ for $n = 0, \dots, N - 1$.
3. Evaluates $s_1 = \cos(2\pi f_1 t)$ and $s_2 = \cos(2\pi f_2 t)$.
4. Returns the peak absolute discrepancy: $\max |s_1 - s_2|$.

---

## Test Cases & Expected Results

With `DURATION = 0.1` seconds and `TOLERANCE = 1e-9`:

| $f$ (Hz) | $f_s$ (Hz) | Partner Frequency (Hz) | Formula ($f_s - f$) | Max \|diff\| | Verdict |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 300 | 1000 | 700 | $1000 - 300$ | $< 10^{-15}$ | `identical` |
| 100 | 1000 | 900 | $1000 - 100$ | $< 10^{-15}$ | `identical` |
| 440 | 8000 | 7560 | $8000 - 440$ | $< 10^{-15}$ | `identical` |
| 50 | 400 | 350 | $400 - 50$ | $< 10^{-15}$ | `identical` |
| 1200 | 3000 | 1800 | $3000 - 1200$ | $< 10^{-15}$ | `identical` |

---

## How to Run

```bash
# Run solution
python3 solution.py

# Or run alias.py
python3 alias.py
```
