# Section C: Even and Odd Signal Decomposition

> **Topic:** Discrete Signal Symmetry, Even/Odd Decomposition, and Stem Visualization
> **Source Specification:** [`online-c1-c2.pdf`](./online-c1-c2.pdf)

---

## Overview

Any discrete-time signal $x[n]$ defined over a symmetric domain $[-N, N]$ can be uniquely decomposed into the sum of an **even (symmetric)** component and an **odd (anti-symmetric)** component:
$$x[n] = x_e[n] + x_o[n]$$
where:
$$x_e[n] = \frac{x[n] + x[-n]}{2}, \quad x_o[n] = \frac{x[n] - x[-n]}{2}$$

Properties:
- **Even symmetry**: $x_e[n] = x_e[-n]$
- **Odd symmetry**: $x_o[n] = -x_o[-n]$ (with $x_o[0] = 0$)
- **Completeness**: $x_e[n] + x_o[n] = x[n]$ for all $n$

---

## Implementation Details

The solution in [`solution-c1-c2.py`](./solution-c1-c2.py):
1. Takes a right-side sequence ($n \ge 0$) and mirrors it to build a symmetric discrete signal.
2. Computes $x_e[n]$ and $x_o[n]$ across 5 test cases.
3. Automatically validates symmetry (`CheckEven`, `CheckOdd`) and sum preservation (`np.allclose(xe + xo, x)`).
4. Generates stem plots saved as `output_case_1.png` through `output_case_5.png`.

---

## How to Run

```bash
python3 solution-c1-c2.py
```
