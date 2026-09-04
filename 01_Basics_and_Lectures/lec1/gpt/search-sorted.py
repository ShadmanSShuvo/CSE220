"""
Examples of np.searchsorted, and how it replaces the manual
for-loop search in the interpolation code with a fast vectorized lookup.

np.searchsorted(a, v, side='left'/'right') returns the index where
v should be inserted into sorted array `a` to keep it sorted.
"""

import numpy as np


# ----------------------------------------------------------------------
# 1. Basic usage
# ----------------------------------------------------------------------
a = np.array([0, 1, 2, 3, 4, 5])

print("Array a:", a)

print(np.searchsorted(a, 2.5))
# -> 3   (2.5 would be inserted at index 3 to keep a sorted: 0,1,2,[2.5],3,4,5)

print(np.searchsorted(a, 2))
# -> 2   (default side='left': inserts BEFORE existing equal entries)

print(np.searchsorted(a, 2, side='right'))
# -> 3   (side='right': inserts AFTER existing equal entries)

print(np.searchsorted(a, -1))
# -> 0   (before everything)

print(np.searchsorted(a, 10))
# -> 6   (after everything, i.e. len(a))


# ----------------------------------------------------------------------
# 2. Vectorized: query many points at once
# ----------------------------------------------------------------------
queries = np.array([-1, 0, 0.5, 2, 2.9, 5, 7])
idx = np.searchsorted(a, queries)
print("\nQueries:", queries)
print("Insert indices:", idx)


# ----------------------------------------------------------------------
# 3. Practical use: bucket / bin lookup
#    e.g. "which interval does t fall into?"
# ----------------------------------------------------------------------
bins = np.array([0, 10, 20, 30, 40])   # bin edges
values = np.array([5, 15, 25, 35, -3, 45])

bin_idx = np.searchsorted(bins, values, side='right') - 1
print("\nValues:", values)
print("Bin index each value falls into:", bin_idx)
# e.g. 5 falls in bin [0,10) -> index 0
#      15 falls in bin [10,20) -> index 1


# ----------------------------------------------------------------------
# 4. Using searchsorted to VECTORIZE linear interpolation
#    (replacing the manual for-loop from before)
# ----------------------------------------------------------------------
n = np.array([0, 1, 2, 3, 4, 5])
xn = np.array([1, -2, 2, -1, 3, 0], dtype=float)


def linear_interp_searchsorted(t_query, n_samples, x_samples):
    """
    Vectorized linear interpolation using searchsorted instead of
    a Python for-loop over every query point.
    """
    t_query = np.atleast_1d(t_query).astype(float)

    # For each t, find index of the right-hand sample bracketing it.
    # side='right' then subtract 1 gives the left index i such that
    # n_samples[i] <= t < n_samples[i+1]
    i = np.searchsorted(n_samples, t_query, side='right') - 1

    # Clamp indices to valid range [0, len-2] so i+1 is always valid
    i = np.clip(i, 0, len(n_samples) - 2)

    x0 = n_samples[i]
    x1 = n_samples[i + 1]
    y0 = x_samples[i]
    y1 = x_samples[i + 1]

    frac = (t_query - x0) / (x1 - x0)
    y = y0 + frac * (y1 - y0)

    # Handle exact edge cases (t below first or above last sample)
    y = np.where(t_query <= n_samples[0], x_samples[0], y)
    y = np.where(t_query >= n_samples[-1], x_samples[-1], y)

    return y


t_dense = np.linspace(0, 5, 11)
y_fast = linear_interp_searchsorted(t_dense, n, xn)
y_ref = np.interp(t_dense, n, xn)   # cross-check against numpy's built-in

print("\nt_dense:  ", t_dense)
print("Manual (searchsorted):", y_fast)
print("np.interp reference:  ", y_ref)
print("Match:", np.allclose(y_fast, y_ref))


# ----------------------------------------------------------------------
# 5. Another common use: nearest-neighbor lookup with searchsorted
# ----------------------------------------------------------------------
def nearest_interp_searchsorted(t_query, n_samples, x_samples):
    t_query = np.atleast_1d(t_query).astype(float)
    i = np.searchsorted(n_samples, t_query)
    i = np.clip(i, 1, len(n_samples) - 1)

    left = n_samples[i - 1]
    right = n_samples[i]

    # choose whichever neighbor is closer
    choose_left = (t_query - left) < (right - t_query)
    idx = np.where(choose_left, i - 1, i)
    return x_samples[idx]


y_nearest = nearest_interp_searchsorted(t_dense, n, xn)
print("\nNearest-neighbor (searchsorted):", y_nearest)