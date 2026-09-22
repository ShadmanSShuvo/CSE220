# Online 02: Convolution & LTI Systems (CSE220)

This directory contains the problem specifications, templates, and solutions for **Online 02 (Convolution & LTI Systems)**.

---

## Overview of Sections

| Section | Topic | Core Concepts | Files |
| :--- | :--- | :--- | :--- |
| [**sec_A**](./sec_A/) | **Linearity & Time-Invariance Verification** | Empirical property testers on System A (LTI) and System B (Time-varying $n \cdot x[n]$) | `solution.py`, `signal_lti.py`, `A1_A2.pdf` |
| [**sec_B**](./sec_B/) | **Cascade of Accumulator & Difference (Identity)** | Inverting an accumulator with first-difference: $h_{\text{acc}} * h_{\text{diff}} = \delta[n]$ | `solution.py`, `signal_lti.py`, `spec.pdf` |
| [**sec_C**](./sec_C/) | **Interconnected LTI Block Diagram** | Parallel and cascade combination: block-by-block vs single overall impulse response $h[n]$ | `solution.py`, `signal_lti.py`, `CONVOLUTION_set1.pdf` |

---

## Shared Architecture (`signal_lti.py`)

All sections build on a unified discrete signal representation:
- `DiscreteSignal(start_time, end_time)`: Explicit time-indexed discrete signals with support for zero-padding, addition, scaling, shifting, convolution, and plotting.
- `LTISystem(impulse_response)`: Encapsulates discrete linear time-invariant filtering via convolution $y[n] = x[n] * h[n]$.

---

## Quick Execution

```bash
# Section A
python3 sec_A/solution.py

# Section B
python3 sec_B/solution.py

# Section C
python3 sec_C/solution.py
```
