import numpy as np

x = np.array([1, 2, 3, 4])

X = np.fft.fft(x)

print("Signal:", x)
print("FFT:", X)
print("Magnitude:", np.abs(X))

x2 = np.fft.ifft(X)

print("Recovered signal:", x2)
