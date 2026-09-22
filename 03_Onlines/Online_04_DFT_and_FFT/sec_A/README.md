# Section A: Hybrid Images (Dual-Scale Frequency Fusion)

> **Topic:** 2D Frequency Filtering, Gaussian Low-Pass, High-Pass, and Hybrid Image Synthesis
> **Source Specification:** [`Jan2026_CSE220_Online_DFT_FFT_A1_A2.pdf`](./Jan2026_CSE220_Online_DFT_FFT_A1_A2.pdf)

---

## Overview

Human visual perception interprets images at multiple spatial scales:
- **Up close**: High spatial frequencies dominate, revealing fine sharp details, edges, and textures.
- **From afar**: The human eye acts as a low-pass filter, observing primarily coarse shapes, luminance, and overall structure.

A **hybrid image** blends:
1. The **low-frequency component** of Image 1 (obtained by convolving with a 2D Gaussian filter kernel).
2. The **high-frequency component** of Image 2 (obtained by subtracting its low-pass filtered version from the original image, using a centered delta impulse):
   $$I_{\text{hybrid}} = (I_1 * G) + (I_2 * (\delta - G))$$

In the 2D frequency domain:
$$S_{\text{hybrid}}(u, v) = S_1(u, v) \cdot G(u, v) + S_2(u, v) \cdot (\Delta(u, v) - G(u, v))$$

---

## Output Visualizations

Outputs stored in `outputs/lab_hybrid_student/`:
- `low_component.png`: Low-pass filtered image.
- `high_component.png`: High-pass edge details.
- `hybrid.png`: Blended hybrid image exhibiting dual perception.
- `comparison.png`: Side-by-side comparative panel.

---

## How to Run

```bash
python3 solution.py
```
