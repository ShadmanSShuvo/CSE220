# Offline 02: Fourier Series & Continuous Fourier Transform

> **Source Specification:** [`Jan26_CSE220_Offline_FS_CFT.pdf`](./Jan26_CSE220_Offline_FS_CFT.pdf)

---

## Overview

This assignment applies continuous and complex exponential Fourier theory to vector graphics animations and 2D spatial frequency image processing across two distinct tasks.

---

## Task 1: Complex Exponential Fourier Series Epicycles (`task1_fourier_epicycles/`)

Expands a closed 2D path loaded from an SVG contour into a complex Fourier Series:
$$f(t) = x(t) + j \cdot y(t) = \sum_{n=-N}^{N} c_n \, e^{j n \omega_0 t}, \quad \omega_0 = \frac{2\pi}{T}$$
- **Harmonic Integration**: Computes complex coefficients $c_n$ via trapezoidal integration.
- **Reconstruction & Animation**: Reconstructs rotating epicycle vectors (circles with radii $|c_n|$ rotating at angular speeds $n \omega_0$).
- **Demonstrations**: Produces animated GIFs and static comparison PNGs for `circle`, `heart`, `infinity`, `s`, `ss`, and `star`.

### Running Task 1:
```bash
cd task1_fourier_epicycles
python3 fs_redrawer.py svgs/heart.svg 150 heart_comparison.png heart_epicycles.gif
```

---

## Task 2: 2D Continuous Fourier Transform Edge Detector (`task2_cft_edge_detector/`)

Implements a continuous 2D Fourier Transform edge detector using separable numerical integration:
1. Computes the 2D continuous transform $F(u, v)$ over spatial domain $[-1, 1] \times [-1, 1]$.
2. Applies a high-pass frequency filter $H(u, v)$ to attenuate low-frequency illumination and accentuate sharp intensity gradients (edges).
3. Evaluates filter cutoff parameters ($k = 1, 10, 100$) producing edge maps `pk1.png`, `pk10.png`, and `pk100.png`.

### Running Task 2:
```bash
cd task2_cft_edge_detector
python3 cft_edge_detector.py
```

---

## Directory Organization

- [`task1_fourier_epicycles/`](./task1_fourier_epicycles/): Epicycle drawing code, SVG samples, and generated GIFs.
- [`task2_cft_edge_detector/`](./task2_cft_edge_detector/): Continuous 2D CFT edge detection engine and output images.
- [`submission/`](./submission/): Final assignment submission files for student roll `2305025`.
- [`archives/`](./archives/): Original assignment distribution package and early drafts.
