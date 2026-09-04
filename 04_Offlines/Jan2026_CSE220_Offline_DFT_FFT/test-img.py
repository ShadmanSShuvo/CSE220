import numpy as np

from image_conv import transform_2d
from transforms import DFTAnalyzer, FFTTransformer

plane = np.array([
    [1, 2],
    [3, 4]
], dtype=float)

dft = transform_2d(plane, DFTAnalyzer())
fft = transform_2d(plane, FFTTransformer())

print("DFT:")
print(dft)

print("\nFFT:")
print(fft)

print("\nSame:")
print(np.allclose(dft, fft, atol=1e-9))


plane = np.random.randn(8, 8)

dft = transform_2d(plane, DFTAnalyzer())
fft = transform_2d(plane, FFTTransformer())

assert np.allclose(dft, fft, atol=1e-9)

print("2D DFT and FFT agree!")
