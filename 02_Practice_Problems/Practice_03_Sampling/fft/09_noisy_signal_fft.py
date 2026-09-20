import numpy as np
import matplotlib.pyplot as plt

fs = 1000
duration = 1

t = np.arange(0, duration, 1/fs)

# Clean signal
clean = np.sin(2 * np.pi * 50 * t)

# Random noise
noise = np.random.normal(0, 0.5, len(t))

# Noisy signal
x = clean + noise

# FFT
X = np.fft.rfft(x)
f = np.fft.rfftfreq(len(x), 1/fs)

magnitude = np.abs(X) / len(x)
magnitude[1:-1] *= 2

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Noisy Signal")
plt.xlim(0, 0.1)
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f, magnitude)
plt.title("FFT of Noisy Signal")
plt.xlabel("Frequency (Hz)")
plt.xlim(0, 200)
plt.grid()

plt.tight_layout()
plt.show()
