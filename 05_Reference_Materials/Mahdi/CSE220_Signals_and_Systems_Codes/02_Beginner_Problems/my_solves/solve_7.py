"""P07 - Downsampling a discrete-time signal. Student template - fill in the ANSWER IMPLEMENTATION functions."""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#Keep every M-th sample
#This is different from y[n] = x[m*n] -> scaling

def x_of_n(n):
    """Given: a slow discrete cosine."""
    return np.cos(2 * np.pi * n / 12)


# ==========================================================
# ANSWER IMPLEMENTATION
# ==========================================================
def downsample(n, x, M):
    """Keep every M-th sample: y[k] = x[M*k]. Return the new index array and
    the downsampled values. (This is array slicing with a step.)"""
    n_new = n[::M]
    y = x[::M]
    return n_new,y


def stem(ax, n, x, title, color=None):
    ml, sl, bl = ax.stem(n, x)
    bl.set_visible(False)
    if color:
        ml.set_color(color); sl.set_color(color)
    ax.set_title(title); ax.set_xlabel("n"); ax.grid(True, alpha=0.3)


def main():
    n = np.arange(0, 24)
    x = x_of_n(n)

    n2, x2 = downsample(n, x, 2)
    n3, x3 = downsample(n, x, 3)

    fig, axs = plt.subplots(3, 1, figsize=(9, 7))
    stem(axs[0], n, x, "original x[n]")
    stem(axs[1], n2, x2, "downsampled by M=2", color="C1")
    stem(axs[2], n3, x3, "downsampled by M=3", color="C2")
    plt.show()
    assert len(x2) == len(x[::2])
    assert np.allclose(x2, x[::2])
    assert np.allclose(x3, x[::3]) and np.array_equal(n3, n[::3])
    print(f"[P07] M=2 keeps {len(x2)} of {len(x)} samples, "
          f"M=3 keeps {len(x3)}  -> passed.")


if __name__ == "__main__":
    main()
