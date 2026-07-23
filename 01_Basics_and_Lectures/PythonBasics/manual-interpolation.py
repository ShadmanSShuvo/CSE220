import numpy as np

def manual_interp(t_query, tp, fp, left=None, right=None):
    """
    Manual linear interpolation — replicates np.interp(t_query, tp, fp, left, right).
    tp must be sorted ascending.

    For each query point:
      1. find the two known samples that bracket it (left index i, right index i+1)
      2. compute how far along the gap the query sits:  w = (q - tp[i]) / (tp[i+1] - tp[i])
      3. blend:  value = fp[i] + w * (fp[i+1] - fp[i])
    Out-of-range queries get `left` / `right` (default: clamp to edge values).
    """
    q = np.asarray(t_query, dtype=float)

    # defaults match np.interp: clamp to the endpoint values
    left_val  = fp[0]  if left  is None else left
    right_val = fp[-1] if right is None else right

    # for each query, find the index of the sample just to its LEFT
    # searchsorted with side='right' gives insertion point; -1 gives the left bracket
    i = np.searchsorted(tp, q, side='right') - 1

    # clip i so i and i+1 are always valid positions (we fix edges afterward)
    i = np.clip(i, 0, len(tp) - 2)

    # the two bracketing sample coordinates and values
    t_left,  t_right  = tp[i], tp[i + 1]
    f_left,  f_right  = fp[i], fp[i + 1]

    # fractional distance of the query into the [t_left, t_right] gap
    w = (q - t_left) / (t_right - t_left)

    # linear blend
    out = f_left + w * (f_right - f_left)

    # handle out-of-range queries explicitly
    out = np.where(q < tp[0],  left_val,  out)
    out = np.where(q > tp[-1], right_val, out)

    return out