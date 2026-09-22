# Section C: Interconnected LTI Systems Block Diagram

> **Topic:** Parallel and Cascade LTI Interconnections & Equivalence Verification
> **Source Specification:** [`CONVOLUTION_set1.pdf`](./CONVOLUTION_set1.pdf)

---

## Overview

A complex network of interconnected LTI blocks can be analyzed in two mathematically equivalent ways:
1. **Block-by-Block Execution**: Convolving through each individual block and combining signals at summing junctions according to the signal flow graph.
2. **Overall Impulse Response $h[n]$**: Using LTI algebraic properties (distributivity and associativity of convolution):
   - Parallel branches add: $h_{\text{parallel}} = h_1 + h_2$
   - Cascade branches convolve: $h_{\text{cascade}} = h_a * h_b$
   - Overall response:
     $$h[n] = (h_1[n] + h_2[n]) * h_3[n] - h_4[n] * h_5[n]$$

This evaluation implements both methods on discrete input $x[n]$ and proves that the maximum absolute difference between both approaches is strictly zero.

---

## Given Impulse Responses

- $x[n]$: Defined from $n=-2$ to $4$ with values $[0, 0, 1, 0, -1, 0, 0]$
- $h_1 = [1.0]$ at $n=0$
- $h_2 = [0.5]$ at $n=1$
- $h_3 = [1.0, 1.0]$ for $n=0, 1$
- $h_4 = [0.7, -0.2]$ for $n=0, 1$
- $h_5 = [0.5, 0.2, -0.1]$ for $n=0, 1, 2$

---

## How to Run

```bash
python3 solution.py
```
Outputs `input_x.png`, `y_block.png`, and `y_combined.png`.
