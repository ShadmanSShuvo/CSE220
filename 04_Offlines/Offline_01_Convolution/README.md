# Offline 01: Discrete Linear Time-Invariant Systems & Convolution

> **Source Specification:** [`spec-offline-convolution.pdf`](./v2_final/spec-offline-convolution.pdf)

---

## Overview

This assignment builds an object-oriented Python engine for discrete-time signal representation and Linear Time-Invariant (LTI) system simulation from first principles.

### Key Objectives
1. **Discrete Signal Abstraction (`signal_lti.py`)**:
   - Explicit finite-support indexing $[t_{\min}, t_{\max}]$.
   - Safe zero-padding for non-supported time queries.
   - Core signal operations: shift $x[n - k]$, scale $\alpha x[n]$, add $x_1[n] + x_2[n]$, multiply $x_1[n] \cdot x_2[n]$.
2. **LTI System Convolution**:
   - 1D Discrete Convolution:
     $$y[n] = \sum_{k} x[k] \, h[n - k]$$
   - 2D Discrete Convolution on 2D grids and image kernels:
     $$Y[r, c] = \sum_{i} \sum_{j} X[i, j] \, H[r - i, c - j]$$
3. **Verification**:
   - Testing commutativity $x * h = h * x$, distributivity $x * (h_1 + h_2) = x * h_1 + x * h_2$, and associativity $x * (h_1 * h_2) = (x * h_1) * h_2$.

---

## Workspace Organization

- [`v2_final/`](./v2_final/): Complete verified submission including `signal_lti.py`, `main.py`, sample inputs, and reference outputs.
- [`v1_initial/`](./v1_initial/): Initial prototype workspace.
- [`archives/`](./archives/): Submission archives (`.zip`).

---

## How to Run

```bash
cd v2_final
python3 main.py
```
