# Online 01: Signals & Properties (CSE220)

This directory contains the problem specifications, templates, and solutions for **Online 01 (Signals & Properties)**.

---

## Overview of Sections

| Section | Topic | Core Concepts | Key Functions / Files |
| :--- | :--- | :--- | :--- |
| [**sec_A**](./sec_A/) | **Time Reversal & Amplitude Scaling** | Base continuous-time signal $x(t) = e^{-t}\cos(t)$, time reversal $x(-t)$, amplitude scaling $\alpha x(-t)$ | `base_signal()`, `transform_signal()`, `set2soln.py` |
| [**sec_B**](./sec_B/) | **Generalized Affine Transformation** | Continuous transformation $y(t) = x(\alpha t + \beta)$ with manual linear interpolation for non-grid points | `base_signal()`, `interpolate_signal()`, `transform_signal()`, `set1soln.py` |
| [**sec_C**](./sec_C/) | **Even and Odd Signal Decomposition** | Decomposing discrete signals into symmetric and anti-symmetric components, verification, stem plots | `BuildEvenSignalFromRightSide()`, `CheckEven()`, `CheckOdd()`, `solution-c1-c2.py` |

---

## Quick Execution

```bash
# Section A
python3 sec_A/set2soln.py

# Section B
python3 sec_B/set1soln.py

# Section C
python3 sec_C/solution-c1-c2.py
```
