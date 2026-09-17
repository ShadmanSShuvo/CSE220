# test transforms.py
import numpy as np
from transforms import DFTAnalyzer, FFTTransformer, ArbitraryLengthFFT

x = np.random.randn(64) + 1j * np.random.randn(64)

d = DFTAnalyzer()
f = FFTTransformer()

assert np.max(np.abs(d.transform(x) - f.transform(x))) < 1e-9
assert np.max(np.abs(d.inverse(d.transform(x)) - x)) < 1e-9

print("All tests passed!")


# FFT should agree with DFT
for N in [1, 2, 4, 8, 16, 32, 64]:
    x = np.random.randn(N) + 1j * np.random.randn(N)

    X_dft = d.transform(x)
    X_fft = f.transform(x)

    assert np.allclose(X_dft, X_fft, atol=1e-9)

    x_recovered = f.inverse(X_fft)

    assert np.allclose(x, x_recovered, atol=1e-9)

print("FFT/DFT tests passed!")


for N in [3, 5, 6, 7, 10, 15]:
    try:
        f.transform(np.ones(N))
        assert False, f"FFT accepted N={N}"
    except ValueError:
        pass

print("Invalid-length tests passed!")


dft = DFTAnalyzer()
arb = ArbitraryLengthFFT()

for N in range(1, 21):
    x = np.random.randn(N) + 1j * np.random.randn(N)

    X_dft = dft.transform(x)
    X_arb = arb.transform(x)

    assert np.allclose(
        X_dft,
        X_arb,
        atol=1e-9,
        rtol=1e-9
    ), f"Forward failed for N={N}"

    x_recovered = arb.inverse(X_arb)

    assert np.allclose(
        x,
        x_recovered,
        atol=1e-9,
        rtol=1e-9
    ), f"Inverse failed for N={N}"

print("All arbitrary-length FFT tests passed!")


test_lengths = [3, 5, 6, 7, 9, 10, 11, 13, 15, 17, 19, 25, 31]

for N in test_lengths:
    x = np.random.randn(N) + 1j * np.random.randn(N)

    assert np.allclose(
        dft.transform(x),
        arb.transform(x),
        atol=1e-9,
        rtol=1e-9
    )

print("Non-power-of-two tests passed!")
