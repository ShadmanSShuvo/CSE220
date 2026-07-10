import numpy as np

def sinusoid(n, A, Omega0, phi):
    """x[n] = A*cos(Omega0*n + phi)"""
    n = np.asarray(n, dtype=float)
    return A * np.cos(Omega0 * n + phi)

def time_shift_sinusoid(n, A, Omega0, phi, n0):
    """x[n - n0]"""
    n = np.asarray(n, dtype=float)
    return A * np.cos(Omega0 * (n - n0) + phi)

def phase_change_sinusoid(n, A, Omega0, phi, phi0):
    """
    x with phase changed by phi0: A*cos(Omega0*n + phi + phi0).
    Sign convention: phi0 is ADDED to the existing phase.
    Note: a RIGHT time-shift by n0 (delay) is equivalent to a phase
    change of phi0 = -Omega0*n0 (not +Omega0*n0), since
    x[n-n0] = A*cos(Omega0*n - Omega0*n0 + phi).
    """
    n = np.asarray(n, dtype=float)
    return A * np.cos(Omega0 * n + phi + phi0)


if __name__ == "__main__":
    n = np.arange(-20, 21)
    A, Omega0, phi = 1.0, 0.3, 0.2

    x = sinusoid(n, A, Omega0, phi)

    # (a) time shift by n0 == phase change by phi0 = -Omega0*n0
    n0 = 4
    x_shift = time_shift_sinusoid(n, A, Omega0, phi, n0)
    # x[n-n0] = A*cos(Omega0*n - Omega0*n0 + phi), so the equivalent phase
    # change is phi0 = -Omega0*n0 (not +Omega0*n0).
    phi0_equiv = -Omega0 * n0
    x_phase = phase_change_sinusoid(n, A, Omega0, phi, phi0_equiv)

    mse = np.mean((x_shift - x_phase) ** 2)
    print(f"n0={n0}, phi0=Omega0*n0={phi0_equiv:.4f}, MSE={mse:.3e}")
    assert mse < 1e-20, "shift <-> phase-change equivalence failed"

    # (b) given an arbitrary phase change phi0, search integer shifts n0
    # for the best match
    phi0_arbitrary = 1.0  # not necessarily a multiple of Omega0
    target = phase_change_sinusoid(n, A, Omega0, phi, phi0_arbitrary)

    best_n0 = None
    best_mse = np.inf
    for candidate in range(-20, 21):
        shifted = time_shift_sinusoid(n, A, Omega0, phi, candidate)
        m = np.mean((shifted - target) ** 2)
        if m < best_mse:
            best_mse = m
            best_n0 = candidate

    print(f"Best integer shift for phi0={phi0_arbitrary}: n0={best_n0}, "
          f"MSE={best_mse:.5f}")
    # Not exact in general: an arbitrary phase change phi0 only has an
    # EXACT discrete-time-shift equivalent when phi0 = Omega0 * (integer),
    # because only then does phi0/Omega0 land on an integer sample shift.
    # Otherwise the best integer n0 only approximately matches the phase.
    print("Note: match is generally inexact since -phi0/Omega0 = "
          f"{-phi0_arbitrary/Omega0:.3f} is not an integer.")

    print("All Set 5 checks passed.")