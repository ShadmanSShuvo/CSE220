"""
transforms.py  --  YOUR CODE GOES HERE.

The shared transform core used by BOTH tasks. Write it once; bigmul.py
(Task A) and image_conv.py (Task B) import it.

Nothing in this file may call numpy.fft, scipy.fft, numpy.convolve,
scipy.signal, or any other library routine that performs a Fourier
transform, a convolution or a correlation for you. NumPy is for array
arithmetic only.

A quick self-test you should run before touching either application:

    import numpy as np
    from transforms import DFTAnalyzer, FFTTransformer
    x = np.random.randn(64) + 1j * np.random.randn(64)
    d, f = DFTAnalyzer(), FFTTransformer()
    assert np.max(np.abs(d.transform(x) - f.transform(x))) < 1e-9
    assert np.max(np.abs(d.inverse(d.transform(x)) - x)) < 1e-9
"""

import numpy as np


def next_power_of_two(n):
    """
    Return the smallest power of two that is >= ``n`` (and at least 1).

    Both tasks need this to choose a transform length for the radix-2 FFT.
    """
    # TODO: implement this function
    n = int(n)
    if n < 1:
        return 1
    k = 0
    while (1 << k) < n:
        k += 1
    return 1 << k


class DFTAnalyzer:
    """
    The Discrete Fourier Transform, computed straight from its definition.

        Analysis:   X[k] = sum_{n=0}^{N-1} x[n] * exp(-2j*pi*k*n/N)
        Synthesis:  x[n] = (1/N) * sum_{k=0}^{N-1} X[k] * exp(+2j*pi*k*n/N)

    How you write it is up to you -- a literal double loop, a precomputed
    table of twiddle factors indexed by (k*n) % N, or a NumPy expression --
    as long as it computes these sums directly and is not secretly an FFT.
    """

    name = "dft"

    def transform(self, x):
        """
        Forward DFT.

        Parameters
        ----------
        x : 1D array_like, length N (real or complex)

        Returns
        -------
        numpy.ndarray of complex128, shape (N,)
        """
        # TODO: implement this method
        x = np.asarray(x, dtype=np.complex128)
        N = len(x)

        spectrum = np.zeros(N, dtype=np.complex128)

        for k in range(N):
            for n in range(N):
                angle = -2j * np.pi * k * n / N
                spectrum[k] += x[n] * np.exp(angle)

        return spectrum

    def inverse(self, spectrum):
        """
        Inverse DFT, including the 1/N factor.

        Parameters
        ----------
        spectrum : 1D array_like, length N (complex)

        Returns
        -------
        numpy.ndarray of complex128, shape (N,)
            Do NOT discard the imaginary part here -- the caller decides when
            it is safe to take .real.
        """
        # TODO: implement this method
        spectrum = np.asarray(spectrum, dtype=np.complex128)
        N = len(spectrum)
        return np.conj(self.transform(np.conj(spectrum))) / N


class FFTTransformer(DFTAnalyzer):
    """
    Radix-2 decimation-in-time (Cooley-Tukey) FFT, in O(N log N).

    It inherits from DFTAnalyzer so that both applications can treat the two
    interchangeably: they call ``engine.transform(...)`` and
    ``engine.inverse(...)`` without caring which engine they hold.

    Requirements:
      * Recursive or iterative (with bit-reversal permutation) -- your choice.
      * N must be a power of two; raise ValueError for any other length.
        The caller is responsible for zero-padding up to next_power_of_two.
      * The inverse must reuse the same butterfly machinery (conjugated
        twiddles, or conjugate-transform-conjugate), not a second copy of it.
      * Twiddle factors for a stage are computed once per stage, never once
        per butterfly.
    """

    name = "fft"

    def _fft(self, x, inverse=False):
        """Shared FFT butterfly machinery."""
        x = np.asarray(x, dtype=np.complex128)
        N = len(x)

        # FFT requires N to be a power of two.
        if N < 1 or (N & (N - 1)) != 0:
            raise ValueError("FFT length must be a power of two")


        result = np.empty(N, dtype=np.complex128)

        bits = N.bit_length() - 1

        for i in range(N):
            reversed_i = 0
            value = i

            for _ in range(bits):
                reversed_i = (reversed_i << 1) | (value & 1)
                value >>= 1

            result[reversed_i] = x[i]

        size = 2

        while size <= N:
            half = size // 2
            sign = 1 if inverse else -1
            twiddles = np.exp(
                sign * 2j * np.pi * np.arange(half) / size
            )

            for start in range(0, N, size):
                for j in range(half):
                    even = result[start + j]
                    odd = result[start + j + half]

                    t = twiddles[j] * odd

                    result[start + j] = even + t
                    result[start + j + half] = even - t

            size *= 2

        if inverse:
            result /= N

        return result

    def transform(self, x):
        """Forward FFT. Same contract as DFTAnalyzer.transform."""
        # TODO: implement this method
        return self._fft(x, inverse=False)

    def inverse(self, spectrum):
        """Inverse FFT, including the 1/N factor."""
        # TODO: implement this method
        return self._fft(spectrum, inverse=True)


