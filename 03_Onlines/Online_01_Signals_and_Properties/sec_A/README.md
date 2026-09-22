# Section A: Time Reversal & Amplitude Scaling

> **Topic:** Continuous-Time Signal Definition, Time Inversion, and Interactive Amplitude Scaling
> **Source Specification:** [`spec_set2.pdf`](./spec_set2.pdf)

---

## Overview

This assignment focuses on basic operations on continuous-time signals:
1. Constructing a continuous base signal defined over a bounded interval $t \in [-\pi, \pi]$:
   $$x(t) = \begin{cases} e^{-t} \cos(t), & -\pi \le t \le \pi \\ 0, & \text{otherwise} \end{cases}$$
2. Applying time reversal:
   $$x(-t)$$
   Because the time axis is uniformly sampled from $-\pi$ to $\pi$, time reversal corresponds to reversing the sampled array (`x[::-1]`).
3. Applying user-controlled amplitude scaling:
   $$y(t) = \alpha \cdot x(-t)$$
4. Interactively accepting scalar values of $\alpha$ from standard input and plotting $x(t)$ alongside $y(t)$.

---

## Key Functions

- `base_signal(t)`: Computes $x(t) = e^{-t} \cos(t)$ with zero-padding outside $[-\pi, \pi]$.
- `transform_signal(t, x, alpha)`: Reverses the sequence in time and scales by $\alpha$.
- `main()`: Prompts for input $\alpha$ in a loop until the user types `'q'`, displaying comparison plots with Matplotlib.

---

## How to Run

```bash
python3 set2soln.py
```
