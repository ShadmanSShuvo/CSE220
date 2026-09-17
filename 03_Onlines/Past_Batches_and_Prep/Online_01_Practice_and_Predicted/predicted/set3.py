import numpy as np

INF = 8
N = np.arange(-INF, INF + 1)

def time_scale_signal(x, k):
    """
    y[n] = x[n/k], k positive integer (up-scaling / expansion).
    Where n/k is an integer -> copy sample; else -> 0.
    """
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    ratio = N / k
    is_int = np.isclose(ratio, np.round(ratio))
    valid = is_int & (ratio >= -INF) & (ratio <= INF)
    src_idx = np.round(ratio[valid]).astype(int) + INF
    dst_idx = N[valid] + INF
    y[dst_idx] = x[src_idx]
    return y

def time_scale_signal_interpolate(x, k):
    """
    Same as above, but non-integer n/k positions get the average of the
    floor and ceil neighbor samples.
    """
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    ratio = N / k

    lo = np.floor(ratio).astype(int)
    hi = np.ceil(ratio).astype(int)

    in_range = (lo >= -INF) & (hi <= INF)

    lo_idx = lo[in_range] + INF
    hi_idx = hi[in_range] + INF
    dst_idx = N[in_range] + INF

    y[dst_idx] = 0.5 * (x[lo_idx] + x[hi_idx])
    return y


if __name__ == "__main__":
    x = np.array([0,0,0,0,0,0,0.5,2,1,0.5,1,0,0,0,0,0,0])

    # k = 1 must return original unchanged, both functions
    y1 = time_scale_signal(x, 1)
    y1i = time_scale_signal_interpolate(x, 1)
    print("k=1 (task1):", y1)
    print("k=1 (task2):", y1i)
    assert np.allclose(y1, x)
    assert np.allclose(y1i, x)

    y3 = time_scale_signal(x, 3)
    y3i = time_scale_signal_interpolate(x, 3)
    print("k=3 (task1, zeros between):", y3)
    print("k=3 (task2, interpolated):", y3i)

    # Spot check the example from the prompt: k=3, n=-1 -> avg(x[0], x[-1])
    idx0 = 0 + INF
    idx_m1 = -1 + INF
    expected = 0.5 * (x[idx0] + x[idx_m1])
    got = y3i[-1 + INF]
    print(f"n=-1 interpolated: got={got}, expected={expected}")
    assert np.isclose(got, expected)

    print("All Set 3 checks passed.")