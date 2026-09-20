"""
Solution for Online 03 Continuous Fourier Transform - Section B
Continuous Fourier Transform 2D, Band-Pass/Band-Stop filtering, Complementarity check,
and DC brightness shift.
"""

import sys
import numpy as np
import matplotlib
try:
    matplotlib.use("Agg")
except Exception:
    pass
import matplotlib.pyplot as plt
try:
    from imageio.v2 import imread
except ImportError:
    from PIL import Image
    def imread(path, mode='L'):
        img = Image.open(path)
        if mode:
            img = img.convert(mode)
        return np.array(img)


# =====================================================================
# Classes for Continuous Image and 2D CFT / Inverse CFT
# =====================================================================

class ContinuousImage:
    """Represents a grayscale image as a continuous 2D spatial signal."""

    def __init__(self, image_path):
        self.image = imread(image_path, mode='L').astype(float)
        self.image = self.image / np.max(self.image)
        self.x = np.linspace(-1, 1, self.image.shape[1])
        self.y = np.linspace(-1, 1, self.image.shape[0])


class CFT2D:
    """2D Continuous Fourier Transform using separable numerical integration."""

    def __init__(self, image_obj: ContinuousImage):
        self.I = image_obj.image
        self.x = image_obj.x
        self.y = image_obj.y
        dx = self.x[1] - self.x[0]
        dy = self.y[1] - self.y[0]
        self.u = np.linspace(-1 / (2 * dx), 1 / (2 * dx), self.I.shape[1])
        self.v = np.linspace(-1 / (2 * dy), 1 / (2 * dy), self.I.shape[0])

    def compute_cft(self):
        Ny, Nx = self.I.shape
        Nv, Nu = len(self.v), len(self.u)
        trap_func = getattr(np, "trapezoid", getattr(np, "trapz", None))

        # Stage 1: integrate over x for each row y and each candidate u
        stage1_cos = np.empty((Ny, Nu))
        stage1_sin = np.empty((Ny, Nu))
        for k, uk in enumerate(self.u):
            phase = 2 * np.pi * uk * self.x
            stage1_cos[:, k] = trap_func(self.I * np.cos(phase)[None, :], self.x, axis=1)
            stage1_sin[:, k] = trap_func(self.I * np.sin(phase)[None, :], self.x, axis=1)

        # Stage 2: integrate over y for each candidate v
        real = np.empty((Nv, Nu))
        imag = np.empty((Nv, Nu))
        for m, vm in enumerate(self.v):
            phase = 2 * np.pi * vm * self.y
            cos_vy = np.cos(phase)[:, None]
            sin_vy = np.sin(phase)[:, None]
            real[m, :] = trap_func(stage1_cos * cos_vy - stage1_sin * sin_vy, self.y, axis=0)
            imag[m, :] = -trap_func(stage1_sin * cos_vy + stage1_cos * sin_vy, self.y, axis=0)

        return real, imag

    def plot_magnitude(self):
        real, imag = self.compute_cft()
        magnitude = np.sqrt(real ** 2 + imag ** 2)
        plt.imshow(np.log(1 + magnitude), cmap='gray')
        plt.title('2D CFT Magnitude Spectrum (log-scaled)')
        plt.axis('off')
        plt.savefig("cft_magnitude.png", bbox_inches="tight")
        plt.close()


class InverseCFT2D:
    """Inverse 2D-CFT using separable numerical integration."""

    def __init__(self, real, imag, u, v, x, y):
        self.real = real
        self.imag = imag
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def reconstruct(self):
        rows, cols = self.real.shape
        trap_func = getattr(np, "trapezoid", getattr(np, "trapz", None))

        P = np.zeros((cols, rows))
        Q = np.zeros((cols, rows))

        cos_vy = np.cos(2 * np.pi * self.y[:, None] * self.v[None, :])
        sin_vy = np.sin(2 * np.pi * self.y[:, None] * self.v[None, :])

        for iu in range(cols):
            R_u = self.real[:, iu]
            Q_u = self.imag[:, iu]

            P[iu, :] = trap_func(R_u[None, :] * cos_vy - Q_u[None, :] * sin_vy, self.v, axis=1)
            Q[iu, :] = trap_func(R_u[None, :] * sin_vy + Q_u[None, :] * cos_vy, self.v, axis=1)

        image = np.zeros((rows, cols))

        cos_ux = np.cos(2 * np.pi * self.x[:, None] * self.u[None, :])
        sin_ux = np.sin(2 * np.pi * self.x[:, None] * self.u[None, :])

        for iy in range(rows):
            P_y = P[:, iy]
            Q_y = Q[:, iy]

            image[iy, :] = trap_func(P_y[None, :] * cos_ux - Q_y[None, :] * sin_ux, self.u, axis=1)

        return image


