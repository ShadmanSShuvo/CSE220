import numpy as np
import matplotlib.pyplot as plt

# Define Discrete Signal Axis and Input Test Signal
# n ranges from -8 to 8 (length 17)
n_axis = np.arange(-8, 9)

# Original signal from the exam template
# x[-2]=0.5, x[-1]=2, x[0]=1, x[1]=0.5, x[2]=1, and others are 0
x_test = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 2.0, 1.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

# =====================================================================
# QUESTION SET 1: Time Shift and Time Scaling
# =====================================================================

def time_shift_signal(x, k):
    """
    Returns the shifted signal x[n - k] as a NumPy array of length 17.
    k is an integer in [-8, 8]. Positive k delays; negative k advances.
    Vacated positions are filled with 0.
    """
    n = np.arange(-8, 9)
    n_in = n - k
    # Keep only indices that fall within the valid window [-8, 8]
    mask = (n_in >= -8) & (n_in <= 8)
    
    out = np.zeros_like(x)
    # Map valid n_in back to 0-based array index by adding 8
    out[mask] = x[n_in[mask] + 8]
    return out

def time_scale_signal(x, k):
    """
    Returns the compressed signal x[k * n] for positive integer k.
    """
    n = np.arange(-8, 9)
    n_in = k * n
    # Keep only indices that fall within the valid window [-8, 8]
    mask = (n_in >= -8) & (n_in <= 8)
    
    out = np.zeros_like(x)
    out[mask] = x[n_in[mask] + 8]
    return out

# =====================================================================
# QUESTION SET 2: Time Reversal and Even-Odd Decomposition
# =====================================================================

def time_reverse_signal(x):
    """
    Returns the time-reversed signal x[-n].
    
    Note on Array Reversal:
    Since the index axis is symmetric about 0 (n = -8...8), reversing the array 
    using x[::-1] correctly maps index i (corresponding to n = i - 8) to 
    index 16 - i (corresponding to -n = 8 - i). 
    If the axis were asymmetric (e.g., n = -5...8), simple reversal would shift 
    the origin. For instance, n=0 (originally at index 5) would map to index 11 
    (which is n=3), resulting in an incorrect time shift along with the reversal.
    """
    return x[::-1]

def odd_even_decomposition(x):
    """
    Returns the odd component xo[n] and even component xe[n] of signal x.
    Calls time_reverse_signal internally.
    """
    xr = time_reverse_signal(x)
    xe = 0.5 * (x + xr)
    xo = 0.5 * (x - xr)
    return xo, xe

# =====================================================================
# QUESTION SET 3: Time Scaling with Interpolation
# =====================================================================

def time_scale_upscale(x, k):
    """
    Returns the up-scaled signal x[n/k] for positive integer k.
    Where n/k is an integer, copies the corresponding sample; otherwise 0.
    """
    n = np.arange(-8, 9)
    divisible_mask = (n % k == 0)
    n_in = n // k
    valid_mask = divisible_mask & (n_in >= -8) & (n_in <= 8)
    
    out = np.zeros_like(x)
    out[valid_mask] = x[n_in[valid_mask] + 8]
    return out

def safe_lookup(x, idx):
    """
    Safely retrieves elements from x corresponding to indices in the 'idx' array.
    If an index falls outside [-8, 8], a value of 0 is returned.
    """
    mask = (idx >= -8) & (idx <= 8)
    out = np.zeros_like(idx, dtype=float)
    out[mask] = x[idx[mask] + 8]
    return out

def time_scale_signal_interpolate(x, k):
    """
    Returns the up-scaled signal x[n/k] for positive integer k.
    Non-integer samples take the average of floor(n/k) and ceil(n/k).
    """
    n = np.arange(-8, 9)
    r = n / k
    r_floor = np.floor(r).astype(int)
    r_ceil = np.ceil(r).astype(int)
    
    val_floor = safe_lookup(x, r_floor)
    val_ceil = safe_lookup(x, r_ceil)
    
    return 0.5 * (val_floor + val_ceil)

# =====================================================================
# QUESTION SET 4: Combined Transformation x[alpha * n + beta]
# =====================================================================

def transform(x, alpha, beta):
    """
    Returns y[n] = x[alpha * n + beta] evaluated on n = -8...8.
    """
    n = np.arange(-8, 9)
    n_in = alpha * n + beta
    mask = (n_in >= -8) & (n_in <= 8)
    
    out = np.zeros_like(x)
    out[mask] = x[n_in[mask] + 8]
    return out


# =====================================================================
# VERIFICATION AND PLOTTING RUNNER
# =====================================================================

