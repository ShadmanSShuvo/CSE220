# CSE220: Signals & Systems — Online Lab Evaluations

This directory contains the problem specifications, templates, starter code, and reference solutions for the **CSE220 Signals & Systems Online Lab Evaluations**.

---

## Roadmap of Online Evaluations

| Online Lab | Topic | Sections | Core Competencies |
| :--- | :--- | :--- | :--- |
| [**Online 01: Signals & Properties**](./Online_01_Signals_and_Properties/) | Basic Continuous & Discrete Signal Operations | `sec_A`, `sec_B`, `sec_C` | Time scaling, time reversal, linear interpolation, even/odd decomposition |
| [**Online 02: Convolution & LTI Systems**](./Online_02_Convolution/) | LTI System Properties & Discrete Convolution | `sec_A`, `sec_B`, `sec_C` | Linearity, time invariance, cascade inversion (accumulator + difference = identity), complex block diagrams |
| [**Online 03: Fourier Series & CFT**](./Online_03_FS_and_CFT/) | Fourier Series Epicycles & 2D CFT | `sec_A`, `sec_B` | Complex exponential epicycles on SVG paths, Parseval energy pruning, 2D continuous FT, spatial bandpass/bandstop filtering |
| [**Online 04: DFT & FFT Applications**](./Online_04_DFT_and_FFT/) | 2D DFT/FFT Image Processing | `sec_A`, `sec_B`, `sec_C` | Hybrid image generation (low-pass + high-pass blending), Fourier magnitude-phase swapping, frequency-domain steganography |
| [**Online 05: Sampling & Reconstruction**](./Online_05_Sampling/) | Sampling, Aliasing & Reconstruction | `Sec_A`, `Sec_B`, `Sec_C` | Alias partner frequency folding, zero-order hold (ZOH) sinc droop, linear reconstruction oversampling factor $k$ |

---

## Directory Navigation

Click into any folder to view its dedicated README with complete theoretical background, mathematical formulas, test cases, and instructions:

- [`Online_01_Signals_and_Properties/`](./Online_01_Signals_and_Properties/)
  - [`sec_A/`](./Online_01_Signals_and_Properties/sec_A/): Signal transformation $y(t) = \alpha x(-t)$ on $x(t) = e^{-t}\cos(t)$
  - [`sec_B/`](./Online_01_Signals_and_Properties/sec_B/): Generalized continuous transformation $y(t) = x(\alpha t + \beta)$ with linear interpolation
  - [`sec_C/`](./Online_01_Signals_and_Properties/sec_C/): Discrete even & odd decomposition, symmetry validation, and stem plots
- [`Online_02_Convolution/`](./Online_02_Convolution/)
  - [`sec_A/`](./Online_02_Convolution/sec_A/): Empirical testing of Linearity and Time-Invariance on LTI vs Time-Varying systems
  - [`sec_B/`](./Online_02_Convolution/sec_B/): Cascade of Accumulator and First-Difference as the Identity system ($h_1 * h_2 = \delta[n]$)
  - [`sec_C/`](./Online_02_Convolution/sec_C/): Interconnected LTI block diagram: block-by-block vs overall equivalent impulse response
- [`Online_03_FS_and_CFT/`](./Online_03_FS_and_CFT/)
  - [`sec_A/`](./Online_03_FS_and_CFT/sec_A/): Fourier Series epicycles on SVG paths, harmonic calculation, Parseval energy pruning
  - [`sec_B/`](./Online_03_FS_and_CFT/sec_B/): 2D Continuous Fourier Transform, Bandpass/Bandstop filtering, filter complementarity, DC shift
- [`Online_04_DFT_and_FFT/`](./Online_04_DFT_and_FFT/)
  - [`sec_A/`](./Online_04_DFT_and_FFT/sec_A/): Hybrid Images via 2D FFT Gaussian low-pass and high-pass filtering
  - [`sec_B/`](./Online_04_DFT_and_FFT/sec_B/): Fourier Magnitude-Phase Swapping between two images
  - [`sec_C/`](./Online_04_DFT_and_FFT/sec_C/): Frequency-Domain Image Steganography (embedding secret image in high-frequency DFT bins)
- [`Online_05_Sampling/`](./Online_05_Sampling/)
  - [`Sec_A/`](./Online_05_Sampling/Sec_A/): Aliasing ambiguity & smallest positive partner frequency $f_{\text{alias}} = f_s - f$
  - [`Sec_B/`](./Online_05_Sampling/Sec_B/): Zero-Order Hold (ZOH) sinc droop attenuation & DFT tone amplitude measurement
  - [`Sec_C/`](./Online_05_Sampling/Sec_C/): Piecewise linear interpolation reconstruction, error bounds, and minimal oversampling $k \ge \pi/\sqrt{8\epsilon}$

---

## General Testing Guide

All evaluations are self-contained Python scripts requiring standard scientific libraries (`numpy`, `matplotlib`, `scipy`, and optionally `pillow` or `imageio`).

```bash
# Example: Running any online solution
python3 Online_05_Sampling/Sec_C/solution.py
```
