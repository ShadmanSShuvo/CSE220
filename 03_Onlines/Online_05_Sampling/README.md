# Online 05: Sampling & Reconstruction (CSE220)

This directory contains the problem specifications, templates, and reference solutions for **Online 05 (Sampling & Reconstruction)** across Sections A, B, and C.

---

## Overview of Sections

| Section | Title | Key Topic | Core Concepts | Files |
| :--- | :--- | :--- | :--- | :--- |
| [**Sec_A**](./Sec_A/) | **Two Tones, One Sample Set** | Aliasing & Ambiguity | Frequency folding, partner frequencies, empirical sample matching | `solution.py`, `alias.py`, `alias_template.py` |
| [**Sec_B**](./Sec_B/) | **The Staircase Droops** | Zero-Order Hold (ZOH) & Sinc Droop | DAC staircase reconstruction, sinc droop attenuation, DFT tone measurement | `solution.py`, `zoh.py`, `zoh_template.py` |
| [**Sec_C**](./Sec_C/) | **Two Is Not Enough** | Linear Interpolation & Oversampling | First-order hold error, oversampling factor $k$, Taylor remainder error bound | `solution.py`, `headroom.py`, `headroom_template.py` |

---

## Core Theoretical Concepts

### 1. The Nyquist-Shannon Sampling Theorem & Aliasing (Sec A)
When a continuous sinusoid $x(t) = \cos(2\pi f t)$ is sampled at rate $f_s$:
- Samples are indistinguishable from frequencies at:
  $$f_{\text{alias}} = | \pm f + k f_s |, \quad k \in \mathbb{Z}$$
- For a baseband tone with $0 < f < \frac{f_s}{2}$, the lowest alias frequency that yields identical discrete sample values is:
  $$f_{\text{partner}} = f_s - f$$

### 2. Zero-Order Hold (ZOH) Sinc Droop (Sec B)
Real DACs hold each sample steady for duration $T_s = 1/f_s$. The impulse response is a rectangular pulse of width $T_s$, giving frequency response:
$$H_{\text{zoh}}(f) = T_s \, e^{-j \pi f / f_s} \, \text{sinc}\left(\frac{f}{f_s}\right)$$
This causes high-frequency attenuation ("sinc droop") with normalized gain:
$$\text{gain}(f) = \left| \text{sinc}\left(\frac{f}{f_s}\right) \right| = \left| \frac{\sin(\pi f / f_s)}{\pi f / f_s} \right|$$

### 3. Linear Reconstruction & Oversampling Headroom (Sec C)
Joining discrete samples with straight lines (first-order hold) avoids sinc pulse infinite support, but introduces chord approximation errors:
- Error bound from Taylor remainder:
  $$\text{error} \le \frac{T_s^2}{8} \max |x''(t)| = \frac{\pi^2}{8 k^2}$$
- Minimum integer oversampling factor $k$ ($f_s = 2 k f$) required to keep error $\le \epsilon$:
  $$k \ge \frac{\pi}{\sqrt{8 \epsilon}}$$
  The required oversampling multiplier depends only on desired accuracy, independent of signal frequency $f$.

---

## Quick Execution Guide

Run any section's solution from within its folder or from the repository root:

```bash
# Section A
python3 Sec_A/solution.py

# Section B
python3 Sec_B/solution.py

# Section C
python3 Sec_C/solution.py
```
