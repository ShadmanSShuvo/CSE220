# Offline 03: Discrete & Fast Fourier Transforms (DFT & FFT)

> **Source Specification:** [`Jan2026_CSE220_Offline_DFT_FFT.pdf`](./dev_workspace/Jan2026_CSE220_Offline_DFT_FFT.pdf)

---

## Overview

This assignment covers the computational foundation of the Discrete Fourier Transform (DFT), advanced Fast Fourier Transform (FFT) algorithms, and their real-world applications in polynomial arithmetic and 2D spatial filtering.

---

## Core Algorithms Implemented

### 1. Transform Engines (`transforms.py`)
- **Direct DFT (`DFTAnalyzer`)**: $O(N^2)$ direct Vandermonde matrix multiplication.
- **Radix-2 Cooley-Tukey FFT (`FFTTransformer`)**: $O(N \log N)$ recursive divide-and-conquer implementation with twiddle factor caching.
- **Arbitrary-Length FFT (`ArbitraryLengthFFT`)**: Bluestein's Chirp-Z algorithm converting arbitrary length $N$ transforms into powers-of-two convolutions:
  $$x_n = a_n \cdot b_n \implies X_k = b_k \sum_{n} (a_n b_n) \cdot b_{k-n}^*$$

### 2. Large Integer Multiplication (`bigmul.py`)
- Represents huge $N$-digit integers as coefficient polynomials $P(x) = \sum a_i x^i$ evaluated at base $x = 10$.
- Computes polynomial multiplication in $O(N \log N)$ via FFT:
  $$\text{FFT} \to \text{pointwise product} \to \text{IFFT} \to \text{carry propagation}$$

### 3. 2D Frequency-Domain Image Convolution (`image_conv.py`)
- Fast spatial filtering by multiplying 2D spectra in the frequency domain with full zero-padding to eliminate circular wrap-around artifacts.

---

## Workspace Structure

- [`dev_workspace/`](./dev_workspace/): Primary development environment with test scripts, benchmarks, and image inputs.
- [`starter/`](./starter/): Original template provided by course instructors.
- [`submission/`](./submission/): Official submitted package for student roll `2305025`.
- [`test_results_full/`](./test_results_full/): Exhaustive test outputs and performance logs.

---

## How to Run Benchmarks & Tests

```bash
cd dev_workspace

# Test arbitrary-length FFT
python3 test-arb.py

# Test 2D image convolution
python3 test-img.py

# Test Big-Integer FFT multiplication
python3 test-limbs.py
```
