import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. SIGNAL GENERATION
# ============================================================

def generate_signal(t, components):
    """
    components = [(amplitude, frequency, phase), ...]
    x(t) = sum A*cos(2*pi*f*t + phase)
    """

    x = np.zeros(len(t))

    for i in range(len(components)):
        A = components[i][0]
        f = components[i][1]
        phase = components[i][2]

        x += A * np.cos(2.0 * np.pi * f * t + phase)

    return x


# Example signal:
# x(t) = cos(2*pi*50*t) + 0.5*cos(2*pi*100*t)

def example_signal(t):
    components = [
        (1.0, 50.0, 0.0),
        (0.5, 100.0, 0.0)
    ]

    return generate_signal(t, components)


# ============================================================
# 2. TIME AXIS
# ============================================================

def create_time_axis(start_time, end_time, count):
    return np.linspace(start_time, end_time, count)


# ============================================================
# 3. SAMPLING
# ============================================================

def get_sampling_interval(fs):
    return 1.0 / fs


def sample_signal(signal, fs, start_time, end_time):
    """
    Samples the given signal function.
    """

    T = 1.0 / fs

    start_index = int(np.ceil(start_time / T))
    end_index = int(np.floor(end_time / T))

    n = np.arange(start_index, end_index + 1)
    t_samples = n * T
    x_samples = signal(t_samples)

    return n, t_samples, x_samples


# ============================================================
# 4. NYQUIST-SHANNON
# ============================================================

def get_nyquist_rate(fmax):
    return 2.0 * fmax


def classify_sampling_frequency(fs, fmax):
    nyquist_rate = 2.0 * fmax

    if fs > nyquist_rate:
        return "Safe"

    if fs == nyquist_rate:
        return "Boundary"

    return "High-risk"


# ============================================================
# 5. ALIASING / FREQUENCY FOLDING
# ============================================================

def alias_frequency(f, fs):
    """
    Folds positive frequency into [0, fs/2].
    """

    f_reduced = f % fs

    if f_reduced <= fs / 2.0:
        return f_reduced

    return fs - f_reduced


def alias_frequency_signed(f, fs):
    """
    Folds frequency into [-fs/2, fs/2).
    """

    return ((f + fs / 2.0) % fs) - fs / 2.0


def compare_aliasing(f1, f2, fs, n):
    """
    Checks whether two frequencies produce
    the same samples.
    """

    T = 1.0 / fs

    x1 = np.cos(2.0 * np.pi * f1 * n * T)
    x2 = np.cos(2.0 * np.pi * f2 * n * T)

    return np.max(np.abs(x1 - x2))


# ============================================================
# 6. NORMALIZED SINC
# ============================================================

def sinc(u):
    """
    Normalized sinc:
        sinc(u) = sin(pi*u)/(pi*u)
    """

    if np.isscalar(u):
        if u == 0.0:
            return 1.0

        return np.sin(np.pi * u) / (np.pi * u)

    u = np.asarray(u, dtype=float)
    result = np.ones_like(u)

    nonzero = (u != 0.0)
    result[nonzero] = np.sin(np.pi * u[nonzero]) / (np.pi * u[nonzero])

    return result


# ============================================================
# 7. SINC INTERPOLATION PULSE
# ============================================================

def sinc_pulse(t, n, T):
    """
    sinc((t - nT)/T)
    """

    return sinc((t - n * T) / T)


# ============================================================
# 8. SINC RECONSTRUCTION
# ============================================================

def sinc_reconstruct(t, n, x_samples, T):
    """
    Reconstructs signal at one time t.
    """

    result = 0.0

    for i in range(len(n)):
        result += x_samples[i] * sinc_pulse(t, n[i], T)

    return result


def reconstruct_signal(t_values, n, x_samples, T):
    """
    Reconstructs signal at many time points.
    """

    reconstructed = np.zeros(len(t_values))

    for i in range(len(t_values)):
        reconstructed[i] = sinc_reconstruct(
            t_values[i], n, x_samples, T
        )

    return reconstructed


# ============================================================
# 9. RMSE
# ============================================================

def calculate_rmse(original, reconstructed):
    error = original - reconstructed
    return np.sqrt(np.mean(error * error))


# ============================================================
# 10. ANALYTICAL SPECTRUM
# ============================================================

def rectangular_spectrum(f, W):
    """
    X(f) = 1 for |f| <= W
           0 otherwise
    """

    if abs(f) <= W:
        return 1.0

    return 0.0


# ============================================================
# 11. SAMPLE-TRAIN SPECTRUM
# ============================================================

def sampled_spectrum(frequencies, fs, W, k_min, k_max):
    """
    Implements:

        Xp(f) = (1/T) * sum X(f - k*fs)
    """

    T = 1.0 / fs
    result = np.zeros(len(frequencies))

    for i in range(len(frequencies)):
        f = frequencies[i]

        for k in range(k_min, k_max + 1):
            shifted_f = f - k * fs
            result[i] += rectangular_spectrum(shifted_f, W)

        result[i] /= T

    return result


# ============================================================
# 12. VALID RECOVERY CUTOFF
# ============================================================

def is_valid_cutoff(W, fs, fc):
    """
    Valid range:

        W < fc < fs - W
    """

    return W < fc < fs - W


# ============================================================
# 13. IDEAL LOW-PASS FILTER
# ============================================================

