import numpy as np
from set1 import time_shift_signal, time_scale_signal

INF = 8
N = np.arange(-INF, INF + 1)

def transform(x, alpha, beta):
    """
    y[n] = x[alpha*n + beta], alpha nonzero integer, beta integer.
    Direct evaluation on the argument avoids operation-order bugs.
    """
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    arg = alpha * N + beta
    valid = (arg >= -INF) & (arg <= INF)
    y[N[valid] + INF] = x[arg[valid] + INF]
    return y

def reverse_signal(x):
    return np.asarray(x, dtype=float)[::-1]


if __name__ == "__main__":
    x = np.array([0,0,0,0,0,0,0.5,2,1,0.5,1,0,0,0,0,0,0])

    # Task 1: y[n] = x[-2n + 1] via single call
    y_direct = transform(x, -2, 1)
    print("x[-2n+1] direct   :", y_direct)

    # Task 2a: compose via shift, reverse, scale
    # x[-2n+1] = x[-2(n - 1/2)] ... integer beta means we do it as:
    # Let w[n] = x[n+1] (shift left by 1, i.e. time_shift with k=-1)
    # Then apply reversal: w[-n] = x[-n+1]
    # Then scale by 2: w[-n] evaluated at 2n -> x[-2n+1]
    w = time_shift_signal(x, -1)      # w[n] = x[n+1]
    w_rev = reverse_signal(w)          # w_rev[n] = w[-n] = x[-n+1]
    y_composed = time_scale_signal(w_rev, 2)  # y[n] = w_rev[2n] = x[-2n+1]
    print("x[-2n+1] composed :", y_composed)
    assert np.allclose(y_direct, y_composed), "composition mismatch!"

    # Task 2b: order-of-operations demo
    # x[-2n+1]  : shift-then-scale in one order
    y_a = transform(x, -2, 1)
    # x[-2(n+1)] = x[-2n - 2] : different beta arising if shift applied
    # AFTER scaling instead of before
    y_b = transform(x, -2, -2)
    print("x[-2n+1]   :", y_a)
    print("x[-2(n+1)] :", y_b)
    # These differ because scaling by alpha first, then shifting by beta,
    # is not the same as shifting first, then scaling: shifting the INPUT
    # signal by 1 sample corresponds to shifting the OUTPUT index by 1/alpha
    # samples once scaling is applied, so applying shift before vs after
    # the scale changes the effective offset by a factor of alpha.
    assert not np.allclose(y_a, y_b), "expected these to differ"

    print("All Set 4 checks passed.")