# ---------------------------------------------------------------------------
# BONUS (optional) -- arbitrary-length FFT.
#
# Delete this class if you are not attempting the bonus. If you do attempt it,
# run both tasks with --engine arbitrary and leave those output directories in
# your submission as the evidence.
# ---------------------------------------------------------------------------
class ArbitraryLengthFFT(FFTTransformer):
    """
    Bonus: an O(N log N) transform for ANY length N, not just powers of two.

    Bluestein's chirp-z algorithm is the usual route: rewrite the DFT as a
    convolution of two chirp sequences, and evaluate that convolution with a
    radix-2 FFT of length >= 2N-1. A mixed-radix Cooley-Tukey that factorises
    N is equally acceptable.

    With this engine, Task A no longer has to pad the digit arrays up to a
    power of two, and Task B no longer has to pad the image up to one.
    """

    name = "arbitrary"

    def transform(self, x):
        # TODO (bonus): implement this method
        x = np.asarray(x, dtype=np.complex128)
        N = len(x)

        if N == 0:
            return np.array([], dtype=np.complex128)

        M = next_power_of_two(2 * N - 1)

        n = np.arange(N)

        chirp = np.exp(-1j * np.pi * n * n / N)

        # a[n] = x[n] * exp(-pi*i*n^2/N)
        a = np.zeros(M, dtype=np.complex128)
        a[:N] = x * chirp

        # b[m] = exp(+pi*i*m^2/N)
        # We need indices -(N-1) ... (N-1).
        # Store negative indices at the end of the FFT array.
        b = np.zeros(M, dtype=np.complex128)

        b[:N] = np.exp(1j * np.pi * n * n / N)

        for m in range(1, N):
            b[M - m] = b[m]


        A = super()._fft(a, inverse=False)
        B = super()._fft(b, inverse=False)

        convolution = super()._fft(A * B, inverse=True)

        result = np.zeros(N, dtype=np.complex128)

        for k in range(N):
            result[k] = (
                convolution[k]
                * np.exp(-1j * np.pi * k * k / N)
            )

        return result

    def inverse(self, spectrum):
        # TODO (bonus): implement this method
        spectrum = np.asarray(spectrum, dtype=np.complex128)
        N = len(spectrum)

        if N == 0:
            return np.array([], dtype=np.complex128)

        # IDFT(X) = conjugate(DFT(conjugate(X))) / N
        return np.conjugate(
            self.transform(np.conjugate(spectrum))
        ) / N


class NTTTransformer:
    """
    Number Theoretic Transform modulo 998244353.
    998244353 = 119 x 2^23 + 1
    Primitive root = 3.
    Supports lengths that are powers of two.
    """

    MOD = 998244353
    ROOT = 3
    name = "ntt"

    def _ntt(self, a, inverse=False):
        a = np.asarray(a, dtype=np.int64).copy()
        N = len(a)

        if N < 1 or (N & (N - 1)) != 0:
            raise ValueError("NTT length must be a power of two")

        # Bit-reversal permutation
        bits = N.bit_length() - 1

        for i in range(N):
            j = 0
            x = i

            for _ in range(bits):
                j = (j << 1) | (x & 1)
                x >>= 1

            if i < j:
                a[i], a[j] = a[j], a[i]

        # Cooley-Tukey butterflies
        length = 2

        while length <= N:
            # primitive length-th root
            wlen = pow(
                self.ROOT,
                (self.MOD - 1) // length,
                self.MOD
            )

            if inverse:
                wlen = pow(wlen, self.MOD - 2, self.MOD)

            half = length // 2

            for start in range(0, N, length):
                w = 1

                for j in range(half):
                    u = int(a[start + j])
                    v = (int(a[start + j + half]) * w) % self.MOD

                    a[start + j] = (u + v) % self.MOD
                    a[start + j + half] = (u - v) % self.MOD

                    w = (w * wlen) % self.MOD

            length *= 2

        # Inverse transform needs multiplication by N^-1
        if inverse:
            inv_N = pow(N, self.MOD - 2, self.MOD)
            a = (a * inv_N) % self.MOD

        return a.astype(np.int64)

    def transform(self, x):
        return self._ntt(x, inverse=False)

    def inverse(self, spectrum):
        return self._ntt(spectrum, inverse=True)