def ideal_lowpass(frequencies, fc):
    """
    H(f) = 1 for |f| <= fc
           0 otherwise
    """

    H = np.zeros(len(frequencies))

    for i in range(len(frequencies)):
        if abs(frequencies[i]) <= fc:
            H[i] = 1.0

    return H


# ============================================================
# 14. APPLY FREQUENCY-DOMAIN FILTER
# ============================================================

def apply_filter(spectrum, filter_response):
    return spectrum * filter_response


# ============================================================
# 15. MANUAL SPECTRAL RECOVERY
# ============================================================

def recover_central_spectrum(frequencies, sampled_spectrum_values, fc):
    """
    Keeps only the central copy |f| <= fc.
    """

    recovered = np.zeros(len(sampled_spectrum_values))

    for i in range(len(frequencies)):
        if abs(frequencies[i]) <= fc:
            recovered[i] = sampled_spectrum_values[i]

    return recovered


# ============================================================
# 16. DFT
# ============================================================

def dft(x):
    """
    Manual DFT.
    No numpy.fft.
    """

    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            angle = -2.0 * np.pi * k * n / N
            X[k] += x[n] * (
                np.cos(angle) + 1j * np.sin(angle)
            )

    return X


# ============================================================
# 17. IDFT
# ============================================================

def idft(X):
    """
    Manual inverse DFT.
    """

    N = len(X)
    x = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            angle = 2.0 * np.pi * k * n / N
            x[n] += X[k] * (
                np.cos(angle) + 1j * np.sin(angle)
            )

        x[n] /= N

    return x


# ============================================================
# 18. DFT FREQUENCY AXIS
# ============================================================

def get_frequency_axis(N, fs):
    """
    Standard DFT frequency bins:

        f[k] = k*fs/N
    """

    frequencies = np.zeros(N)

    for k in range(N):
        frequencies[k] = k * fs / N

    return frequencies


def get_centered_frequency_axis(N, fs):
    """
    Frequency axis in signed form.
    """

    frequencies = np.zeros(N)

    for k in range(N):
        if k <= N // 2:
            frequencies[k] = k * fs / N
        else:
            frequencies[k] = (k - N) * fs / N

    return frequencies


# ============================================================
# 19. MANUAL FFTSHIFT
# ============================================================

def shift_spectrum(X):
    """
    Moves zero frequency to the center.
    """

    N = len(X)
    shifted = np.zeros(N, dtype=complex)
    half = N // 2

    for i in range(N):
        shifted[i] = X[(i + half) % N]

    return shifted


# ============================================================
# 20. MAGNITUDE AND PHASE
# ============================================================

def magnitude_spectrum(X):
    magnitude = np.zeros(len(X))

    for k in range(len(X)):
        magnitude[k] = abs(X[k])

    return magnitude


def phase_spectrum(X):
    phase = np.zeros(len(X))

    for k in range(len(X)):
        phase[k] = np.angle(X[k])

    return phase


# ============================================================
# 21. FREQUENCY CONVERSION
# ============================================================

def hz_to_rad(f):
    return 2.0 * np.pi * f


def rad_to_hz(omega):
    return omega / (2.0 * np.pi)


# ============================================================
# 22. EXAMPLE: SAMPLING + RECONSTRUCTION
# ============================================================

def run_sampling_demo():

    fs = 500.0
    fmax = 100.0

    start_time = 0.0
    end_time = 0.1

    T = get_sampling_interval(fs)

    print("T =", T)
    print("Nyquist rate =", get_nyquist_rate(fmax))
    print("Sampling =", classify_sampling_frequency(fs, fmax))

    # Original signal
    t = create_time_axis(start_time, end_time, 2000)
    x = example_signal(t)

    # Sampling
    n, t_samples, x_samples = sample_signal(
        example_signal, fs, start_time, end_time
    )

    # Sinc reconstruction
    x_reconstructed = reconstruct_signal(
        t, n, x_samples, T
    )

    # Error
    rmse = calculate_rmse(x, x_reconstructed)

    print("RMSE =", rmse)

    # Plot
    plt.figure()

    plt.plot(t, x, label="Original")
    plt.plot(t, x_reconstructed, label="Reconstructed")
    plt.scatter(t_samples, x_samples, s=15, label="Samples")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()

    plt.show()


# ============================================================
# 23. EXAMPLE: SAMPLED SPECTRUM
# ============================================================

def run_spectrum_demo():

    fs = 300.0
    W = 100.0

    frequencies = np.linspace(-800.0, 800.0, 2000)

    Xp = sampled_spectrum(
        frequencies, fs, W, -3, 3
    )

    plt.figure()

    plt.plot(frequencies, Xp)

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Sampled Spectrum")
    plt.grid()

    plt.show()


# ============================================================
# 24. EXAMPLE: MANUAL DFT
# ============================================================

def run_dft_demo():

    fs = 500.0

    n = np.arange(16)
    t = n / fs

    x = example_signal(t)

    X = dft(x)

    frequencies = get_frequency_axis(len(x), fs)
    magnitude = magnitude_spectrum(X)

    plt.figure()

    plt.stem(frequencies, magnitude)

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|X[k]|")
    plt.title("Manual DFT")
    plt.grid()

    plt.show()


# ============================================================
# MAIN
# ============================================================

def main():

    run_sampling_demo()

    # Uncomment when needed:
    # run_spectrum_demo()
    # run_dft_demo()


if __name__ == "__main__":
    main()
