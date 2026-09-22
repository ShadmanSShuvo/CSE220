# Section A: Fourier Epicycles & Energy-Preserving Harmonic Pruning

> **Topic:** Complex Exponential Fourier Series, Contour Drawing via Epicycles, and Parseval Energy Pruning
> **Source Specification:** [`Online-A1_A2.pdf`](./Online-A1_A2.pdf)

---

## Overview

Any closed 2D curve $(x(t), y(t))$ parameterized by time $t \in [0, T]$ can be treated as a periodic complex signal:
$$f(t) = x(t) + j \cdot y(t)$$
and expanded into a complex exponential Fourier series:
$$f(t) \approx \sum_{n=-N}^N c_n \, e^{j n \omega_0 t}, \quad \omega_0 = \frac{2\pi}{T}$$
where the Fourier coefficients are computed via numerical integration:
$$c_n = \frac{1}{T} \int_0^T f(t) \, e^{-j n \omega_0 t} \, dt$$

### Parseval's Theorem & Harmonic Pruning
Total signal energy in the frequency domain is given by Parseval's theorem:
$$E_{\text{total}} = \sum_{n=-N}^N |c_n|^2$$
To compress the representation while maintaining visual fidelity, harmonics are sorted by energy $|c_n|^2$ and pruned until cumulative energy reaches specific thresholds:
- $96\%$, $98\%$, $99\%$, and $100\%$

---

## Output Visualizations

The pruned reconstructions are saved as:
- `heart_pruned_0.96.png`: High compression, essential shape preserved.
- `heart_pruned_0.98.png`: Intermediate fidelity.
- `heart_pruned_0.99.png`: Near-identical contour.
- `heart_pruned_1.00.png`: Full harmonic reconstruction.

---

## How to Run

```bash
python3 solution.py
```
