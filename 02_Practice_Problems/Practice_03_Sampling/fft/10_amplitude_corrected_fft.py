import numpy as np
import matplotlib.pyplot as plt

# 1. Define time and sampling parameters
sampling_rate = 1000
time_step = 1.0 / sampling_rate
duration = 1.0

t = np.arange(0, duration, time_step)

# 2. Create a mixed signal
signal = (
    3 * np.sin(2 * np.pi * 50 * t)
    + 1.5 * np.sin(2 * np.pi * 120 * t)
)

# 3. Compute FFT
n_samples = len(signal)

fft_output = np.fft.fft(signal)
frequencies = np.fft.fftfreq(n_samples, d=time_step)

# 4. Calculate magnitude
magnitude = np.abs(fft_output) / n_samples

# 5. Keep only positive frequencies
positive_mask = frequencies >= 0

frequencies = frequencies[positive_mask]
magnitude = magnitude[positive_mask]

# 6. Correct amplitude for one-sided spectrum
magnitude[1:-1] *= 2

# ============================================================
# 7. Plot
# ============================================================

plt.figure(figsize=(10, 7))

# Original signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)

plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 0.1)       # Show first 0.1 seconds
plt.grid()

# Frequency spectrum
plt.subplot(2, 1, 2)
plt.stem(frequencies, magnitude)

plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 200)
plt.grid()

plt.tight_layout()
plt.show()
