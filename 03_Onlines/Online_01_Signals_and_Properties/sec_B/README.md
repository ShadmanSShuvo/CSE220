# Section B: Generalized Continuous Transformation with Interpolation

> **Topic:** Continuous Signal Transformation $y(t) = x(\alpha t + \beta)$ and Off-Grid Interpolation
> **Source Specification:** [`spec_set1.pdf`](./spec_set1.pdf)

---

## Overview

When a continuous-time signal $x(t)$ is represented digitally on a discrete time grid with sample spacing $dt$, evaluating the affine transformation:
$$y(t) = x(\alpha t + \beta)$$
often requires values of $x$ at non-grid query times $\tau = \alpha t + \beta$.

This evaluation implements:
1. Base sinusoidal signal $x(t) = \sin(t)$ for $t \in [-\pi, \pi]$ (zero elsewhere).
2. A custom interpolation routine `interpolate_signal(t, x, query_t)` that:
   - Returns $0$ outside $[-\pi, \pi]$.
   - Locates exact matches within floating-point tolerance `np.isclose`.
   - Performs piecewise linear interpolation (averaging neighboring bounds) when $\tau$ falls strictly between sampled points.
3. Interactive user testing of scaling factor $\alpha$ and time shift $\beta$.

---

## Key Functions

- `generate_time_axis(t_min, t_max, dt)`: Constructs uniform time grid with step $dt = 0.05$.
- `base_signal(t)`: Computes $x(t) = \sin(t)$ for $t \in [-\pi, \pi]$.
- `interpolate_signal(t, x, query_t)`: Binary search (`np.searchsorted`) and linear interpolation.
- `transform_signal(t, x, alpha, beta)`: Computes $y(t_i) = x(\alpha t_i + \beta)$ for all $t_i$.

---

## How to Run

```bash
python3 set1soln.py
```
