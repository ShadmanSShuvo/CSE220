import numpy as np

x = np.array([1, 2, 3, 4])

# FFT
X = np.fft.fft(x)

# Inverse FFT
reconstructed = np.fft.ifft(X)

print("Original:")
print(x)

print("\nFFT:")
print(X)

print("\nReconstructed:")
print(reconstructed)
