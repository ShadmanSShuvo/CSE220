# Practice Set 02: Discrete Convolution & LTI Systems

> **Source Documents:** [`PractiveProblemConv.pdf`](./PractiveProblemConv.pdf), [`CSE220 Convolution Practice Solutions.pdf`](./CSE220%20Convolution%20Practice%20Solutions.pdf)

---

## Overview

Discrete-time convolution is the defining operation for Linear Time-Invariant (LTI) systems:
$$y[n] = (x * h)[n] = \sum_{k=-\infty}^{\infty} x[k] \, h[n - k]$$

When two finite-duration discrete signals $x[n]$ (defined for $n \in [n_{x,\min}, n_{x,\max}]$) and $h[n]$ (defined for $n \in [n_{h,\min}, n_{h,\max}]$) are convolved:
1. **Length of output sequence**: $L_y = L_x + L_h - 1$
2. **Time range of output sequence**:
   $$n_{y,\min} = n_{x,\min} + n_{h,\min}$$
   $$n_{y,\max} = n_{x,\max} + n_{h,\max}$$

---

## Files in this Directory

| File | Description |
| :--- | :--- |
| [`fixed_soln.py`](./fixed_soln.py) | Clean OOP implementation defining `DiscreteSignal` and `LTISystem`. Accurately handles index boundaries, shifts, and stem plotting. |
| [`2305025-practice.py`](./2305025-practice.py) | Lab practice script with user student roll number `2305025`. |
| [`CSE220 Convolution Practice Solutions.pdf`](./CSE220%20Convolution%20Practice%20Solutions.pdf) | Step-by-step hand-derived solutions and verification tables. |
| [`PractiveProblemConv.pdf`](./PractiveProblemConv.pdf) | Original problem specifications and practice prompts. |

---

## How to Run

```bash
python3 fixed_soln.py
```
