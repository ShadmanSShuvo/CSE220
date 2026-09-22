# Section B: The Staircase Droops

> **Topic:** Zero-Order Hold (ZOH), Sinc Droop, and DFT Amplitude Measurement
> **Source Problem:** [`the-staircase-droops.md`](./the-staircase-droops.md)

---

## Overview

Physical Digital-to-Analog Converters (DACs) reconstruct continuous signals from discrete samples by holding each sample level constant until the next sample arrival time. This hardware operation is known as a **zero-order hold (ZOH)** and generates a piecewise-constant staircase waveform.

Holding each sample value for a duration of $T_s = 1/f_s$ attenuates higher frequencies in the passband. This high-frequency attenuation is termed **sinc droop**.

This assignment demonstrates:
1. Predicting theoretical ZOH gain attenuation via the normalized sinc function.
2. Generating an oversampled staircase waveform using `np.repeat(samples, upsample)`.
3. Measuring the fundamental tone amplitude from the staircase using Discrete Fourier Transform (`np.fft.rfft`).
4. Verifying agreement between predicted droop and measured amplitude across frequencies up to near-Nyquist.

---

## Key Theory & Formula

### 1. Zero-Order Hold Frequency Response
The continuous impulse response of a ZOH block is a rectangular pulse of duration $T_s$:
$$h_{\text{zoh}}(t) = u(t) - u(t - T_s)$$
Taking its Fourier Transform:
$$H_{\text{zoh}}(f) = T_s \, e^{-j \pi f T_s} \, \frac{\sin(\pi f T_s)}{\pi f T_s} = T_s \, e^{-j \pi f / f_s} \, \text{sinc}\left(\frac{f}{f_s}\right)$$
For a unit-amplitude cosine input $\cos(2\pi f t)$, the magnitude gain of the output is:
$$\text{gain}(f) = \left| \text{sinc}\left(\frac{f}{f_s}\right) \right| = \left| \frac{\sin(\pi f / f_s)}{\pi f / f_s} \right|$$
In decibels:
$$\text{droop (dB)} = 20 \log_{10}(\text{gain}(f))$$

> **Note on NumPy `sinc`:** In NumPy, `np.sinc(x)` computes $\frac{\sin(\pi x)}{\pi x}$, so `np.sinc(f / fs)` directly corresponds to the normalized formula.

---

## Implemented Functions

### 1. `zoh_gain(f, fs)`
Computes theoretical ZOH gain:
$$\text{gain} = \left|\text{np.sinc}\left(\frac{f}{f_s}\right)\right|$$

### 2. `measured_zoh_gain(f, fs, upsample, duration)`
1. Samples $\cos(2\pi f t)$ at rate $f_s$ over $[0, \text{duration})$.
2. Holds each discrete sample for `upsample` points on a fine grid running at $f_{s,\text{fine}} = \text{upsample} \cdot f_s$:
   ```python
   staircase = np.repeat(samples, upsample)
   ```
3. Extracts the tone amplitude at frequency $f$ using `tone_amplitude(staircase, upsample * fs, f)`.
4. Returns the measured gain (which equals the amplitude for unit input).

---

## Test Cases & Expected Results

Parameters: $f_s = 1000\text{ Hz}$, $\text{UPSAMPLE} = 100$, $\text{DURATION} = 0.1\text{ s}$, $\text{TOLERANCE} = 10^{-3}$:

| $f$ (Hz) | $f / f_s$ | Predicted Gain | Measured Gain | \|Error\| | Droop (dB) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | 0.05 | 0.9959 | 0.9959 | $4.10 \times 10^{-7}$ | $-0.04\text{ dB}$ |
| 100 | 0.10 | 0.9836 | 0.9836 | $1.62 \times 10^{-6}$ | $-0.14\text{ dB}$ |
| 200 | 0.20 | 0.9355 | 0.9355 | $6.16 \times 10^{-6}$ | $-0.58\text{ dB}$ |
| 300 | 0.30 | 0.8584 | 0.8584 | $1.27 \times 10^{-5}$ | $-1.33\text{ dB}$ |
| 450 | 0.45 | 0.6986 | 0.6987 | $2.33 \times 10^{-5}$ | $-3.11\text{ dB}$ |

Notice that near the Nyquist rate ($f = 450\text{ Hz}$, $f/f_s = 0.45$), the staircase droop exceeds $-3.1\text{ dB}$ (more than $30\%$ signal attenuation).

---

## How to Run

```bash
# Run solution
python3 solution.py

# Or run zoh.py
python3 zoh.py
```
