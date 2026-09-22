# Online 04: Discrete Fourier Transform & FFT Applications (CSE220)

This directory contains the problem specifications, templates, and solutions for **Online 04 (DFT and FFT Applications in Image Processing)**.

---

## Overview of Sections

| Section | Topic | Core Concepts | Files |
| :--- | :--- | :--- | :--- |
| [**sec_A**](./sec_A/) | **Hybrid Images (Dual-Perception Filtering)** | Combining low frequencies of image A with high frequencies of image B; 2D FFT convolution with zero-padding and centered delta spectrum | `solution.py`, `image_conv.py`, `transforms.py`, `Jan2026_CSE220_Online_DFT_FFT_A1_A2.pdf` |
| [**sec_B**](./sec_B/) | **Fourier Magnitude-Phase Swapping** | Separating magnitude (spectral energy distribution) from phase (geometric/spatial structural information); reconstruct with $|A|e^{j\angle B}$ | `solution.py`, `image_conv.py`, `transforms.py`, `Jan2026_CSE220_Online_DFT_FFT_B1_B2.pdf` |
| [**sec_C**](./sec_C/) | **Frequency-Domain Image Steganography** | Hiding a secret watermark/image in the high-frequency DFT bins of a cover image using circular frequency masks | `solution.py`, `transforms.py`, `image_conv.py`, `CSE220_Online.pdf` |

---

## Shared FFT Engines (`transforms.py`)

All sections support interchangeable Fourier transformation backends:
1. `DFTAnalyzer`: Direct $O(N^2)$ matrix Discrete Fourier Transform.
2. `FFTTransformer`: Optimized Radix-2 Cooley-Tukey FFT (powers of 2).
3. `ArbitraryLengthFFT`: Chirp-Z / Bluestein FFT algorithm for non-power-of-2 dimensions.

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
