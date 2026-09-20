"""
Solution for Online 03 Fourier Series - Section A1, A2
Energy-Preserving Harmonic Pruning and Reconstruction Error Evaluation.
"""

import sys
import copy
from pathlib import Path
import numpy as np
import matplotlib
try:
    matplotlib.use("Agg")
except Exception:
    pass
import matplotlib.pyplot as plt

from svg_utils import load_svg_path


class FourierEpicycles:
    def __init__(self, t, signal, n_harmonics):
        """
        Parameters
        ----------
        t : 1D numpy array, shape (M,)
            Uniformly spaced sample times covering one full period [0, T].
        signal : 1D complex numpy array, shape (M,)
            signal[i] = f(t[i]) = x(t[i]) + 1j * y(t[i]).
        n_harmonics : int (N)
            Harmonics from -N to N (2N + 1 terms).
        """
        self.t = t
        self.signal = signal
        self.N = n_harmonics
        self.T = t[-1] - t[0]
        self.omega = 2 * np.pi / self.T
        self.coeffs = {}

    def calculate_cn(self, n):
        """Compute Fourier coefficient c_n via trapezoidal numerical integration."""
        exp_term = np.exp(-1j * n * self.omega * self.t)
        int_this = self.signal * exp_term
        # Use np.trapezoid (or np.trapz for older numpy)
        trap_func = getattr(np, "trapezoid", getattr(np, "trapz", None))
        return (1.0 / self.T) * trap_func(int_this, self.t)

    def calculate_all_coefficients(self):
        """Populate self.coeffs with c_n for every n in [-N, N]."""
        for n in range(-self.N, self.N + 1):
            self.coeffs[n] = self.calculate_cn(n)

    def approximate(self, t):
        """Reconstruct the signal at time(s) t from stored coefficients."""
        t_arr = np.atleast_1d(t)
        result = np.zeros(len(t_arr), dtype=complex)
        for n, cn in self.coeffs.items():
            if cn != 0:
                result += cn * np.exp(1j * n * self.omega * t_arr)
        if len(t_arr) == 1 and not isinstance(t, np.ndarray):
            return result[0]
        return result

    def prune_harmonics_by_energy(self, r):
        """
        Task 1: Energy-Preserving Harmonic Pruning.
        Retain minimal subset of most energetic harmonics such that cumulative
        energy accounts for at least fraction r of total energy.
        Discarded harmonics have their coefficients set to zero.

        Returns
        -------
        retained_count : int
            Number of retained non-zero harmonics.
        actual_energy_ratio : float
            Fraction of total energy retained.
        """
        if not (0 < r <= 1.0):
            raise ValueError("Target energy ratio r must be in (0, 1]")

        total_energy = sum(abs(cn) ** 2 for cn in self.coeffs.values())
        if total_energy == 0:
            return 0, 0.0

        # Sort harmonics by energy |c_n|^2 descending
        sorted_harmonics = sorted(self.coeffs.items(), key=lambda item: abs(item[1]) ** 2, reverse=True)

        if r >= 1.0:
            # Retain all harmonics
            retained_keys = set(self.coeffs.keys())
            cum_energy = total_energy
        else:
            target_energy = r * total_energy
            cum_energy = 0.0
            retained_keys = set()
            for n, cn in sorted_harmonics:
                retained_keys.add(n)
                cum_energy += abs(cn) ** 2
                if cum_energy >= target_energy - 1e-12:
                    break

        # Zero out discarded harmonics
        for n in list(self.coeffs.keys()):
            if n not in retained_keys:
                self.coeffs[n] = 0.0 + 0.0j

        retained_count = len(retained_keys)
        actual_energy_ratio = cum_energy / total_energy
        return retained_count, actual_energy_ratio

    def evaluate_reconstruction_error(self):
        """
        Task 2: Reconstruction Error Evaluation.
        Compute Mean Squared Error between ground truth f(t) and approximation f_hat(t).
        MSE = (1 / M) * sum(|f(t_i) - f_hat(t_i)|^2)
        """
        f_hat = self.approximate(self.t)
        mse = np.mean(np.abs(self.signal - f_hat) ** 2)
        return float(mse)


def main():
    svg_path = sys.argv[1] if len(sys.argv) > 1 else "svgs/heart.svg"
    n_harmonics = int(sys.argv[2]) if len(sys.argv) > 2 else 150

    if not Path(svg_path).exists():
        print(f"Error: {svg_path} not found.")
        sys.exit(1)

    t, signal = load_svg_path(svg_path)
    base_fe = FourierEpicycles(t, signal, n_harmonics)
    base_fe.calculate_all_coefficients()

    target_ratios = [0.96, 0.98, 0.99, 1.00]

    print(f"\nLoaded '{svg_path}' with N = {n_harmonics} (Total harmonics = {2 * n_harmonics + 1})")
    print("\nTarget Ratio | Harmonics Retained | Actual Energy Ratio | MSE")
    print("-" * 65)

    for r in target_ratios:
        # Deep copy to test pruning independently for each target ratio
        fe_pruned = copy.deepcopy(base_fe)
        retained_count, actual_ratio = fe_pruned.prune_harmonics_by_energy(r)
        mse = fe_pruned.evaluate_reconstruction_error()

        print(f"{r:12.2f} | {retained_count:18d} | {actual_ratio:19.4f} | {mse:10.4e}")

        # Task 3: Save visual comparison plot as heart_pruned_{r}.png
        f_hat = fe_pruned.approximate(t)

        fig, ax = plt.subplots(figsize=(6, 6))
        # Ground truth: invert y for SVG coordinate system consistency
        ax.plot(signal.real, -signal.imag, "k--", label="Ground Truth", alpha=0.6, linewidth=1.5)
        ax.plot(f_hat.real, -f_hat.imag, "r-", label=f"Reconstructed (r={r:.2f}, {retained_count} terms)", linewidth=2.0)
        ax.set_aspect("equal")
        ax.set_title(f"Heart Pruned: r={r:.2f}, Retained={retained_count}/{2*n_harmonics+1}\nMSE={mse:.2e}")
        ax.axis("off")
        ax.legend(loc="upper right")
        plt.tight_layout()

        out_name = f"heart_pruned_{r:.2f}.png"
        plt.savefig(out_name, dpi=150, bbox_inches="tight")
        plt.close(fig)

    print("\nSaved comparison plots: heart_pruned_0.96.png, heart_pruned_0.98.png, heart_pruned_0.99.png, heart_pruned_1.00.png")


if __name__ == "__main__":
    main()
