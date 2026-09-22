# Section B: Fourier Magnitude-Phase Swapping

> **Topic:** 2D Spectral Decomposition, Magnitude vs. Phase Role in Visual Structure
> **Source Specification:** [`Jan2026_CSE220_Online_DFT_FFT_B1_B2.pdf`](./Jan2026_CSE220_Online_DFT_FFT_B1_B2.pdf)

---

## Overview

In the 2D Discrete Fourier Transform of an image, every complex coefficient can be expressed in polar form:
$$F(u, v) = |F(u, v)| \, e^{j \angle F(u, v)}$$
- **Magnitude $|F(u, v)|$**: Quantifies the energy present at spatial frequency $(u, v)$ (brightness, contrast, and directional dominance).
- **Phase $\angle F(u, v)$**: Encodes the spatial alignment and relative positioning of waveforms that form edges and recognizable geometric boundaries.

This assignment implements cross-synthesis between two images $A$ and $B$:
1. Image $AB$: Combined spectrum using the magnitude of $A$ and phase of $B$:
   $$S_{AB}(u, v) = |F_A(u, v)| \cdot e^{j \angle F_B(u, v)}$$
2. Image $BA$: Combined spectrum using the magnitude of $B$ and phase of $A$:
   $$S_{BA}(u, v) = |F_B(u, v)| \cdot e^{j \angle F_A(u, v)}$$

Reconstructing via 2D Inverse FFT visually proves Oppenheim's classic observation: **the reconstructed image visually resembles the image that donated the phase**, while the magnitude only contributes lighting and texture energy.

---

## Output Visualizations

Outputs stored in `outputs/lab_phase_swap_student/`:
- `mag_a_phase_b.png`: Dominant visual appearance of image B.
- `mag_b_phase_a.png`: Dominant visual appearance of image A.
- `comparison.png`: 4-quadrant comparison showing original images and swapped counterparts.

---

## How to Run

```bash
python3 solution.py
```
