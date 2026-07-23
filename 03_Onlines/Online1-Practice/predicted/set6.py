import numpy as np

INF = 8

def energy(x):
    x = np.asarray(x, dtype=float)
    return np.sum(np.abs(x) ** 2)

def average_power(x):
    x = np.asarray(x, dtype=float)
    return energy(x) / len(x)


# ---- System definitions ----

def sys_diff(x):
    """y[n] = x[n] - x[n-1]"""
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    y[1:] = x[1:] - x[:-1]
    return y

def sys_n_times_x(x):
    """y[n] = n * x[n], n = -8..8"""
    x = np.asarray(x, dtype=float)
    n = np.arange(-INF, INF + 1)
    return n * x

def sys_square(x):
    """y[n] = x[n]^2"""
    x = np.asarray(x, dtype=float)
    return x ** 2

def sys_add5(x):
    """y[n] = x[n] + 5"""
    x = np.asarray(x, dtype=float)
    return x + 5

def sys_centered_avg(x):
    """y[n] = 0.5*(x[n-1] + x[n] + x[n+1])"""
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    xm1 = np.zeros_like(x); xm1[1:] = x[:-1]
    xp1 = np.zeros_like(x); xp1[:-1] = x[1:]
    y = 0.5 * (xm1 + x + xp1)
    return y

def sys_reverse(x):
    """y[n] = x[-n]"""
    x = np.asarray(x, dtype=float)
    return x[::-1]


def check_linearity(system, x1, x2, a=2.0, b=-3.0):
    lhs = system(a * x1 + b * x2)
    rhs = a * system(x1) + b * system(x2)
    return np.allclose(lhs, rhs)

def check_time_invariance(system, x, shift_fn, k=2):
    """
    T{shift(x)} vs shift(T{x}), compared only on an interior window that
    is unaffected by the finite-array zero-padding at both ends (avoids
    false negatives from edge/boundary truncation rather than genuine
    time-variance).
    """
    shifted_then_sys = system(shift_fn(x, k))
    sys_then_shifted = shift_fn(system(x), k)
    margin = abs(k) + 2
    interior = slice(margin, len(x) - margin)
    return np.allclose(shifted_then_sys[interior], sys_then_shifted[interior])

def shift(x, k):
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

def check_causality_numerically(system):
    """
    Numeric causality check via impulse perturbation, defined in terms of
    actual TIME INDEX n (n = -8..8, array position = n+8), not raw array
    position. For each interior output time n0, perturb only the input
    sample at time n0+1 (strictly in n0's future) and see if the output
    at time n0 changes. A causal system's output at n0 must depend only
    on inputs at times <= n0, so it must be unaffected.
    """
    N = 17
    rng = np.random.default_rng(1)
    base = rng.standard_normal(N)
    y_base = system(base)

    causal = True
    for n0 in range(-INF + 3, INF - 3):  # interior times, avoid edge artifacts
        pos_now = n0 + INF               # array position of time n0
        for future_n in range(n0 + 1, INF - 2):  # any strictly future time
            pos_future = future_n + INF
            perturbed = base.copy()
            perturbed[pos_future] += 1.0
            y_pert = system(perturbed)
            if not np.isclose(y_base[pos_now], y_pert[pos_now]):
                causal = False
                break
        if not causal:
            break
    return causal


if __name__ == "__main__":
    x = np.array([0,0,0,0,0,0,0.5,2,1,0.5,1,0,0,0,0,0,0])

    print("Energy:", energy(x))
    assert np.isclose(energy(x), np.sum(x**2))
    print("Average power:", average_power(x))

    rng = np.random.default_rng(0)
    x1 = rng.standard_normal(17)
    x2 = rng.standard_normal(17)

    systems = {
        "x[n]-x[n-1]": sys_diff,
        "n*x[n]": sys_n_times_x,
        "x[n]^2": sys_square,
        "x[n]+5": sys_add5,
        "centered avg": sys_centered_avg,
        "x[-n]": sys_reverse,
    }

    expected = {
        "x[n]-x[n-1]": (True, True, True),
        "n*x[n]": (True, False, True),
        "x[n]^2": (False, True, True),
        "x[n]+5": (False, True, True),
        "centered avg": (True, True, False),
        "x[-n]": (True, False, False),
    }

    print(f"\n{'System':<16}{'Linear':<10}{'TimeInv':<10}{'Causal':<10}")
    for name, fn in systems.items():
        lin = check_linearity(fn, x1, x2)
        ti = check_time_invariance(fn, x1, shift, k=2)
        causal = check_causality_numerically(fn)
        print(f"{name:<16}{str(lin):<10}{str(ti):<10}{str(causal):<10}")
        exp_lin, exp_ti, exp_causal = expected[name]
        assert lin == exp_lin, f"{name}: linearity mismatch"
        assert ti == exp_ti, f"{name}: time-invariance mismatch"
        assert causal == exp_causal, f"{name}: causality mismatch"

    print("\nAll Set 6 checks passed (matches answer key).")