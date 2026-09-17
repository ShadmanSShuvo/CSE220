"""
========================================================================
CSE 220 : Signals and Linear Systems  --  EXAM TEMPLATE
========================================================================
Discrete-signal convention (same as every CSE 220 online):
  - A signal is a NumPy array of length 2*INF+1  (INF = 8  ->  length 17)
  - It stores values for indices n = -8 .. 8
  - Anything outside that window is 0
  - Array position of index n  =  n + INF     (the "+8" rule)

CORE RULE for every transform  y[n] = x(alpha*n + beta):
  Keep the output axis FIXED. For each output index n, compute the
  argument (alpha*n + beta) and PULL x at that argument.
  -> integer arg inside [-8,8]  : copy that sample
  -> otherwise                  : 0
  (Solve alpha*n_new + beta = n_old for n_new if you prefer the push view;
   for x[2n] that means n_new = n_old/2, keeping only integer targets.)

TRAP CHECKLIST:
  [ ] reversal x[::-1] only OK because axis is symmetric (-8..8)
  [ ] shifts: use zero-padding (concatenate), NOT np.roll (roll wraps)
  [ ] scaling: never interpolate a discrete signal onto non-integer index
  [ ] even/odd: NO extra /2 on the odd term; check xe+xo == x
  [ ] plots: savefig BEFORE show; label axes + legend
  [ ] property tests: use np.allclose, not ==
  [ ] bonus marks: vectorize, no explicit python loops
========================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

INF = 8


# ----------------------------------------------------------------------
# Provided helpers (typically given in the online -- do not modify)
# ----------------------------------------------------------------------
def init_signal() -> np.ndarray:
    """Return a blank length-17 signal (all zeros) on n = -8..8."""
    return np.zeros(2 * INF + 1)


def plot(signal,
         title=None,
         y_range=(-1, 3),
         figsize=(8, 3),
         x_label='n (Time Index)',
         y_label='x[n]',
         saveTo=None):
    """Stem plot for a discrete signal stored on n = -8..8."""
    plt.figure(figsize=figsize)
    plt.xticks(np.arange(-INF, INF + 1, 1))
    y_range = (y_range[0], max(np.max(signal), y_range[1]) + 1)
    plt.ylim(*y_range)
    plt.stem(np.arange(-INF, INF + 1, 1), signal)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    if saveTo is not None:
        plt.savefig(saveTo)     # save BEFORE show
    plt.show()


def plot_pair(x, xr, t1="x[n]", t2="transformed", figsize=(8, 3)):
    """Overlay two discrete signals for comparison."""
    n = np.arange(-INF, INF + 1)
    plt.figure(figsize=figsize)
    plt.stem(n, x, linefmt='C0-', markerfmt='C0o', label=t1)
    plt.stem(n, xr, linefmt='C1-', markerfmt='C1o', label=t2)
    plt.xticks(n)
    plt.xlabel("n"); plt.ylabel("Amplitude")
    plt.grid(True); plt.legend()
    plt.show()


# ======================================================================
#  SECTION A -- BASIC TRANSFORMS
# ======================================================================

def time_shift_signal(x: np.ndarray, k: int) -> np.ndarray:
    """
    y[n] = x[n - k].   Positive k = delay (shift right), zeros fill in.
    Use zero-padded concatenate (NOT np.roll).
    """
    if k > 0:
        return np.concatenate((np.zeros(k), x[:-k]))
    elif k < 0:
        return np.concatenate((x[-k:], np.zeros(-k)))
    return x.copy()


def time_reverse_signal(x: np.ndarray) -> np.ndarray:
    """
    y[n] = x[-n].   Axis is symmetric about 0 (n=-8..8), so slicing works.
    (On an asymmetric axis you would also need to flip the axis: -n[::-1].)
    """
    return x[::-1]


def time_scale_compress(x: np.ndarray, k: int) -> np.ndarray:
    """
    y[n] = x[k n]   (compression / downsampling, positive integer k).
    PULL: for each output n, read x at index k*n. Out of range -> 0.
    """
    arg = np.arange(-INF, INF + 1) * k          # k*n for each output n
    out = np.zeros_like(x)
    in_range = (arg >= -INF) & (arg <= INF)
    out[in_range] = x[arg[in_range] + INF]      # +INF maps index -> position
    return out


def time_scale_expand_zeros(x: np.ndarray, k: int) -> np.ndarray:
    """
    y[n] = x[n/k]   (expansion, positive integer k), GAPS SET TO 0.
    Only integer n/k are real samples; the rest are 0.
    """
    m = np.arange(-INF, INF + 1) / k
    is_int = (m == np.round(m))
    mi = np.round(m).astype(int)
    out = np.zeros_like(x)
    ok = is_int & (mi >= -INF) & (mi <= INF)
    out[ok] = x[mi[ok] + INF]
    return out


def time_scale_expand_interp(x: np.ndarray, k: int) -> np.ndarray:
    """
    y[n] = x[n/k]   (expansion), GAPS FILLED BY AVERAGING NEIGHBOURS.
    Each non-integer n/k -> average of x at floor(n/k) and ceil(n/k).
    (This is linear interpolation for the discrete case.)
    """
    m = np.arange(-INF, INF + 1) / k
    lo = np.floor(m).astype(int)
    hi = np.ceil(m).astype(int)

    def grab(idx):
        v = np.zeros(len(idx))
        ok = (idx >= -INF) & (idx <= INF)
        v[ok] = x[idx[ok] + INF]
        return v

    x_lo, x_hi = grab(lo), grab(hi)
    return np.where(lo == hi, x_lo, (x_lo + x_hi) / 2)   # exact sample vs average


def transform(x: np.ndarray, alpha: float, beta: float) -> np.ndarray:
    """
    GENERAL transform  y[n] = x[alpha*n + beta]  on n = -8..8.
    One function for shift + reversal + scaling (integer args only).
    PULL method with zero-fill.
    """
    n_out = np.arange(-INF, INF + 1)
    arg = alpha * n_out + beta
    out = np.zeros_like(x, dtype=float)
    is_int = (arg == np.round(arg))
    ai = np.round(arg).astype(int)
    ok = is_int & (ai >= -INF) & (ai <= INF)
    out[ok] = x[ai[ok] + INF]
    return out


# ======================================================================
#  SECTION B -- EVEN / ODD DECOMPOSITION
# ======================================================================

def even_odd_decomposition(x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns (x_even, x_odd).   MUST call time_reverse_signal inside.
      xe[n] = 0.5*(x[n] + x[-n])
      xo[n] = 0.5*(x[n] - x[-n])           <-- NO extra /2 !
    NOTE: check the required RETURN ORDER in the question
          (some ask for (odd, even) first).
    """
    xr = time_reverse_signal(x)
    x_even = 0.5 * (x + xr)
    x_odd = 0.5 * (x - xr)
    return x_even, x_odd


