import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. SIGNAL
# ============================================================

def signal(t):
    """
    x(t) = cos(2*pi*50*t) + 0.5*cos(2*pi*100*t)
    """
    return (
        np.cos(2 * np.pi * 50 * t)
        + 0.5 * np.cos(2 * np.pi * 100 * t)
    )


# ============================================================
# 2. SINC
# ============================================================

def sinc(u):
    """
    Normalized sinc:
        sinc(u) = sin(pi*u) / (pi*u)

    sinc(0) = 1
    """

    if np.isscalar(u):
        if u == 0:
            return 1.0

        return np.sin(np.pi * u) / (np.pi * u)

    u = np.asarray(u, dtype=float)

    result = np.ones_like(u)

    nonzero = (u != 0)
    result[nonzero] = (
        np.sin(np.pi * u[nonzero])
        / (np.pi * u[nonzero])
    )

    return result


# ============================================================
# 3. SINC INTERPOLATION PULSE
# ============================================================

def sinc_pulse(t, n, T):
    """
    sinc interpolation pulse centered at nT:

        sinc((t - nT) / T)
    """

    return sinc((t - n * T) / T)


# ============================================================
# 4. SINC RECONSTRUCTION
# ============================================================

def sinc_reconstruct(t, n, x_samples, T):
    """
    Reconstruct the signal at one time t.
    """

    result = 0.0

    for i in range(len(n)):
        result += (
            x_samples[i]
            * sinc_pulse(t, n[i], T)
        )

    return result


def reconstruct_signal(t_values, n, x_samples, T):
    """
    Reconstruct the signal at many time points.
    """

    reconstructed = np.zeros(len(t_values))

    for i in range(len(t_values)):
        reconstructed[i] = sinc_reconstruct(
            t_values[i],
            n,
            x_samples,
            T
        )

    return reconstructed


# ============================================================
# 5. MAIN DEMO
# ============================================================

def main():

    # --------------------------------------------------------
    # Sampling parameters
    # --------------------------------------------------------

    fs = 500          # Sampling frequency
    T = 1 / fs        # Sampling period

    start_time = 0
    end_time = 0.1

    # --------------------------------------------------------
    # Continuous-time signal
    # --------------------------------------------------------

    t = np.linspace(
        start_time,
        end_time,
        2000
    )

    x = signal(t)

    # --------------------------------------------------------
    # Sample the signal
    # --------------------------------------------------------

    n = np.arange(
        int(start_time / T),
        int(end_time / T) + 1
    )

    t_samples = n * T

    x_samples = signal(t_samples)

    # --------------------------------------------------------
    # Sinc reconstruction
    # --------------------------------------------------------

    x_reconstructed = reconstruct_signal(
        t,
        n,
        x_samples,
        T
    )

    # --------------------------------------------------------
    # Plot
    # --------------------------------------------------------

    plt.figure(figsize=(10, 5))

    # Original signal
    plt.plot(
        t,
        x,
        label="Original Signal"
    )

    # Reconstructed signal
    plt.plot(
        t,
        x_reconstructed,
        "--",
        label="Sinc Reconstruction"
    )

    # Samples
    plt.scatter(
        t_samples,
        x_samples,
        s=25,
        label="Samples"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Sinc Interpolation / Signal Reconstruction")

    plt.grid()
    plt.legend()

    plt.show()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
