# Sampling & Digital Signal Processing (CSE220) Lab & Exam Toolkit

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20+-013243.svg?logo=numpy)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-11557c.svg)](https://matplotlib.org/)
[![Topic](https://img.shields.io/badge/Topic-Signals%20%26%20Systems%20%7C%20DSP-orange.svg)]()

A comprehensive repository for mastering **Signal Sampling, Aliasing, Sinc Reconstruction, and Discrete Fourier Analysis**. This repository is structured specifically for Signals & Systems / DSP lab exams, online evaluations, and practical implementations with NumPy and Matplotlib.

---

## Table of Contents
1. [Overview & Highlights](#overview--highlights)
2. [Repository Structure](#repository-structure)
3. [Theoretical Foundations & Formula Cheat-Sheet](#theoretical-foundations--formula-cheat-sheet)
4. [Master Template (`template.py`)](#master-template-templatepy)
5. [Problem Sets & Practice Modules](#problem-sets--practice-modules)
   - [1. Mahdi: 10 Timed Practice Exams (`/Mahdi`)](#1-mahdi-10-timed-practice-exams-mahdi)
   - [2. GPT: 15 Applied Exam & Simulation Problems (`/gpt`)](#2-gpt-15-applied-exam--simulation-problems-gpt)
   - [3. Sami: Exam Workbook & 18 Worked Solutions (`/Sami`)](#3-sami-exam-workbook--18-worked-solutions-sami)
   - [4. Fast Fourier Transform Modules (`/fft`)](#4-fast-fourier-transform-modules-fft)
6. [Installation & Setup](#installation--setup)
7. [How to Run](#how-to-run)
8. [Exam Quick-Reference Checklist](#exam-quick-reference-checklist)

---

## Overview & Highlights

This toolkit covers the full spectrum of continuous-to-discrete-to-continuous conversion:
- **Sampling & Discretization**: Uniform sampling grids, time step calculation ($T_s = 1/f_s$), and signal discretization.
- **Nyquist-Shannon Theorem**: Critical rates ($f_s = 2 f_{\max}$), oversampling vs. undersampling, and aliasing boundaries.
- **Aliasing & Frequency Folding**: Mathematical calculation of folded frequencies ($|f_0 - k f_s|$), phantom tones, and beat frequencies.
- **Spectral Replicas**: Periodic spectral copies in the continuous frequency domain $\sum X(f - k f_s)$.
- **Reconstruction Methods**:
  - **Zero-Order Hold (ZOH)**: Staircase piecewise-constant interpolation.
  - **Linear Interpolation**: Endpoint-safe piecewise-linear interpolation.
  - **Whittaker-Shannon Sinc Interpolation**: Normalized sinc kernel convolution for bandlimited recovery.
- **Multirate DSP**: Zero-insertion upsampling, anti-aliasing low-pass filtering, and decimation (downsampling).
- **Fourier Domain Analysis**: Scratch Discrete Fourier Transform (DFT), Inverse DFT (IDFT), physical frequency bin mapping, and symmetric two-sided spectrum representations (`fftshift`).
- **Fast Fourier Transform (FFT)**: NumPy FFT algorithms (`fft`, `rfft`, `ifft`, `fftshift`, `fftfreq`), amplitude correction, and peak frequency detection.
- **Real-World Simulations**: Audio fidelity tradeoffs (8 kHz telephony vs. 44.1 kHz CD audio), ECG sampling, and ADC quantization noise / SQNR.

---

## Repository Structure

```text
Sampling/
├── README.md                      # Complete project documentation & guide
├── template.py                    # Master DSP reference library (clean 24 modular sections)
├── test_template.py               # Complete test runner & 7-figure visual demonstration suite
│
├── fft/                           # 11 Fast Fourier Transform (FFT) Demonstration Modules
│   ├── 01_minimal_fft.py          # Minimal 4-point discrete sequence FFT & IFFT toy example
│   ├── 02_inverse_fft.py          # Inverse FFT (np.fft.ifft) signal recovery
│   ├── 03_single_tone_fft.py      # Single-frequency spectrum & positive-frequency masking
│   ├── 04_two_tone_fft.py         # Dual-frequency signal with time-domain & stem FFT spectrum
│   ├── 05_multi_tone_fft.py       # Multi-tone signal with one-sided amplitude calibration (*2)
│   ├── 06_real_fft.py             # Optimized real FFT (np.fft.rfft & rfftfreq)
│   ├── 07_centered_fftshift.py    # Zero-frequency centered two-sided spectrum (fftshift)
│   ├── 08_dominant_frequency.py   # Dominant peak frequency detection via np.argmax
│   ├── 09_noisy_signal_fft.py     # Extracting sinusoids from Gaussian white noise
│   ├── 10_amplitude_corrected_fft.py # Step-by-step annotated one-sided FFT guide
│   └── 11_compute_fft_utility.py  # Reusable compute_fft(signal, fs) helper function
│
├── Mahdi/                         # 10 Timed 30-Minute Lab Practice Exams
│   ├── README.md                  # Scope & exam guidelines
│   ├── 01_Easy_Uniform_Sampling/  # statement.pdf, template.py, solution.py
│   ├── 02_Easy_Nyquist_Check/
│   ├── 03_Easy_Same_Samples/
│   ├── 04_Easy_Sinc_Kernel/
│   ├── 05_Medium_Spectral_Copies/
│   ├── 06_Medium_Alias_Frequencies/
│   ├── 07_Medium_Ideal_Filter/
│   ├── 08_Medium_Sinc_Reconstruction/
│   ├── 09_Hard_Alias_Collisions/
│   └── 10_Hard_Reconstruction_Experiment/
│
├── gpt/                           # 15 Interactive Problem Scripts + Descriptions
│   ├── problems.md                # Mathematical descriptions and tasks for 15 problems
│   ├── problem1.py                # Basic sampling & Nyquist criterion
│   ├── problem2.py                # Nyquist rate detection on multi-tone signal
│   ├── problem3.py                # Visualizing aliased waveforms
│   ├── problem4.py                # Aliasing frequency calculator & folding table
│   ├── problem5.py                # Composite signal sampling & component tracking
│   ├── problem6.py                # Frequency-domain spectral replica viewer
│   ├── problem7.py                # Sinc interpolation recovery & error metrics
│   ├── problem8.py                # Reconstruction failure under undersampling
│   ├── problem9.py                # ECG-like signal sampling & harmonics
│   ├── problem10.py               # Audio sampling trade-offs (8k vs 44.1k)
│   ├── problem11.py               # Identifying unknown sampling rates from DFT peaks
│   ├── problem12.py               # Minimum sampling rate design under constraints
│   ├── problem13.py               # Sampling theorem multi-panel interactive visualizer
│   ├── problem14.py               # Reverse engineering aliased frequencies
│   └── problem15.py               # ADC sampling and quantization (SQNR)
│
└── Sami/                          # Practice Workbook & 18 Worked Solutions
    ├── QUESTIONS.pdf              # 15-page exam workbook (Theory + Prompts + Revision)
    ├── templatex.py               # Reusable interpolation functions (sinc, zoh, linear)
    ├── practice(me)/              # Personal practice scratch scripts
    └── AllSoln/                   # 18 Modular Python Solution Scripts
        ├── 01_sampling_grid_and_nyquist_report.py
        ├── 02_alias_table.py
        ├── 03_same_samples_different_continuous_tones.py
        ├── 04_fft_peak_to_physical_frequency.py
        ├── 05_signed_dft_bin_map.py
        ├── 06_spectral_copy_intervals.py
        ├── 07_downsampling_and_predicted_aliases.py
        ├── 08_anti_alias_filter_before_decimation.py
        ├── 09_zero_order_hold_reconstruction.py
        ├── 10_endpoint_safe_linear_reconstruction.py
        ├── 11_manual_linear_interpolation.py
        ├── 12_vectorized_sinc_reconstruction.py
        ├── 13_compare_zoh_linear_and_sinc.py
        ├── 14_zero_insertion_upsampling.py
        ├── 15_interpolation_filter_after_upsampling.py
        ├── 16_rational_resampling_by_linear_interpolation.py
        ├── 17_periodic_signal_and_dft_coefficients.py
        └── 18_repair_a_sampling_pipeline.py
```

---

## Theoretical Foundations & Formula Cheat-Sheet

### 1. The Sampling Process
Given continuous signal $x(t)$, sampling with period $T_s = 1 / f_s$ yields discrete samples:
$$x[n] = x(n T_s) = x\left(\frac{n}{f_s}\right)$$

### 2. Nyquist-Shannon Sampling Theorem
To completely reconstruct a bandlimited signal whose highest frequency is $f_{\max}$:
$$f_s > 2 f_{\max} \quad \text{or} \quad \omega_s > 2 \omega_{\max}$$
- **Nyquist Rate**: $f_{N} = 2 f_{\max}$ (minimum theoretical rate; strict inequality $f_s > 2 f_{\max}$ required for non-trivial phase/amplitude recovery).
- **Nyquist Frequency (Folding Frequency)**: $f_{\text{fold}} = \frac{f_s}{2}$.

### 3. Aliasing and Frequency Folding
When $f_0 > f_s / 2$, the continuous tone aliases into the primary baseband $[0, f_s/2]$:
$$f_{\text{apparent}} = \left| f_0 - k \cdot f_s \right|, \quad k = \operatorname{round}\left(\frac{f_0}{f_s}\right)$$

### 4. Sampled Spectrum & Spectral Copies
Sampling in the time domain corresponds to periodic replication in the frequency domain scaled by $f_s$:
$$X_s(f) = f_s \sum_{k=-\infty}^{\infty} X(f - k f_s)$$
If $f_s < 2 f_{\max}$, copies overlap (aliasing / spectral distortion).

### 5. Ideal Sinc Reconstruction (Whittaker-Shannon)
An ideal low-pass brickwall filter with cutoff $f_c = f_s/2$ produces the normalized sinc interpolation:
$$x_r(t) = \sum_{n=-\infty}^{\infty} x[n] \operatorname{sinc}\left(\frac{t - n T_s}{T_s}\right)$$
where normalized sinc is defined as:
$$\operatorname{sinc}(u) = \begin{cases} \frac{\sin(\pi u)}{\pi u}, & u \neq 0 \\ 1, & u = 0 \end{cases}$$
*(Note: `np.sinc(u)` in NumPy evaluates $\frac{\sin(\pi u)}{\pi u}$).*

### 6. Discrete Fourier Transform (DFT) & Bin Mapping
For an $N$-point DFT of $x[n]$ sampled at $f_s$:
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}, \quad k = 0, 1, \dots, N-1$$
- **Bin resolution**: $\Delta f = \frac{f_s}{N}$ Hz per bin.
- **Bin to frequency (one-sided)**: $f_k = k \cdot \frac{f_s}{N}$ for $k \in [0, N-1]$.
- **Signed / two-sided frequencies** (centered with `fftshift`):
  $$k_{\text{signed}} \in \left[ -\left\lfloor \frac{N}{2} \right\rfloor, \left\lfloor \frac{N-1}{2} \right\rfloor \right] \implies f_{\text{signed}} = k_{\text{signed}} \cdot \frac{f_s}{N}$$

---

## Master Template (`template.py`) & Test Suite (`test_template.py`)

The root `template.py` file is a clean, importable reference library containing 24 modular DSP sections without testing boilerplate. Its companion test driver [`test_template.py`](file:///Users/shuvo/Sampling/test_template.py) runs sequential verification on all functions and launches a comprehensive 7-figure visual demonstration suite:

| Section # | Component / Function | Purpose |
|:---:|:---|:---|
| **1** | `generate_signal(t, components)` | Multi-tone sinusoid generator ($\sum A_i \cos(2\pi f_i t + \phi_i)$) |
| **2** | `create_time_axis(start, end, count)` | High-density grid generator for analog signal emulation |
| **3** | `sample_signal(signal, fs, start, end)` | Uniform sample grid generator returning `n`, `t_samples`, `x_samples` |
| **4** | `nyquist_rate(f_max)` / `is_sampling_safe()` | Nyquist rate computation & strict inequality check |
| **5** | `apparent_frequency(f, fs)` | Precise aliased frequency folding computation |
| **6** | `normalized_sinc(u)` | Safe normalized sinc function $\sin(\pi u)/(\pi u)$ with zero-check |
| **7** | `sinc_interpolation_pulse(...)` | Scaled sinc kernel evaluation centered at sample points |
| **8** | `sinc_reconstruct(t_fine, n, x_samples, fs)` | Whittaker-Shannon summation reconstruction |
| **9** | `compute_rmse(x_true, x_rec)` | Root-Mean-Square Error calculation between signals |
| **10** | `analytical_spectrum_two_tones(...)` | Exact continuous-time Fourier Transform spectrum evaluation |
| **11** | `sample_train_spectrum(...)` | Periodic spectral copies evaluation over specified replica range |
| **12** | `valid_recovery_cutoff(f_max, fs)` | Cutoff range validation: $f_{\max} \le f_c \le f_s - f_{\max}$ |
| **13** | `ideal_lowpass_filter(f, cutoff, gain)` | Frequency response $H(f)$ of ideal brickwall filter |
| **14** | `apply_filter(X, H)` | Spectral multiplication $Y(f) = X(f) \cdot H(f)$ |
| **15** | `manual_spectral_recovery(...)` | End-to-end continuous spectral filtering demonstration |
| **16** | `dft(x)` | $O(N^2)$ Discrete Fourier Transform from fundamental definition |
| **17** | `idft(X)` | Inverse Discrete Fourier Transform from scratch |
| **18** | `dft_frequencies(N, fs, centered)` | DFT bin to physical frequency axis mapper |
| **19** | `manual_fftshift(x)` / `manual_fftshift_freq(...)`| Zero-frequency shift centering without external dependencies |
| **20** | `magnitude_spectrum(X)` / `phase_spectrum(X)` | Complex spectrum polar decomposition with noise thresholding |
| **21** | `hz_to_rad_s(f)` / `rad_s_to_hz(w)` | Frequency unit conversion helpers |
| **22** | `run_sampling_demo()` | End-to-end demo: analog signal vs. samples vs. sinc reconstruction |
| **23** | `run_spectrum_demo()` | End-to-end demo: original vs. sampled spectral replicas |
| **24** | `run_dft_demo()` | End-to-end demo: manual DFT and two-sided magnitude spectrum plot |

---

## Problem Sets & Practice Modules

### 1. Mahdi: 10 Timed Practice Exams (`/Mahdi`)
Each subfolder contains:
- `statement.pdf`: 1-page problem description, input/output contract, and numerical example.
- `template.py`: Starter code with `TODO` markers and a complete test driver.
- `solution.py`: Reference implementation.

| Directory | Difficulty | Topic / Description |
|:---|:---:|:---|
| `01_Easy_Uniform_Sampling` | Easy | Uniform sampling grid creation and discrete sinusoid generation |
| `02_Easy_Nyquist_Check` | Easy | Maximum frequency identification, Nyquist rate, and safety validation |
| `03_Easy_Same_Samples` | Easy | Demonstrating different continuous tones producing identical sample sequences |
| `04_Easy_Sinc_Kernel` | Easy | Implementation of the normalized interpolation pulse $T_s \operatorname{sinc}(f_s t)$ |
| `05_Medium_Spectral_Copies` | Medium | Constructing periodic spectral replicas in radians/second |
| `06_Medium_Alias_Frequencies` | Medium | Folding multi-component cosine signals across multiple Nyquist zones |
| `07_Medium_Ideal_Filter` | Medium | Designing and applying an ideal low-pass brickwall filter in frequency domain |
| `08_Medium_Sinc_Reconstruction` | Medium | Reconstructing signals from a finite sample set using Whittaker-Shannon formula |
| `09_Hard_Alias_Collisions` | Hard | Identifying aliasing collisions where distinct tones fold to the exact same frequency |
| `10_Hard_Reconstruction_Experiment` | Hard | Comparing reconstruction RMSE when varying sample count $N$ vs. rate $f_s$ |

---

### 2. GPT: 15 Applied Exam & Simulation Problems (`/gpt`)
Full mathematical problem formulations are in `gpt/problems.md`. Each `problemX.py` script provides an automated CLI solution and multi-panel Matplotlib plot:

| Script | Topic | Key Concepts Illustrated |
|:---|:---|:---|
| `problem1.py` | Basic Sampling of a Sinusoid | $f_0=5\text{ Hz}$ sampled at 50, 10, and 7 Hz; apparent alias visualization |
| `problem2.py` | Nyquist Rate Detection | Multi-tone signal $x(t) = \sin(2\pi 10t) + 0.5\sin(2\pi 25t)$ tested across 4 rates |
| `problem3.py` | Demonstrating Aliasing | $35\text{ Hz}$ sinusoid sampled at $50\text{ Hz}$, showing 15 Hz alias in time domain |
| `problem4.py` | Aliasing Frequency Calculator | Formula $f_{\text{apparent}} = \|f - k f_s\|$ tabulated for negative/positive harmonics |
| `problem5.py` | Sampling a Composite Signal | Analyzing 3-tone signal with some components preserved and others folded |
| `problem6.py` | Frequency-Domain View of Sampling | Continuous spectrum convolution with Dirac comb; spectral replica overlap |
| `problem7.py` | Sinc Reconstruction | Recovering continuous signal via matrix/vectorized sinc interpolation |
| `problem8.py` | Undersampling & Reconstruction Failure | Comparing reconstructed signal vs. ground truth when Nyquist is violated |
| `problem9.py` | ECG-Like Signal Sampling | Physiological signal modeling with harmonics; bandlimiting and distortion |
| `problem10.py` | Audio Sampling Trade-offs | Telephone standard ($8\text{ kHz}$), speech ($16\text{ kHz}$), and CD ($44.1\text{ kHz}$) |
| `problem11.py` | Unknown Sampling Frequency | Deducing true sampling frequency from DFT peak indices and known tone |
| `problem12.py` | Minimum Sampling Rate Design | Designing minimal anti-aliased rate given guard-band constraints |
| `problem13.py` | Sampling Theorem Visualizer | Comprehensive multi-panel diagnostic showing time and frequency simultaneously |
| `problem14.py` | Reverse Engineering Aliases | Finding candidate original frequencies that could have produced an observed alias |
| `problem15.py` | Sampling + Quantization (ADC) | Quantization levels ($B$ bits), quantization error, and Signal-to-Quantization-Noise (SQNR) |

---

### 3. Sami: Exam Workbook & 18 Worked Solutions (`/Sami`)
The file `Sami/QUESTIONS.pdf` is an exam workbook containing practical theory summaries, 18 coding questions, worked solutions, and an exam revision sheet. The companion directory `Sami/AllSoln/` contains production-ready Python solutions:

| Solution Script | Primary Objective |
|:---|:---|
| `01_sampling_grid_and_nyquist_report.py` | Discretization grid generator & boolean safety report dictionary |
| `02_alias_table.py` | Generates folding frequency lookup tables for arbitrary input tones |
| `03_same_samples_different_continuous_tones.py` | Identifies harmonic families $f_k = f_0 + k f_s$ sharing sample values |
| `04_fft_peak_to_physical_frequency.py` | Converts FFT bin index $k^*$ to physical continuous frequency in Hz |
| `05_signed_dft_bin_map.py` | Maps raw FFT output to signed two-sided bins $[-N/2, N/2 - 1]$ |
| `06_spectral_copy_intervals.py` | Computes bandwidth occupancy intervals $[k f_s - B, k f_s + B]$ |
| `07_downsampling_and_predicted_aliases.py` | Decimation by integer factor $M$ and predicted alias frequency shifts |
| `08_anti_alias_filter_before_decimation.py` | Applying FIR/IIR anti-aliasing low-pass filter prior to downsampling |
| `09_zero_order_hold_reconstruction.py` | Vectorized Zero-Order Hold (sample repetition) reconstruction |
| `10_endpoint_safe_linear_reconstruction.py` | Piecewise linear interpolation handling boundary conditions |
| `11_manual_linear_interpolation.py` | Manual linear interpolation without `np.interp` via index search & $\alpha$ blending |
| `12_vectorized_sinc_reconstruction.py` | Outer-product vectorized Whittaker-Shannon sinc reconstruction |
| `13_compare_zoh_linear_and_sinc.py` | Direct performance and RMSE comparison across ZOH, Linear, and Sinc |
| `14_zero_insertion_upsampling.py` | Expanding discrete sequences by factor $L$ via zero-stuffing |
| `15_interpolation_filter_after_upsampling.py` | Removing imaging spectral copies using an anti-imaging low-pass filter |
| `16_rational_resampling_by_linear_interpolation.py` | Resampling from arbitrary $f_{s1}$ to $f_{s2}$ via linear interpolation |
| `17_periodic_signal_and_dft_coefficients.py` | Computing Fourier series harmonics from exactly periodic sampled blocks |
| `18_repair_a_sampling_pipeline.py` | Diagnosing and fixing a corrupted sampling & reconstruction pipeline |

---

### 4. Fast Fourier Transform Modules (`/fft`)
The `/fft` directory provides 11 progressive scripts demonstrating NumPy's Fast Fourier Transform library (`np.fft`), transitioning from basic discrete array transformations to real-world audio/spectral analysis:

| Script | Title / Focus | Concepts Demonstrated |
|:---|:---|:---|
| `01_minimal_fft.py` | Minimal 4-Point DFT & IDFT | Toy array `[1, 2, 3, 4]`, `np.fft.fft`, `np.abs(X)` magnitude, and `np.fft.ifft` roundtrip |
| `02_inverse_fft.py` | Signal Reconstruction via IFFT | Validating lossless reconstruction back to original time samples |
| `03_single_tone_fft.py` | Single Sinusoid Spectrum | $50\text{ Hz}$ sine wave, frequency bin mapping via `fftfreq`, and positive-frequency masking |
| `04_two_tone_fft.py` | Dual-Frequency Spectrum | Dual-tone signal ($50\text{ Hz} + 120\text{ Hz}$) with time-domain and stem spectrum subplots |
| `05_multi_tone_fft.py` | Multi-Tone Amplitude Correction | Three sinusoids ($50, 120, 200\text{ Hz}$) with one-sided amplitude calibration (`magnitude[1:-1] *= 2`) |
| `06_real_fft.py` | Real FFT (`rfft` / `rfftfreq`) | Efficient computation specifically optimized for real signals (outputs non-negative frequencies only) |
| `07_centered_fftshift.py` | Zero-Centered Spectrum (`fftshift`) | Centering zero frequency to display a symmetric two-sided spectrum across $[-f_s/2, f_s/2]$ |
| `08_dominant_frequency.py` | Peak Frequency Detection | Extracting dominant frequency component programmatically using `np.argmax` on magnitude |
| `09_noisy_signal_fft.py` | Spectral Analysis in Noise | Detecting a $50\text{ Hz}$ sinusoid buried in Gaussian white noise |
| `10_amplitude_corrected_fft.py` | Step-by-Step Annotated Guide | Comprehensive walkthrough covering $T_s$, FFT, positive masking, and amplitude normalization |
| `11_compute_fft_utility.py` | Reusable FFT Function | Production-ready helper function `compute_fft(signal, sampling_rate)` returning `(f, magnitude)` |

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- NumPy
- Matplotlib

### Setup Virtual Environment
```bash
# Clone or navigate to the repository
cd /Users/shuvo/Sampling

# Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install required packages
pip install numpy matplotlib
```

---

## How to Run

### 1. Running the Master DSP Toolkit & Comprehensive Test Suite
- **Sequential Terminal Test Mode** (instantly executes and prints outputs for all 30 functions without GUI blocking):
  ```bash
  python3 test_template.py
  ```
- **Comprehensive Visual Demonstration Mode** (generates and displays 7 multi-panel Matplotlib figures covering continuous waveforms, uniform sampling, aliasing collisions, sinc interpolation pulses, Whittaker-Shannon reconstruction, spectral replication, low-pass filtering, and DFT/IDFT phase/magnitude):
  ```bash
  python3 test_template.py --plot
  ```

### 2. Practicing Timed Exams in `/Mahdi`
1. Navigate into any problem folder:
   ```bash
   cd Mahdi/01_Easy_Uniform_Sampling
   ```
2. Open `statement.pdf` to read the prompt and input/output contracts.
3. Edit `template.py` and implement the `TODO` functions.
4. Run your solution:
   ```bash
   python3 template.py
   ```
5. Compare your implementation with the reference solution:
   ```bash
   python3 solution.py
   ```

### 3. Running GPT Problem Demonstrations
Run any of the 15 simulation problems directly to see the terminal breakdown and generated Matplotlib figure:
```bash
# Example: Problem 1 (Basic sampling and Nyquist check)
python3 gpt/problem1.py

# Example: Problem 7 (Sinc reconstruction)
python3 gpt/problem7.py

# Example: Problem 15 (Sampling + ADC Quantization)
python3 gpt/problem15.py
```

### 4. Running Sami Exam Solutions
To run any of the 18 worked exam problems:
```bash
# Example: Compare ZOH, Linear, and Sinc reconstruction
python3 Sami/AllSoln/13_compare_zoh_linear_and_sinc.py

# Example: Anti-aliasing filter before decimation
python3 Sami/AllSoln/08_anti_alias_filter_before_decimation.py
```

### 5. Running Fast Fourier Transform Modules (`/fft`)
Run any of the 11 FFT tutorial and analysis scripts:
```bash
# Example: Step-by-step amplitude-corrected FFT demonstration
python3 fft/10_amplitude_corrected_fft.py

# Example: Finding the dominant peak frequency in a multi-tone signal
python3 fft/08_dominant_frequency.py

# Example: Spectral analysis of a sinusoid buried in Gaussian noise
python3 fft/09_noisy_signal_fft.py
```

---

## Exam Quick-Reference Checklist

When solving sampling problems under exam conditions, verify these critical points:

1. **Strict Nyquist Inequality**:
   - $f_s > 2 f_{\max}$ (not $\ge$). If $x(t) = \sin(2\pi f_0 t)$ is sampled at exactly $f_s = 2 f_0$, all sample points land on zero crossings ($t = n / (2 f_0) \implies \sin(n\pi) = 0$).
2. **Frequency Folding Formula**:
   - Calculate $k = \operatorname{round}(f_0 / f_s)$. The folded frequency is $f_{\text{alias}} = |f_0 - k f_s|$.
   - For a cosine, the folded phase is identical; for a sine, flipping across Nyquist reverses sign ($\sin(- \theta) = -\sin(\theta)$).
3. **Normalized Sinc Definition**:
   - NumPy's `np.sinc(x)` computes $\frac{\sin(\pi x)}{\pi x}$. Do **not** multiply the argument by $\pi$ when calling `np.sinc`.
   - The reconstruction formula with NumPy is:
     $$x_r(t) = \sum_{n} x[n] \cdot \text{np.sinc}\left(\frac{t - n T_s}{T_s}\right)$$
4. **Vectorized Sinc Implementation (Speed & Clean Code)**:
   ```python
   # t_eval: (M,), t_samples: (N,), x_samples: (N,)
   # Outer difference matrix: (M, N)
   dt = t_eval[:, None] - t_samples[None, :]
   x_recon = np.dot(np.sinc(dt / Ts), x_samples)
   ```
5. **DFT Bin Resolution**:
   - Each bin represents $\Delta f = \frac{f_s}{N}$ Hz.
   - To increase frequency resolution (smaller $\Delta f$), increase the observation duration $T = N \cdot T_s = N / f_s$.
   - Zero-padding interpolates the spectrum in frequency but does not improve physical resolution between two closely spaced continuous sinusoids.
6. **Decimation vs. Upsampling**:
   - **Downsampling by $M$**: Pre-filter with a digital low-pass filter ($f_{\text{cutoff}} = \frac{f_s}{2M}$) to prevent aliasing before keeping every $M$-th sample.
   - **Upsampling by $L$**: Insert $L-1$ zeros between samples, then post-filter with a low-pass filter (gain $L$, cutoff $\frac{f_s}{2L}$) to eliminate spectral imaging copies.
