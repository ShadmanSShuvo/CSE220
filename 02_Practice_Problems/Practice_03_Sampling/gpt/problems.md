## CSE220 Lab — Sampling Problems

### 1. Basic Sampling of a Sinusoid

Given

$$
x(t)=\sin(2\pi 5t)
$$

Sample the signal at:

* \(f_s=50\) Hz
* \(f_s=10\) Hz
* \(f_s=7\) Hz

**Tasks**

1. Generate the continuous-time approximation.
2. Generate the sampled signals.
3. Plot all three cases.
4. Determine which sampling frequencies satisfy the Nyquist criterion.
5. Explain what happens when \(f_s < 2f_{\max}\).

---

### 2. Nyquist Rate Detection

Consider

$$
x(t)=\sin(2\pi 10t)+0.5\sin(2\pi 25t)
$$

**Tasks**

1. Determine the highest frequency component.
2. Calculate the Nyquist rate.
3. Sample the signal at \(f_s=100, 50, 40,\) and \(30\) Hz.
4. Plot the sampled signals.
5. Identify the cases where aliasing occurs.

---

### 3. Demonstrate Aliasing

Generate

$$
x(t)=\sin(2\pi 35t)
$$

with sampling frequency

$$
f_s=50\text{ Hz}.
$$

**Tasks**

1. Sample the signal.
2. Calculate the apparent/aliased frequency.
3. Plot the original and sampled signals.
4. Verify the alias frequency experimentally.

**Expected concept:**
Students should discover that a 35-Hz sinusoid sampled at 50 Hz appears as a lower-frequency sinusoid.

---

### 4. Aliasing Frequency Calculator

Write a Python function:

```python
def alias_frequency(f, fs):
    ...
```

that returns the frequency observed after sampling a sinusoid of frequency \(f\) at sampling frequency \(f_s\).

Test it for:

|  \(f\) | \(f_s\) |
| -----: | ------: |
|  35 Hz |   50 Hz |
|  60 Hz |  100 Hz |
|  75 Hz |  100 Hz |
| 125 Hz |  100 Hz |
| 230 Hz |  100 Hz |

Plot the original frequency and corresponding alias frequency.

---

### 5. Sampling a Composite Signal

Given

$$
x(t)=2\cos(2\pi 5t)+\cos(2\pi 15t)+0.5\sin(2\pi 30t).
$$

**Tasks**

1. Find the minimum sampling frequency required to avoid aliasing.
2. Sample at exactly the Nyquist rate.
3. Sample above the Nyquist rate.
4. Sample below the Nyquist rate.
5. Compare the resulting plots.

---

### 6. Frequency-Domain View of Sampling ⭐

Consider

$$
x(t)=\cos(2\pi 10t).
$$

Sample it using an impulse train:

$$
p(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT_s).
$$

The sampled signal is

$$
x_s(t)=x(t)p(t).
$$

**Tasks**

1. Explain why sampling creates repeated spectra.
2. Numerically approximate the FFT of the sampled signal.
3. Plot the magnitude spectrum.
4. Repeat for:

   * \(f_s=100\) Hz
   * \(f_s=30\) Hz
   * \(f_s=15\) Hz
5. Identify spectral overlap.

---

### 7. Reconstruction Using Sinc Interpolation ⭐⭐

Given samples of

$$
x(t)=\sin(2\pi 5t)
$$

taken at \(f_s=20\) Hz.

Reconstruct the signal using sinc interpolation:

$$
x(t)=\sum_{n=-\infty}^{\infty}
x[n]\operatorname{sinc}\left(\frac{t-nT_s}{T_s}\right).
$$

**Tasks**

1. Generate the samples.
2. Implement sinc interpolation manually.
3. Reconstruct the signal.
4. Plot:

   * Original signal
   * Samples
   * Reconstructed signal
5. Calculate the reconstruction error.

---

### 8. Undersampling and Reconstruction Failure

Given

$$
x(t)=\sin(2\pi 40t)
$$

and

$$
f_s=50\text{ Hz}.
$$

**Tasks**

1. Sample the signal.
2. Reconstruct it using sinc interpolation.
3. Compare the reconstructed signal with the original.
4. Explain why perfect reconstruction is impossible even though sinc interpolation is used.

---

### 9. ECG-Like Signal Sampling

Generate a synthetic signal:

$$
x(t)=
\sin(2\pi 1.2t)
+0.3\sin(2\pi 15t)
+0.1\sin(2\pi 40t).
$$

Treat it as a simplified physiological signal.

**Tasks**

1. Determine its maximum frequency.
2. Calculate the Nyquist rate.
3. Sample it at \(f_s=100\), \(60\), and \(50\) Hz.
4. Plot the signals.
5. Compare their FFT spectra.
6. Discuss which components become distorted due to aliasing.

---

### 10. Audio Sampling Problem ⭐⭐

Generate a signal containing:

$$
f_1=500\text{ Hz},\qquad
f_2=3000\text{ Hz},\qquad
f_3=7000\text{ Hz}.
$$

Sample it at:

* 8 kHz
* 12 kHz
* 16 kHz

**Tasks**

1. Determine the Nyquist frequency for each sampling rate.
2. Determine which frequency components alias.
3. Calculate their alias frequencies.
4. Verify your calculations using FFT plots.

---

## Challenge Problems

### 11. Unknown Sampling Frequency

A sinusoidal signal has frequency

$$
f=17\text{ Hz}.
$$

After sampling, the observed frequency is 13 Hz.

Find **all possible sampling frequencies below 100 Hz** that could produce this alias.

Write a program to search for the possible values.

---

### 12. Design the Minimum Sampling Rate

Given

$$
x(t)=
\sin(2\pi 8t)
+2\cos(2\pi 17t)
+\cos(2\pi 31t)
+0.5\sin(2\pi 43t),
$$

find the **minimum sampling frequency** that allows perfect reconstruction.

Then write a program that automatically determines the required sampling rate for an arbitrary list of frequency components.

---

### 13. Sampling Theorem Visualizer ⭐⭐⭐

Build an interactive Python/Streamlit application with three inputs:

```text
Signal frequency:       [slider]
Sampling frequency:     [slider]
Observation duration:   [slider]
```

The application should display:

1. Original signal
2. Sampled signal
3. FFT of the sampled signal
4. Nyquist frequency
5. Whether aliasing occurs
6. Aliased frequency, if applicable

Example:

```text
Signal frequency: 35 Hz
Sampling frequency: 50 Hz

Nyquist frequency: 25 Hz
Aliasing: YES
Observed frequency: 15 Hz
```

This would make a particularly good **online lab problem** because students can visually explore the sampling theorem rather than simply calculating answers.

---

### 14. Reverse Engineering an Aliased Signal

You observe a sampled signal whose apparent frequency is **12 Hz**, sampled at

$$
f_s=40\text{ Hz}.
$$

**Tasks**

Find possible original frequencies in the range

$$
0<f<100\text{ Hz}
$$

that could produce the observed 12-Hz component.

Write a program that generates all possible frequencies.

---

### 15. Sampling + Quantization

Generate

$$
x(t)=\sin(2\pi 5t).
$$

Sample it at \(f_s=50\) Hz and quantize the samples using:

* 2 bits
* 3 bits
* 4 bits
* 8 bits

**Tasks**

1. Plot the quantized signals.
2. Calculate quantization error.
3. Calculate MSE.
4. Compare the effect of increasing the number of bits.

This introduces the distinction between **sampling** (time discretization) and **quantization** (amplitude discretization).
