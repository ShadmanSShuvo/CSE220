import numpy as np
import matplotlib.pyplot as plt
from imageio.v2 import imread


class ContinuousImage:
    """Represents a grayscale image as a continuous 2D spatial signal. (Given)"""

    def __init__(self, image_path):
        self.image = imread(image_path, mode='L').astype(float)
        self.image = self.image / np.max(self.image)

        # Continuous spatial coordinate vectors, both spanning [-1, 1]
        self.x = np.linspace(-1, 1, self.image.shape[1])
        self.y = np.linspace(-1, 1, self.image.shape[0])

    def show(self, title="Image"):
        plt.imshow(self.image, cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()


class CFT2D:
    """Computes the 2D Continuous Fourier Transform of a ContinuousImage
    using separable numerical (trapezoidal) integration."""

    def __init__(self, image_obj: ContinuousImage):
        self.I = image_obj.image
        self.x = image_obj.x
        self.y = image_obj.y

        # Frequency axes conjugate to x and y (given), spanning the full
        # Nyquist range implied by the sample spacing (dx, dy). This is
        # what lets the transform represent fine, edge-scale spatial
        # detail instead of only very coarse (near-DC) variation.
        dx = self.x[1] - self.x[0]
        dy = self.y[1] - self.y[0]
        self.u = np.linspace(-1 / (2 * dx), 1 / (2 * dx), self.I.shape[1])
        self.v = np.linspace(-1 / (2 * dy), 1 / (2 * dy), self.I.shape[0])

    def compute_cft(self):
        """
        Compute the real and imaginary parts of the 2D Continuous Fourier
        Transform of self.I, using SEPARABLE trapezoidal integration:

            Re{F(u,v)} =  Integral Integral I(x,y) cos(2*pi*(u*x + v*y)) dx dy
            Im{F(u,v)} = -Integral Integral I(x,y) sin(2*pi*(u*x + v*y)) dx dy

        Do NOT evaluate this as a direct 4-nested-loop double integral over
        (x, y, u, v) -- that is O(N^4) and will not finish in reasonable
        time. Instead exploit separability: expand cos(2*pi*(ux+vy)) and
        sin(2*pi*(ux+vy)) with the angle-sum identities, first integrate
        over x for every (y, u) pair, then integrate the result over y for
        every (u, v) pair. Each of the two stages is an O(N^3) operation
        (an O(N) numerical integral, repeated over an N x N grid), which is
        what makes this tractable.

        Use self.u and self.v (NOT self.x/self.y) as the frequency axes --
        they were already computed for you in __init__.

        Use np.trapezoid(..., axis=...) for the integration -- no built-in
        FFT/DFT routine (np.fft, scipy.fft, ...) may be used anywhere in
        this method.

        Returns
        -------
        real, imag : two 2D numpy arrays, each of shape self.I.shape
        """
        Ny, Nx = self.I.shape
        Nv, Nu = len(self.v), len(self.u)

        # Stage 1: integrate over x, for every row y and every candidate u.
        # Produces two (Ny, Nu) arrays.
        stage1_cos = np.empty((Ny, Nu))
        stage1_sin = np.empty((Ny, Nu))
        for k, uk in enumerate(self.u):
            phase = 2 * np.pi * uk * self.x                      # (Nx,)
            stage1_cos[:, k] = np.trapezoid(self.I * np.cos(phase)[None, :], self.x, axis=1)
            stage1_sin[:, k] = np.trapezoid(self.I * np.sin(phase)[None, :], self.x, axis=1)

        # Stage 2: integrate over y, for every candidate v (u already handled above).
        # cos(2pi(ux+vy)) = cos(2pi ux)cos(2pi vy) - sin(2pi ux)sin(2pi vy)
        # sin(2pi(ux+vy)) = sin(2pi ux)cos(2pi vy) + cos(2pi ux)sin(2pi vy)
        real = np.empty((Nv, Nu))
        imag = np.empty((Nv, Nu))
        for m, vm in enumerate(self.v):
            phase = 2 * np.pi * vm * self.y                      # (Ny,)
            cos_vy = np.cos(phase)[:, None]                        # (Ny, 1)
            sin_vy = np.sin(phase)[:, None]                        # (Ny, 1)
            real[m, :] = np.trapezoid(stage1_cos * cos_vy - stage1_sin * sin_vy, self.y, axis=0)
            imag[m, :] = -np.trapezoid(stage1_sin * cos_vy + stage1_cos * sin_vy, self.y, axis=0)

        return real, imag

    def plot_magnitude(self):
        """
        Plot the log-scaled magnitude spectrum of the 2D CFT computed by
        compute_cft(), i.e. plt.imshow(np.log(1 + magnitude), ...) where
        magnitude = sqrt(real**2 + imag**2). Purely for your own visual
        debugging -- not called by the command-line entry point below.
        """
        real, imag = self.compute_cft()
        magnitude = np.sqrt(real ** 2 + imag ** 2)
        plt.imshow(np.log(1 + magnitude), cmap='gray')
        plt.title('2D CFT Magnitude Spectrum (log-scaled)')
        plt.axis('off')
        plt.show()


class FrequencyFilter:
    """Applies frequency-domain filtering operations. (Given)"""

    def high_pass(self, real, imag, cutoff):
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


class InverseCFT2D:
    """Reconstructs the spatial-domain image from a (filtered) 2D frequency
    spectrum using separable numerical integration."""

    def __init__(self, real, imag, u, v, x, y):
        self.real = real
        self.imag = imag
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def reconstruct(self):
        """
        Perform the inverse 2D Continuous Fourier Transform:

            I(x,y) = Integral Integral F(u,v) exp(j*2*pi*(u*x + v*y)) du dv

        using the same separable-integration strategy as compute_cft():
        expand the complex exponential into cos/sin via Euler's identity,
        integrate over v first (for every (y, u) pair), then integrate
        that result over u (for every (x, y) pair). Use np.trapezoid.

        self.real, self.imag are the (possibly filtered) frequency-domain
        components; self.u, self.v are the frequency axes they were
        computed on; self.x, self.y are the spatial axes to reconstruct
        onto.

        Returns
        -------
        image : 2D numpy array of shape (len(self.y), len(self.x))
            The reconstructed real-valued spatial-domain signal. Note
            that after a high-pass filter this is NOT a valid image on
            its own (it will contain negative values, since the DC/
            low-frequency component that carried the average brightness
            has been removed) -- see the command-line entry point below
            for how it gets turned into a displayable edge map.
        """
        Nv, Nu = self.real.shape
        Ny, Nx = len(self.y), len(self.x)

        # I(x,y) = Re{ integral integral F(u,v) exp(j*2*pi*(ux+vy)) du dv }
        #   exp(j*theta) = cos(theta) + j*sin(theta), theta = 2*pi*(ux+vy)
        #   Re{(Re_F + j*Im_F)(cos(theta)+j*sin(theta))} = Re_F*cos(theta) - Im_F*sin(theta)
        # Expand cos(theta), sin(theta) via angle-sum and integrate over v first
        # (for every u, y pair), then over u (for every x, y pair).

        # Stage 1: integrate over v -> shape (Nu, Ny) for each of 4 combinations
        stage1_Rc = np.empty((Nu, Ny))  # integral Re(u,v) cos(2*pi*v*y) dv
        stage1_Rs = np.empty((Nu, Ny))  # integral Re(u,v) sin(2*pi*v*y) dv
        stage1_Ic = np.empty((Nu, Ny))  # integral Im(u,v) cos(2*pi*v*y) dv
        stage1_Is = np.empty((Nu, Ny))  # integral Im(u,v) sin(2*pi*v*y) dv

        for m, ym in enumerate(self.y):
            phase = 2 * np.pi * self.v * ym                       # (Nv,)
            cos_vy = np.cos(phase)                                  # (Nv,)
            sin_vy = np.sin(phase)                                  # (Nv,)
            # self.real, self.imag have shape (Nv, Nu); integrate over axis=0 (v)
            stage1_Rc[:, m] = np.trapezoid(self.real * cos_vy[:, None], self.v, axis=0)
            stage1_Rs[:, m] = np.trapezoid(self.real * sin_vy[:, None], self.v, axis=0)
            stage1_Ic[:, m] = np.trapezoid(self.imag * cos_vy[:, None], self.v, axis=0)
            stage1_Is[:, m] = np.trapezoid(self.imag * sin_vy[:, None], self.v, axis=0)

        # Stage 2: integrate over u -> shape (Ny, Nx)
        image = np.empty((Ny, Nx))
        for n, xn in enumerate(self.x):
            phase = 2 * np.pi * self.u * xn                        # (Nu,)
            cos_ux = np.cos(phase)                                   # (Nu,)
            sin_ux = np.sin(phase)                                   # (Nu,)

            # cos(theta) = cos_ux*cos_vy - sin_ux*sin_vy -> already v-integrated above
            re_cos_theta = cos_ux[:, None] * stage1_Rc - sin_ux[:, None] * stage1_Rs  # (Nu, Ny)
            # sin(theta) = sin_ux*cos_vy + cos_ux*sin_vy -> already v-integrated above
            im_sin_theta = sin_ux[:, None] * stage1_Ic + cos_ux[:, None] * stage1_Is  # (Nu, Ny)

            integrand = re_cos_theta - im_sin_theta                # (Nu, Ny)
            image[:, n] = np.trapezoid(integrand, self.u, axis=0)

        return image


# =====================================================
# Command-line entry point (given -- do not modify)
# Usage: python3 cft_edge_detector.py <input_image_path> <output_image_path> [cutoff]
# =====================================================
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python3 cft_edge_detector.py <input_image_path> <output_image_path> [cutoff]")
        print("Example: python3 cft_edge_detector.py pikachu.png pikachu_edges.png 15")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    cutoff = float(sys.argv[3]) if len(sys.argv) > 3 else 15

    img = ContinuousImage(input_path)
    cft2d = CFT2D(img)
    real, imag = cft2d.compute_cft()

    filt = FrequencyFilter()
    real_f, imag_f = filt.high_pass(real, imag, cutoff)

    icft2d = InverseCFT2D(real_f, imag_f, cft2d.u, cft2d.v, img.x, img.y)
    edges = icft2d.reconstruct()

    edge_map = np.abs(edges)
    if edge_map.max() > 0:
        edge_map = edge_map / edge_map.max()
    edge_map = 1 - edge_map  # invert: edges black, background white

    plt.imsave(output_path, edge_map, cmap='gray')
    print(f"Saved edge map to {output_path}")
