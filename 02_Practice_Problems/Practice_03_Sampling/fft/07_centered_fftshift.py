import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

x = np.sin(2*np.pi*50*t)

X = np.fft.fft(x)

f = np.fft.fftfreq(len(x), 1/fs)

# Shift zero frequency to center
X_shifted = np.fft.fftshift(X)
f_shifted = np.fft.fftshift(f)

plt.plot(f_shifted, np.abs(X_shifted))

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Centered FFT Spectrum")
plt.xlim(-200, 200)
plt.grid()

plt.show()
