import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# METHOD A: Standard Linear Interpolation (Best for general use)
# -------------------------------------------------------------
def transform_continuous_linear(t_orig, x_orig, alpha, beta, t_out):
    """
    Computes y(t) = x(alpha * t + beta) using linear interpolation.
    Fills out-of-bounds regions with 0.
    """
    # Backward mapping: find where the output grid maps to on the original grid
    t_query = alpha * t_out + beta
    
    # Linear interpolation
    y = np.interp(t_query, t_orig, x_orig, left=0, right=0)
    return y

# -------------------------------------------------------------
# METHOD B: Neighbor-Average Interpolation (Strictly for your Lab Sheet)
# -------------------------------------------------------------
def transform_continuous_average(t_orig, x_orig, alpha, beta, t_out):
    """
    Computes y(t) = x(alpha * t + beta) using neighbor-averaging[cite: 12, 16].
    """
    t_query = alpha * t_out + beta
    dt = t_orig[1] - t_orig[0]
    
    # Find exact fractional index addresses
    float_indices = (t_query - t_orig[0]) / dt
    
    # Extract left and right integer neighbor slots
    left = np.floor(float_indices).astype(int)
    right = np.ceil(float_indices).astype(int)
    
    # Clip indices to prevent array out-of-bounds crashes
    max_idx = len(x_orig) - 1
    left = np.clip(left, 0, max_idx)
    right = np.clip(right, 0, max_idx)
    
    # Calculate the average of the two closest samples 
    y = 0.5 * (x_orig[left] + x_orig[right])
    return y

def transform_discrete_generic(n_samp, x_samp, alpha, beta, n_out):
    """
    Computes y[n] = x[alpha * n + beta] for discrete signals.
    Handles non-contiguous timelines and forces missing samples to 0.
    """
    # 1. Map backward to find the original target address framework
    arg = alpha * n_out + beta     
    out = np.zeros(n_out.shape)
    
    # 2. Separate values into exact integers vs fractional addresses
    is_int = (arg == np.round(arg))  
    ai = np.round(arg).astype(int)
    
    # 3. Perform a binary search to find the index locations
    pos = np.searchsorted(n_samp, ai) 
    pos = np.clip(pos, 0, len(n_samp) - 1) 
    
    # 4. Double check that the index actually matches our target integer
    valid = is_int & (n_samp[pos] == ai) 
    
    # 5. Populate matches into output array; the rest remain 0
    out[valid] = x_samp[pos[valid]]  
    return out

def time_shift_signal(x, k):
    if k > 0:      # delay: zeros in from the left, tail drops off
        return np.concatenate((np.zeros(k,dtype=x.dtype), x[:-k]))
    elif k < 0:    # advance
        return np.concatenate((x[-k:], np.zeros(-k,dtype=x.dtype)))
    return x.copy()