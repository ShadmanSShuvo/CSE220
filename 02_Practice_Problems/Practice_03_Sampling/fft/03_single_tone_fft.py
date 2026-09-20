import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1

t = np.arange(0, duration, 1/fs)

# 50 Hz sine wave
x = np.sin(2 * np.pi * 50 * t)

# FFT
X = np.fft.fft(x)
f = np.fft.fftfreq(len(x), 1/fs)

# Positive frequencies
mask = f >= 0

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.xlim(0, 0.1)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f[mask], np.abs(X[mask]) / len(x))
plt.title("FFT")
plt.xlabel("Frequency (Hz)")
plt.xlim(0, 100)
plt.grid()

plt.tight_layout()
plt.show()
