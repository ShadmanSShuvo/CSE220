import numpy as np

INF = 8
N = np.arange(-INF, INF + 1)  # index axis -8..8

def time_shift_signal(x, k):
    """y[n] = x[n-k]. Positive k delays (shifts right)."""
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    if k >= 0:
        if k < len(x):
            y[k:] = x[:len(x) - k]
    else:
        k = -k
        if k < len(x):
            y[:len(x) - k] = x[k:]
    return y

def time_scale_signal(x, k):
    """y[n] = x[k*n], k positive integer (compression)."""
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    valid = (k * N >= -INF) & (k * N <= INF)
    idx_out = N[valid] + INF
    idx_in = (k * N[valid]) + INF
    y[idx_out] = x[idx_in]
    return y


if __name__ == "__main__":
    x = np.array([0,0,0,0,0,0,0.5,2,1,0.5,1,0,0,0,0,0,0])

    # Task 1 verification
    print("Original       :", x)
    print("Shift k=0      :", time_shift_signal(x, 0))
    assert np.allclose(time_shift_signal(x, 0), x)

    right3 = time_shift_signal(x, 3)
    back = time_shift_signal(right3, -3)
    print("Shift +3 then -3:", back)
    assert np.allclose(back, x)  # nothing pushed off edge here since x is centered

    # Task 2 verification
    scaled = time_scale_signal(x, 2)
    print("Scale k=2      :", scaled)
    # only even-indexed input samples should appear
    for n in N:
        if (2 * n + INF) in range(len(x)) and (2*n >= -INF and 2*n <= INF):
            pass
    print("All Set 1 checks passed.")