import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000          # Sampling frequency (Hz)
T = 1              # Duration (seconds)
t = np.arange(0, T, 1/fs)

# Signal = 50 Hz + 120 Hz
x = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# ============================================================
# FFT
# ============================================================

N = len(x)

X = np.fft.fft(x)              # Compute FFT
freq = np.fft.fftfreq(N, 1/fs) # Frequency bins

# Magnitude
magnitude = np.abs(X) / N

# Only keep positive frequencies
positive = freq >= 0

# ============================================================
# Plot
# ============================================================

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Time Domain Signal")
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(freq[positive], magnitude[positive])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Spectrum")
plt.xlim(0, 200)
plt.grid()

plt.tight_layout()
plt.show()
