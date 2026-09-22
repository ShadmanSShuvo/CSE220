import numpy as np

# from svg_utils import load_svg_path
# from epicycle_animation import save_outputs


class FourierEpicycles:
    def __init__(self, t, signal, n_harmonics):
        self.t = t
        self.signal = signal
        self.N = n_harmonics
        self.T = t[-1] - t[0]          # closed interval [0, T], so this is just t[-1]
        self.omega = 2 * np.pi / self.T
        self.coeffs = {}

    def calculate_cn(self, n):
        kernel = np.exp(-1j * n * self.omega * self.t)
        integrand = self.signal * kernel
        return (1.0 / self.T) * np.trapezoid(integrand, self.t)

    def calculate_all_coefficients(self):
        for n in range(-self.N, self.N + 1):
            self.coeffs[n] = self.calculate_cn(n)

    def approximate(self, t):
        t = np.asarray(t, dtype=float)
        scalar_input = (t.ndim == 0)
        t = np.atleast_1d(t)

        result = np.zeros_like(t, dtype=complex)
        for n, cn in self.coeffs.items():
            result += cn * np.exp(1j * n * self.omega * t)

        return result[0] if scalar_input else result


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        print("Usage: python3 assignment.py <path_to_svg> [n_harmonics] [comparison_png_path] [gif_path]")
        print("Example: python3 assignment.py svgs/heart.svg 150 heart_comparison.png heart_epicycles.gif")
        sys.exit(1)

    svg_path = sys.argv[1]
    N_HARMONICS = int(sys.argv[2]) if len(sys.argv) > 2 else 150
    stem = Path(svg_path).stem
    comparison_path = sys.argv[3] if len(sys.argv) > 3 else f"{stem}_comparison.png"
    gif_path = sys.argv[4] if len(sys.argv) > 4 else f"{stem}_epicycles.gif"

    t, z = load_svg_path(svg_path, num_points=1000)
    fs = FourierEpicycles(t, z, n_harmonics=N_HARMONICS)
    fs.calculate_all_coefficients()

    save_outputs(fs, z, comparison_path, gif_path, num_frames=240)