if __name__ == "__main__":
    print("--- QUESTION SET 1 VERIFICATION ---")
    # x[n-0] is original
    assert np.allclose(time_shift_signal(x_test, 0), x_test)
    print("Verification 1 (x[n-0] == x[n]): Passed")
    
    # Shifting right then left restores original (within limits)
    k_shift = 2
    r_shift = time_shift_signal(x_test, k_shift)
    l_shift = time_shift_signal(r_shift, -k_shift)
    assert np.allclose(l_shift, x_test)  # Edge values of x_test are already 0
    print("Verification 2 (Shift right then left): Passed")
    
    # Confirm only even input indices survive in x[2n]
    scaled_2 = time_scale_signal(x_test, 2)
    expected_scaled = np.zeros_like(x_test)
    expected_scaled[-1 + 8] = x_test[-2 + 8] # y[-1] = x[-2]
    expected_scaled[0 + 8] = x_test[0 + 8]   # y[0] = x[0]
    expected_scaled[1 + 8] = x_test[2 + 8]   # y[1] = x[2]
    assert np.allclose(scaled_2, expected_scaled)
    print("Verification 3 (Compression x[2n] survival): Passed\n")
    
    print("--- QUESTION SET 2 VERIFICATION ---")
    xo, xe = odd_even_decomposition(x_test)
    
    # Check even symmetry: xe[-n] == xe[n]
    assert np.allclose(time_reverse_signal(xe), xe)
    print("Check 1 (xe[-n] == xe[n]): Passed")
    
    # Check odd symmetry: xo[-n] == -xo[n]
    assert np.allclose(time_reverse_signal(xo), -xo)
    print("Check 2 (xo[-n] == -xo[n]): Passed")
    
    # Check reconstruction: xe[n] + xo[n] == x[n]
    assert np.allclose(xe + xo, x_test)
    print("Check 3 (xe + xo == x): Passed\n")
    
    print("--- QUESTION SET 3 VERIFICATION ---")
    # For k=1, both functions must return original unchanged
    assert np.allclose(time_scale_upscale(x_test, 1), x_test)
    assert np.allclose(time_scale_signal_interpolate(x_test, 1), x_test)
    print("Verification 1 (k=1 upscale / interpolate identity): Passed")
    
    # Confirm interpolation behavior for k=3 at non-integer step
    interp_3 = time_scale_signal_interpolate(x_test, 3)
    # n = -1 => r = -1/3 => floor is -1, ceil is 0. 
    # Average of x_test[-1]=2.0 and x_test[0]=1.0 is 1.5
    assert np.isclose(interp_3[-1 + 8], 1.5)
    print("Verification 2 (k=3 interpolation check): Passed\n")
    
    print("--- QUESTION SET 4 VERIFICATION ---")
    # Method A: Single transform call
    y_single = transform(x_test, -2, 1)
    
    # Method B: Composition (shift by -1, reverse, scale by 2)
    s = time_shift_signal(x_test, -1)   # x[n+1]
    r = time_reverse_signal(s)         # x[-n+1]
    y_comp = time_scale_signal(r, 2)    # x[-2n+1]
    
    assert np.allclose(y_single, y_comp)
    print("Verification 1 (x[-2n+1] single vs composed): Passed")
    
    # Now verify shift-after-scale composition for x[-2(n+1)] = x[-2n-2]
    y2_single = transform(x_test, -2, -2)
    
    w2 = time_scale_signal(x_test, 2)   # x[2n]
    v2 = time_reverse_signal(w2)       # x[-2n]
    y2_comp = time_shift_signal(v2, -1) # v2[n+1] = x[-2(n+1)]
    
    assert np.allclose(y2_single, y2_comp)
    print("Verification 2 (x[-2(n+1)] single vs composed): Passed\n")

    # =====================================================================
    # PLOTTING ROUTINES
    # =====================================================================
    
    # Plot Question Set 2: Even-Odd Decomposition
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.stem(n_axis, x_test, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.title("Original Signal x[n]")
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    plt.stem(n_axis, xe, linefmt='g-', markerfmt='go', basefmt='r-')
    plt.title("Even Component xe[n]")
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    plt.stem(n_axis, xo, linefmt='m-', markerfmt='mo', basefmt='r-')
    plt.title("Odd Component xo[n]")
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    plt.stem(n_axis, xe + xo, linefmt='c-', markerfmt='co', basefmt='r-')
    plt.title("Reconstructed xe[n] + xo[n]")
    plt.grid(True)
    
    plt.tight_layout()
    plt.suptitle("Question Set 2 — Decomposition Plots", y=1.02, fontsize=14)
    plt.show()

    # Plot Question Set 4: Combined Transformations
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.stem(n_axis, x_test, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.title("Original Signal x[n]")
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    plt.stem(n_axis, y_single, linefmt='g-', markerfmt='go', basefmt='r-')
    plt.title("Transform x[-2n + 1]")
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    plt.stem(n_axis, y2_single, linefmt='m-', markerfmt='mo', basefmt='r-')
    plt.title("Transform x[-2(n + 1)]")
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    plt.stem(n_axis, y_comp, linefmt='c-', markerfmt='co', basefmt='r-')
    plt.title("Composed x[-2n + 1] (Shift->Rev->Scale)")
    plt.grid(True)
    
    plt.tight_layout()
    plt.suptitle("Question Set 4 — Transformation Plots", y=1.02, fontsize=14)
    plt.show()