# ======================================================================
#  SECTION C -- ENERGY & POWER
# ======================================================================

def energy(x: np.ndarray) -> float:
    """E = sum |x[n]|^2   (np.abs handles complex too)."""
    return float(np.sum(np.abs(x) ** 2))


def average_power(x: np.ndarray) -> float:
    """P = energy / number of samples."""
    return float(np.sum(np.abs(x) ** 2) / len(x))


# ======================================================================
#  SECTION D -- SINUSOIDS : TIME SHIFT vs PHASE SHIFT
# ======================================================================

def sinusoid(n: np.ndarray, A: float, W0: float, phi: float) -> np.ndarray:
    """x[n] = A cos(W0 n + phi)."""
    return A * np.cos(W0 * n + phi)


def time_shift_sinusoid(n, A, W0, phi, n0) -> np.ndarray:
    """x[n - n0]  (substitute n -> n - n0)."""
    return A * np.cos(W0 * (n - n0) + phi)


def phase_change_sinusoid(n, A, W0, phi, phi0) -> np.ndarray:
    """Change phase by phi0. State sign convention; be consistent."""
    return A * np.cos(W0 * n + phi - phi0)


def mse(a: np.ndarray, b: np.ndarray) -> float:
    """Mean squared error -- used to compare shifted vs phase-changed."""
    return float(np.mean((a - b) ** 2))

# KEY FACT: a time shift by n0 == a phase change of phi0 = W0*n0  (MSE ~ 0).
# The reverse is only EXACT when phi0 = W0 * integer; otherwise the best
# integer shift is an approximation (small nonzero MSE).


# ======================================================================
#  SECTION E -- SYSTEM PROPERTY TESTS  (Linear / Time-Invariant / Causal)
# ======================================================================