# =====================================================================
# Task 1 & Task 3 — FrequencyFilter
# =====================================================================

class FrequencyFilter:

    def high_pass(self, real, imag, cutoff):
        """Given high pass filter."""
        rows, cols = real.shape
        cx, cy = rows // 2, cols // 2
        real = real.copy()
        imag = imag.copy()
        for i in range(rows):
            for j in range(cols):
                if np.sqrt((i - cx) ** 2 + (j - cy) ** 2) <= cutoff:
                    real[i, j] = 0
                    imag[i, j] = 0
        return real, imag

    def band_pass(self, real, imag, r_low, r_high):
        """Task 1: retain entries with r_low < d(i,j) <= r_high, zero the rest."""
        rows, cols = real.shape
        ci, cj = rows // 2, cols // 2
        i_coords, j_coords = np.ogrid[:rows, :cols]
        dist = np.sqrt((i_coords - ci) ** 2 + (j_coords - cj) ** 2)

        mask = (dist > r_low) & (dist <= r_high)
        real_bp = np.where(mask, real, 0.0)
        imag_bp = np.where(mask, imag, 0.0)
        return real_bp, imag_bp

    def band_stop(self, real, imag, r_low, r_high):
        """Task 1: zero entries with r_low < d(i,j) <= r_high, retain the rest."""
        rows, cols = real.shape
        ci, cj = rows // 2, cols // 2
        i_coords, j_coords = np.ogrid[:rows, :cols]
        dist = np.sqrt((i_coords - ci) ** 2 + (j_coords - cj) ** 2)

        mask = (dist > r_low) & (dist <= r_high)
        real_bs = np.where(mask, 0.0, real)
        imag_bs = np.where(mask, 0.0, imag)
        return real_bs, imag_bs

    def shift_brightness(self, real, imag, shift_amount):
        """Task 3: Add shift_amount strictly to the real component of the exact center pixel."""
        rows, cols = real.shape
        ci, cj = rows // 2, cols // 2
        real_shifted = real.copy()
        imag_shifted = imag.copy()
        real_shifted[ci, cj] += shift_amount
        return real_shifted, imag_shifted


# =====================================================================
# Task 2 — Complementarity check on raw spatial reconstructions
# =====================================================================

class ReconstructionValidator:

    def verify_complementarity(self, I_recon, I_bp, I_bs):
        """Task 2: verify the complementarity property. Return (is_valid, delta)."""
        delta = float(np.max(np.abs(I_bp + I_bs - I_recon)))
        is_valid = bool(delta < 1e-9)
        return is_valid, delta


# =====================================================================
# Entry point
# =====================================================================
if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "pikachu.png"
    r_low, r_high = 10, 50

    print(f"Processing '{input_path}' with r_low={r_low}, r_high={r_high}...")
    img = ContinuousImage(input_path)
    cft2d = CFT2D(img)
    real, imag = cft2d.compute_cft()

    filt = FrequencyFilter()
    real_bp, imag_bp = filt.band_pass(real, imag, r_low, r_high)
    real_bs, imag_bs = filt.band_stop(real, imag, r_low, r_high)

    def reconstruct(r, im):
        return InverseCFT2D(r, im, cft2d.u, cft2d.v, img.x, img.y).reconstruct()

    I_recon = reconstruct(real, imag)
    I_bp = reconstruct(real_bp, imag_bp)
    I_bs = reconstruct(real_bs, imag_bs)

    validator = ReconstructionValidator()
    is_valid, delta = validator.verify_complementarity(I_recon, I_bp, I_bs)
    print(f"Complementarity check: {is_valid} | max delta: {delta:.2e}")

    def save_edge_map(I_raw, path):
        edge_map = np.abs(I_raw)
        if edge_map.max() > 0:
            edge_map = edge_map / edge_map.max()
        plt.imsave(path, 1 - edge_map, cmap='gray')
        print(f"Saved {path}")

    save_edge_map(I_bp, "pikachu_bandpass.png")
    save_edge_map(I_bs, "pikachu_bandstop.png")

    # Task 3 execution
    real_shifted, imag_shifted = filt.shift_brightness(real, imag, shift_amount=2.0)
    I_brightened = reconstruct(real_shifted, imag_shifted)

    # Save brightened image (clip to [0,1], no edge-map inversion)
    I_brightened_clipped = np.clip(I_brightened, 0, 1)
    plt.imsave("pikachu_brightened.png", I_brightened_clipped, cmap='gray')
    print("Saved pikachu_brightened.png")
