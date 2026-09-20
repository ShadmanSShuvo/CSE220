import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

x = np.sin(2*np.pi*100*t)

X = np.fft.rfft(x)
f = np.fft.rfftfreq(len(x), 1/fs)

magnitude = np.abs(X) / len(x)
magnitude[1:-1] *= 2

plt.plot(f, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 200)
plt.grid()
plt.show()