def is_linear(system, x1, x2, a, b) -> bool:
    """T{a*x1 + b*x2} == a*T{x1} + b*T{x2} ?  (test complex a,b if needed)."""
    lhs = system(a * x1 + b * x2)
    rhs = a * system(x1) + b * system(x2)
    return np.allclose(lhs, rhs)
    # Quick nonlinearity check: if system(zeros) != 0  -> NOT linear.


def _delay(x, k):
    """Zero-padded (non-circular) delay, helper for the TI test."""
    if k > 0:
        return np.concatenate((np.zeros(k), x[:-k]))
    if k < 0:
        return np.concatenate((x[-k:], np.zeros(-k)))
    return x.copy()


def is_time_invariant(system, x, k) -> bool:
    """system(delay(x,k)) == delay(system(x),k) ?"""
    return np.allclose(system(_delay(x, k)), _delay(system(x), k))
    # Suspect a bare n or t OUTSIDE x's argument (e.g. n*x[n]) -> time-varying.


def is_causal(system, x, n_trials=8, seed=0) -> bool:
    """Perturb only FUTURE samples; past/present output must not change."""
    rng = np.random.default_rng(seed)
    N = len(x)
    y0 = system(x)
    for _ in range(n_trials):
        n0 = rng.integers(0, N - 1)
        xp = x.copy()
        xp[n0 + 1:] += rng.normal(scale=10, size=N - n0 - 1)
        if not np.allclose(y0[:n0 + 1], system(xp)[:n0 + 1]):
            return False
    return True
    # Analytical shortcut: any x[n+k] with k>0 (future) -> non-causal.


# Example systems to classify (write as system(x) and run the three tests):
#   y[n] = x[n] - x[n-1]              -> linear, time-invariant, causal
#   y[n] = n * x[n]                   -> linear, TIME-VARYING, causal
#   y[n] = x[n]**2                    -> NONLINEAR, time-invariant, causal
#   y[n] = x[n] + 5                   -> NONLINEAR (T{0}!=0), TI, causal
#   y[n] = (x[n-1]+x[n]+x[n+1])/3     -> linear, TI, NON-CAUSAL (needs x[n+1])
#   y[n] = x[-n]                      -> linear, TIME-VARYING, NON-CAUSAL


# ======================================================================
#  MAIN -- adapt to whatever the online actually asks
# ======================================================================
def main():
    # --- build the example signal (edit to match the question) ---
    x = init_signal()
    x[INF + 0] = 1
    x[INF + 1] = 0.5
    x[INF - 1] = 2
    x[INF + 2] = 1
    x[INF - 2] = 0.5

    # --- Section A demos ---
    plot(x, title="Original x[n]")
    plot(time_shift_signal(x, 2),      title="x[n-2]")
    plot(time_reverse_signal(x),       title="x[-n]")
    plot(time_scale_compress(x, 2),    title="x[2n]")
    plot(time_scale_expand_zeros(x, 3),  title="x[n/3] (zeros)")
    plot(time_scale_expand_interp(x, 3), title="x[n/3] (interp)")
    plot(transform(x, alpha=-2, beta=1), title="x[-2n+1]")

    # --- Section B: even / odd ---
    xe, xo = even_odd_decomposition(x)
    plot(xe, title="Even part xe[n]")
    plot(xo, title="Odd part xo[n]")
    # verification (worth marks):
    print("even ok :", np.allclose(xe, xe[::-1]))
    print("odd  ok :", np.allclose(xo, -xo[::-1]))
    print("recon ok:", np.allclose(xe + xo, x))

    # --- Section C: energy / power ---
    print("energy  :", energy(x))
    print("avg pow :", average_power(x))

    # --- Section D: sinusoid shift vs phase ---
    n = np.arange(-20, 21)
    A, W0, phi = 1.0, np.pi / 4, 0.0
    xs = sinusoid(n, A, W0, phi)
    xt = time_shift_sinusoid(n, A, W0, phi, n0=1)
    xp = phase_change_sinusoid(n, A, W0, phi, phi0=W0 * 1)   # equivalent phase
    print("shift==phase MSE:", mse(xt, xp))   # ~0

    # --- Section E: classify a system (example) ---
    diff_sys = lambda s: np.diff(s, prepend=0)     # y[n]=x[n]-x[n-1]
    print("diff linear:", is_linear(diff_sys, x, x[::-1], 2.0, -1.5))
    print("diff TI    :", is_time_invariant(diff_sys, x, 3))
    print("diff causal:", is_causal(diff_sys, x))


if __name__ == "__main__":
    main()