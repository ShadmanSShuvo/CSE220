import numpy as np

INF = 8

def time_reverse_signal(x):
    """
    y[n] = x[-n].
    Because the stored axis n = -8..8 is symmetric about 0, index n maps to
    array position n+8, and index -n maps to position -n+8 = 16-(n+8).
    So reversing the array (x[::-1]) exactly swaps position (n+8) with
    (16-(n+8)), which is precisely the x[-n] mapping.
    If the axis were asymmetric (e.g. n = -3..10), position i no longer
    corresponds to a symmetric partner (16-i) inside the array bounds, so a
    plain x[::-1] would NOT correctly compute x[-n]; you'd need to re-index
    using the actual offset and re-pad/truncate accordingly.
    """
    x = np.asarray(x, dtype=float)
    return x[::-1]

def odd_even_decomposition(x):
    """Return (odd, even) components."""
    x = np.asarray(x, dtype=float)
    x_rev = time_reverse_signal(x)
    even = 0.5 * (x + x_rev)
    odd = 0.5 * (x - x_rev)
    return odd, even


if __name__ == "__main__":
    x = np.array([0,0,0,0,0,0,0.5,2,1,0.5,1,0,0,0,0,0,0])

    odd, even = odd_even_decomposition(x)
    print("x    :", x)
    print("even :", even)
    print("odd  :", odd)

    # Check 1: even part is truly even -> even[::-1] == even
    assert np.allclose(even[::-1], even), "even part failed symmetry check"

    # Check 2: odd part is truly odd -> odd[::-1] == -odd
    assert np.allclose(odd[::-1], -odd), "odd part failed antisymmetry check"

    # Check 3: reconstruction
    assert np.allclose(even + odd, x), "reconstruction failed"

    print("All Set 2 checks passed.")