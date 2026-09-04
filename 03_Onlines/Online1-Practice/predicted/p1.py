import numpy as np

def time_shift_signal(x: np.ndarray, k: int) -> np.ndarray:
    """
    Returns x[n - k] for n = -8...8.
    Vacated positions are filled with 0. No loops, no np.roll.
    """
    n = np.arange(-8, 9)
    # The source index we need to pull from for each destination index `n`
    src_indices = n - k
    
    # Create a mask for indices that fall within the valid input range [-8, 8]
    valid_mask = (src_indices >= -8) & (src_indices <= 8)
    
    # Map the valid source indices from [-8, 8] to array indices [0, 16]
    # np.where handles the boundary fill beautifully
    return np.where(valid_mask, x[src_indices + 8], 0.0)


def time_scale_signal(x: np.ndarray, k: int) -> np.ndarray:
    """
    Returns x[kn] for a positive integer k, where n = -8...8.
    Out-of-bound indices are filled with 0. No loops.
    """
    n = np.arange(-8, 9)
    # The source index we need to pull from is k * n
    src_indices = k * n
    
    # Create a mask for scaled indices that fit within the [-8, 8] window
    valid_mask = (src_indices >= -8) & (src_indices <= 8)
    
    # Map valid scaled indices to array indices [0, 16]
    return np.where(valid_mask, x[src_indices + 8], 0.0)