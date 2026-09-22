# Section B: Cascade of Accumulator & Difference as Identity System

> **Topic:** Inverse Systems, Accumulator, First Difference, and Identity Verification
> **Source Specification:** [`spec.pdf`](./spec.pdf)

---

## Overview

The running sum (accumulator) and first-difference operations are inverse operations of each other:
1. **Accumulator**:
   $$y_{\text{acc}}[n] = \sum_{k=-\infty}^n x[k] \implies h_{\text{acc}}[n] = u[n]$$
2. **First Difference**:
   $$y_{\text{diff}}[n] = w[n] - w[n - 1] \implies h_{\text{diff}}[n] = \delta[n] - \delta[n - 1]$$

When placed in cascade, their convolution yields an impulse:
$$h_{\text{cascade}}[n] = h_{\text{acc}}[n] * h_{\text{diff}}[n] = u[n] - u[n-1] = \delta[n]$$
Thus, the cascaded system is an **Identity System**: for any input $x[n]$, the final output equals $x[n]$ exactly.

---

## Key Functions

- `cascade(first_system, second_system, input_signal)`: Runs signal through both systems sequentially.
- `plot_cascade_responses(...)`: Generates stem plots of input, intermediate accumulated signal, and recovered output signal (`cascade_plot.png`).
- Verification: Validates that $|y_{\text{diff}}[n] - x[n]| = 0$ across the evaluation window.

---

## How to Run

```bash
python3 solution.py
```
