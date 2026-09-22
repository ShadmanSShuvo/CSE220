# Section B: 2D Continuous Fourier Transform & Spatial Filtering

> **Topic:** Separable 2D Continuous Fourier Transform (CFT), Spatial Filtering, and Filter Complementarity
> **Source Specification:** [`Spec.pdf`](./Spec.pdf)

---

## Overview

This assignment extends Fourier analysis into 2D continuous space to filter continuous image signals $I(x, y)$ defined over $[-1, 1] \times [-1, 1]$:
1. **2D Continuous Fourier Transform**:
   $$F(u, v) = \int_{-1}^1 \int_{-1}^1 I(x, y) \, e^{-j 2\pi (ux + vy)} \, dx \, dy$$
   Evaluated using separable numerical integration (`np.trapezoid` over $x$, then over $y$).
2. **2D Frequency-Domain Filtering**:
   - **Bandpass Filter**: Keeps spatial frequencies in the annular ring $[R_1, R_2]$. Emphasizes edges and texture.
   - **Bandstop (Notch) Filter**: Attenuates frequencies in $[R_1, R_2]$ and retains low and very high components.
3. **Filter Complementarity**:
   Validates that:
   $$H_{\text{bp}}(u, v) + H_{\text{bs}}(u, v) = 1 \implies I_{\text{bp}}(x, y) + I_{\text{bs}}(x, y) = I(x, y)$$
4. **DC Shift**:
   Modifying the zero-frequency coefficient $F(0, 0)$ independently adjusts average image brightness without altering spatial edges or details.

---

## Output Images

- `pikachu.png`: Input image.
- `pikachu_bandpass.png`: Extracted mid-frequency edge features.
- `pikachu_bandstop.png`: Complementary background and fine features.
- `pikachu_brightened.png`: Image with DC coefficient shifted.

---

## How to Run

```bash
python3 solution.py
```
