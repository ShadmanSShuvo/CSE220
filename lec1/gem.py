import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 1. Base Signals Definition
# =====================================================================

def piecewise_continuous_signal(t):
    """
    Implements the continuous piecewise signal from Slide 32:
    x(t) = 1      for 0 <= t < 1
    x(t) = 2 - t  for 1 <= t <= 2
    x(t) = 0      otherwise
    """
    conditions = [
        (t >= 0) & (t < 1),
        (t >= 1) & (t <= 2)
    ]
    functions = [
        lambda t: np.ones_like(t),
        lambda t: 2 - t
    ]
    return np.select(conditions, [f(t) for f in functions], default=0)


def discrete_unit_step(n):
    """
    Implements the discrete-time unit step signal from Slide 49:
    x[n] = 1 for n >= 0
    x[n] = 0 for n < 0
    """
    return np.where(n >= 0, 1.0, 0.0)


# =====================================================================
# 2. Even & Odd Decomposition Functions
# =====================================================================

def decompose_continuous_even_odd(signal_func, t):
    """
    Extracts the even and odd components of a continuous signal function
    using formulas from Slide 43:
    x_e(t) = 0.5 * (x(t) + x(-t))
    x_o(t) = 0.5 * (x(t) - x(-t))
    """
    x_t = signal_func(t)
    x_neg_t = signal_func(-t)
    
    even_part = 0.5 * (x_t + x_neg_t)
    odd_part = 0.5 * (x_t - x_neg_t)
    return even_part, odd_part


def decompose_discrete_even_odd(n, x_n):
    """
    Extracts the even and odd components of a discrete time signal vector.
    Assumes n is symmetric around 0 (e.g., from -N to N).
    """
    # Flip the signal array cleanly relative to time array alignment
    x_neg_n = np.flip(x_n)
    
    even_part = 0.5 * (x_n + x_neg_n)
    odd_part = 0.5 * (x_n - x_neg_n)
    return even_part, odd_part


# =====================================================================
# 3. Execution & Visualization
# =====================================================================

if __name__ == "__main__":
    # Setup plotting aesthetics
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    # -----------------------------------------------------------------
    # Visualizing Transformation: x(-3t + 2) [Slides 31-35]
    # -----------------------------------------------------------------
    t = np.linspace(-3, 3, 1000)
    
    # Recipe: Apply shift first, then scale/reversal (alpha=-3, beta=2)
    x_original = piecewise_continuous_signal(t)
    x_transformed = piecewise_continuous_signal(-3 * t + 2)
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(t, x_original, 'g-', lw=2.5, label='$x(t)$')
    plt.title('Original Piecewise Signal')
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(t, x_transformed, 'b-', lw=2.5, label='$x(-3t + 2)$')
    plt.title('Transformed Signal: Shifted, Flipped, & Compressed')
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

    # -----------------------------------------------------------------
    # Decomposition: Continuous Non-Symmetric Signal [Slides 45-48]
    # -----------------------------------------------------------------
    # A test function that is neither even nor odd: x(t) = t + 1 for -1<=t<=1
    def ramp_signal(t_val):
        return np.where((t_val >= -1) & (t_val <= 1), t_val + 1, 0.0)
    
    t_dense = np.linspace(-2, 2, 1000)
    x_ramp = ramp_signal(t_dense)
    even_c, odd_c = decompose_continuous_even_odd(ramp_signal, t_dense)
    
    plt.figure(figsize=(15, 4))
    
    plt.subplot(1, 3, 1)
    plt.plot(t_dense, x_ramp, 'k-', lw=2, label='$x(t) = t+1$')
    plt.title('Original Signal')
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.legend()
    
    plt.subplot(1, 3, 2)
    plt.plot(t_dense, even_c, 'g-', lw=2, label='$x_e(t)$ (Even Part)')
    plt.title('Extracted Even Component (Should be 1)')
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.legend()
    
    plt.subplot(1, 3, 3)
    plt.plot(t_dense, odd_c, 'r-', lw=2, label='$x_o(t)$ (Odd Part)')
    plt.title('Extracted Odd Component (Should be $t$)')
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

    # -----------------------------------------------------------------
    # Decomposition: Discrete Time Unit Step Signal [Slides 49-52]
    # -----------------------------------------------------------------
    # Must use a symmetric integer range around zero for vector flipping math
    n = np.arange(-5, 6) 
    x_n = discrete_unit_step(n)
    even_d, odd_d = decompose_discrete_even_odd(n, x_n)
    
    plt.figure(figsize=(15, 4))
    
    plt.subplot(1, 3, 1)
    plt.stem(n, x_n, linefmt='b-', markerfmt='bo', basefmt='k-')
    plt.title('Discrete Signal $x[n]$ (Unit Step)')
    plt.xlabel('n')
    
    plt.subplot(1, 3, 2)
    plt.stem(n, even_d, linefmt='g-', markerfmt='go', basefmt='k-')
    plt.title('Even Component $x_e[n]$')
    plt.xlabel('n')
    
    plt.subplot(1, 3, 3)
    plt.stem(n, odd_d, linefmt='r-', markerfmt='ro', basefmt='k-')
    plt.title('Odd Component $x_o[n]$')
    plt.xlabel('n')
    
    plt.tight_layout()
    plt.show()