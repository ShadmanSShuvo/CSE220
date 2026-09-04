"""P10 - Sampling a continuous-time sinusoid. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def continuous_signal(t, f):
    """A 'continuous' cosine cos(2*pi*f*t) evaluated on a dense grid t."""
    return np.cos(2*np.pi*f*t)


def sample_times(fs, duration):
    """Sample instants 0, 1/fs, 2/fs, ... up to (but not including) duration."""
    return np.arange(0, duration, 1.0 / fs)
    #return np.linspace(0,duration,int(duration*fs),endpoint=False)


def sample_signal(f, fs, duration):
    """Return (sample_times, samples) of cos(2*pi*f*t) taken at rate fs."""
    ts = sample_times(fs,duration)
    return ts,continuous_signal(ts,f)


def main():
    f, duration = 2.0, 1.0
    t_dense = np.linspace(0, duration, 1000)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t_dense, continuous_signal(t_dense, f),
            "0.6", label="continuous cos(2*pi*2*t)")
    for fs, mark in [(20.0, "C0"), (5.0, "C3")]:
        ts, xs = sample_signal(f, fs, duration)
        ml, sl, bl = ax.stem(ts, xs, linefmt=mark, markerfmt=mark + "o")
        bl.set_visible(False)
        ml.set_label(f"samples at fs={fs:.0f} Hz")
    ax.set_title("Sampling a continuous-time sinusoid (f=2 Hz)")
    ax.set_xlabel("t"); ax.set_ylabel("Amplitude")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)
    plt.show()
    ts, xs = sample_signal(f, 20.0, duration)
    assert len(ts) == 20 and np.isclose(ts[1] - ts[0], 1 / 20)
    assert np.isclose(xs[0], 1.0)                      # cos(0) = 1
    print(f"[P10] fs=20 Hz gives {len(ts)} samples spaced {1/20:.3f}s; "
          f"Nyquist needs fs > 2f = 4 Hz  -> passed.")


if __name__ == "__main__":
    main()
