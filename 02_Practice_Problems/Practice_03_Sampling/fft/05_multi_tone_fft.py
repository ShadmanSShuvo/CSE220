import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1

t = np.arange(0, duration, 1/fs)

# Three frequencies
x = (
    2 * np.sin(2 * np.pi * 50 * t)
    + 1 * np.sin(2 * np.pi * 120 * t)
    + 0.5 * np.sin(2 * np.pi * 200 * t)
)

# FFT
X = np.fft.fft(x)
f = np.fft.fftfreq(len(x), 1/fs)

mask = f >= 0

magnitude = np.abs(X) / len(x)
magnitude[1:-1] *= 2

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Original Signal")
plt.xlim(0, 0.1)
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(f[mask], magnitude[mask])
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.xlim(0, 250)
plt.grid()

plt.tight_layout()
plt.show()
