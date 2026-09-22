# Section A: Linearity and Time-Invariance Verification

> **Topic:** Empirical Testing of Linearity and Time-Invariance on Discrete Systems
> **Source Specification:** [`A1_A2.pdf`](./A1_A2.pdf)

---

## Overview

This assignment provides general automated property checkers to empirically test whether a discrete-time system satisfies:
1. **Linearity**: The system satisfies superposition:
   $$T\{a \cdot x_1[n] + b \cdot x_2[n]\} = a \cdot T\{x_1[n]\} + b \cdot T\{x_2[n]\}$$
2. **Time-Invariance**: Shifting the input by $k$ shifts the output by exactly $k$:
   $$T\{x[n - k]\} = y[n - k], \quad \text{where } y[n] = T\{x[n]\}$$

Two systems are evaluated:
- **System A (LTI System)**: Defined by impulse response $h_A = [1.0, -0.5, 0.25]$. Satisfies both Linearity and Time-Invariance.
- **System B (Time-Varying System)**: Computes $y[n] = n \cdot x[n]$. Linear, but **Time-Varying** (time-invariance error $\gg 0$).

---

## Key Functions

- `test_linearity(apply_system, x1, x2, a, b)`: Evaluates maximum difference between $T\{a x_1 + b x_2\}$ and $a T\{x_1\} + b T\{x_2\}$.
- `test_time_invariance(apply_system, x, k)`: Evaluates maximum difference between $T\{x[n-k]\}$ and $y[n-k]$.

---

## How to Run

```bash
python3 solution.py
```
