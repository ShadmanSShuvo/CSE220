import numpy as np
from transforms import DFTAnalyzer, ArbitraryLengthFFT

dft = DFTAnalyzer()
arb = ArbitraryLengthFFT()

for N in range(1, 21):
    x = np.random.randn(N) + 1j * np.random.randn(N)

    X_dft = dft.transform(x)
    X_arb = arb.transform(x)

    assert np.allclose(X_dft, X_arb, atol=1e-9, rtol=1e-9), \
        f"Forward failed for N={N}"

    x_recovered = arb.inverse(X_arb)

    assert np.allclose(x, x_recovered, atol=1e-9, rtol=1e-9), \
        f"Inverse failed for N={N}"

print("All arbitrary-length FFT tests passed!")
