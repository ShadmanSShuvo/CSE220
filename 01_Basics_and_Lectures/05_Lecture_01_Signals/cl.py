"""
CSE 219 - Signals and Linear Systems
Template: shifting, scaling, reversal, energy/power, even-odd decomposition.

Fill in / tweak the `x_func` definition and the transformation params,
then run each section. Uses only numpy + matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# numpy >=2.0 renamed trapz -> trapezoid
_trapz = getattr(np, "trapezoid", None) or np.trapz


# ----------------------------------------------------------------------
# 1. Define the base continuous-time signal x(t)
#    (approximated on a dense time grid — this is how we "simulate"
#     continuous signals numerically)
# ----------------------------------------------------------------------

def x_func(t):
    """
    Example from the slides:
        x(t) = t + 1,  -1 <= t <= 1
             = 0,       otherwise
    Swap this out for any piecewise / sinusoidal / etc. signal.
    """
    return np.where((t >= -1) & (t <= 1), t + 1, 0.0)


t = np.linspace(-6, 6, 4000)   # dense grid ~ continuous time
x = x_func(t)


def plot_signal(t, x, title, ax=None):
    own_fig = ax is None
    if own_fig:
        fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(t, x, lw=2)
    ax.axhline(0, color='k', lw=0.5)
    ax.axvline(0, color='k', lw=0.5)
    ax.set_title(title)
    ax.set_xlabel("t")
    ax.set_ylabel("x(t)")
    ax.grid(alpha=0.3)
    if own_fig:
        plt.tight_layout()
        plt.show()


# ----------------------------------------------------------------------
# 2. General transformation: y(t) = x(alpha * t + beta)
#    Recipe from the slides:
#       Step 1: shift  -> x(t + beta)
#       Step 2: reverse (only if alpha < 0)
#       Step 3: scale by |alpha|
# ----------------------------------------------------------------------

def transform_signal(x_func, t, alpha, beta):
    """
    Returns y(t) = x(alpha * t + beta), evaluated directly
    (equivalent to doing shift -> reverse -> scale, but computed
    in one line since we have x_func in closed form).
    """
    return x_func(alpha * t + beta)


def transform_demo():
    fig, axes = plt.subplots(1, 4, figsize=(18, 3.2))

    plot_signal(t, x_func(t), "Original: x(t)", axes[0])
    plot_signal(t, transform_signal(x_func, t, 1, 3), "Shift left by 3: x(t+3)", axes[1])
    plot_signal(t, transform_signal(x_func, t, 2, 0), "Compress by 2: x(2t)", axes[2])
    plot_signal(t, transform_signal(x_func, t, -3, 2), "x(-3t + 2)  [reverse+shift+compress]", axes[3])

    plt.tight_layout()
    plt.savefig("transform_demo.png", dpi=150)
    plt.show()


# ----------------------------------------------------------------------
# 3. Step-by-step visualization of the 3-step recipe
#    e.g. reproduce slide example: x(-3t + 2)
# ----------------------------------------------------------------------

def step_by_step_demo(alpha=-3, beta=2):
    g1 = x_func(t + beta)                      # Step 1: shift
    g2 = g1 if alpha > 0 else x_func(-t + beta) # Step 2: reverse if alpha<0
    g3 = transform_signal(x_func, t, alpha, beta)  # Step 3: scale (final)

    fig, axes = plt.subplots(1, 4, figsize=(18, 3.2))
    plot_signal(t, x_func(t), "x(t)", axes[0])
    plot_signal(t, g1, f"Step 1: x(t + {beta})", axes[1])
    plot_signal(t, g2, f"Step 2: reverse if α<0", axes[2])
    plot_signal(t, g3, f"Step 3: x({alpha}t + {beta})", axes[3])
    plt.tight_layout()
    plt.savefig("step_by_step_demo.png", dpi=150)
    plt.show()


# ----------------------------------------------------------------------
# 4. Energy and Power (continuous, numerically via trapezoidal rule)
# ----------------------------------------------------------------------

def energy_continuous(x_func, t1, t2, n=10000):
    tt = np.linspace(t1, t2, n)
    xx = x_func(tt)
    return _trapz(np.abs(xx) ** 2, tt)


def power_continuous(x_func, t1, t2, n=10000):
    E = energy_continuous(x_func, t1, t2, n)
    return E / (t2 - t1)


# Discrete version
def energy_discrete(x_n):
    x_n = np.asarray(x_n)
    return np.sum(np.abs(x_n) ** 2)


def power_discrete(x_n):
    x_n = np.asarray(x_n)
    return energy_discrete(x_n) / len(x_n)


def energy_power_demo():
    # Continuous example from slides: half-sine, energy = pi/2, power = 1/2
    half_sine = lambda tt: np.where((tt >= 0) & (tt <= np.pi), np.sin(tt), 0.0)
    E = energy_continuous(half_sine, 0, np.pi)
    P = power_continuous(half_sine, 0, np.pi)
    print(f"Half-sine energy  ≈ {E:.4f}  (expected π/2 ≈ {np.pi/2:.4f})")
    print(f"Half-sine power   ≈ {P:.4f}  (expected 1/2 = 0.5)")

    # Discrete example from slides: x = [1, -2, 2, -1]
    x_n = [1, -2, 2, -1]
    print(f"Discrete energy = {energy_discrete(x_n)}  (expected 10)")
    print(f"Discrete power  = {power_discrete(x_n)}  (expected 2.5)")


# ----------------------------------------------------------------------
# 5. Even / Odd decomposition
#    xe(t) = 1/2 [x(t) + x(-t)]
#    xo(t) = 1/2 [x(t) - x(-t)]
# ----------------------------------------------------------------------

def even_odd_decompose(x_func, t):
    x_pos = x_func(t)
    x_neg = x_func(-t)
    xe = 0.5 * (x_pos + x_neg)
    xo = 0.5 * (x_pos - x_neg)
    return xe, xo


def even_odd_demo():
    xe, xo = even_odd_decompose(x_func, t)

    fig, axes = plt.subplots(1, 3, figsize=(14, 3.2))
    plot_signal(t, x_func(t), "Original x(t)", axes[0])
    plot_signal(t, xe, "Even part: xe(t)", axes[1])
    plot_signal(t, xo, "Odd part: xo(t)", axes[2])
    plt.tight_layout()
    plt.savefig("even_odd_demo.png", dpi=150)
    plt.show()

    # sanity checks
    recon = xe + xo
    print("Max |x - (xe+xo)| =", np.max(np.abs(x_func(t) - recon)))          # should be ~0
    print("Max |xe(t) - xe(-t)| =", np.max(np.abs(xe - even_odd_decompose(x_func, -t)[0])))  # even check


# ----------------------------------------------------------------------
# 6. Discrete-time signal shifting (for x[n])
# ----------------------------------------------------------------------

def discrete_shift_demo():
    n = np.arange(-5, 11)
    xn = np.where((n >= 0) & (n <= 3), [1, -2, 2, -1][:4] if False else 0, 0)
    # build a simple discrete signal manually
    xn = np.zeros_like(n, dtype=float)
    vals = {0: 1, 1: -2, 2: 2, 3: -1}
    for k, v in vals.items():
        xn[n == k] = v

    shift = 4
    n_shifted = n  # index axis stays the same, but we relabel which n maps to which sample
    xn_shifted = np.zeros_like(n, dtype=float)
    for k, v in vals.items():
        xn_shifted[n == k + shift] = v   # x[n - shift]

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.2))
    axes[0].stem(n, xn)
    axes[0].set_title("x[n]")
    axes[0].grid(alpha=0.3)
    axes[1].stem(n, xn_shifted)
    axes[1].set_title(f"x[n - {shift}]  (delayed)")
    axes[1].grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("discrete_shift_demo.png", dpi=150)
    plt.show()


# ----------------------------------------------------------------------
# Run everything
# ----------------------------------------------------------------------

if __name__ == "__main__":
    transform_demo()
    step_by_step_demo(alpha=-3, beta=2)
    energy_power_demo()
    even_odd_demo()
    discrete_shift_demo()