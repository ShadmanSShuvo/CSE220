import numpy as np
import matplotlib.pyplot as plt
def compute_fft(signal, sampling_rate):

    N = len(signal)

    # FFT
    X = np.fft.rfft(signal)

    # Frequencies
    f = np.fft.rfftfreq(N, 1/sampling_rate)

    # Magnitude
    magnitude = np.abs(X) / N

    # One-sided amplitude correction
    if N > 1:
        magnitude[1:-1] *= 2

    return f, magnitude


fs = 1000
t = np.arange(0, 1, 1/fs)

x = (
    3 * np.sin(2*np.pi*50*t)
    + 1.5 * np.sin(2*np.pi*120*t)
)

f, magnitude = compute_fft(x, fs)

plt.plot(f, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 200)
plt.grid()
plt.show()
