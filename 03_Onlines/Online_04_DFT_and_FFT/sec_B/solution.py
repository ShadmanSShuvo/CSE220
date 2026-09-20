"""
Solution for Online 04 DFT and FFT - Section B1, B2
Fourier Magnitude-Phase Swap between two images.
"""

import argparse
import os

import numpy as np

from image_conv import inverse_2d, transform_2d
from image_utils import load_image, save_comparison, save_image
from io_utils import write_report
from transforms import ArbitraryLengthFFT, DFTAnalyzer, FFTTransformer


def unit_phase(spectrum, epsilon=1e-12):
    """Return unit-magnitude complex values carrying only spectral phase."""
    spectrum = np.asarray(spectrum, dtype=np.complex128)
    magnitude = np.abs(spectrum)

    result = np.ones_like(spectrum, dtype=np.complex128)
    reliable = magnitude > epsilon
    result[reliable] = spectrum[reliable] / magnitude[reliable]
    return result


def swap_plane_spectra(plane_a, plane_b, engine):
    """Return magnitude(A)+phase(B) and magnitude(B)+phase(A) images."""
    plane_a = np.asarray(plane_a, dtype=np.float64)
    plane_b = np.asarray(plane_b, dtype=np.float64)
    if plane_a.ndim != 2 or plane_a.shape != plane_b.shape:
        raise ValueError("the two planes must have the same 2D shape")
    spectrum_a = transform_2d(plane_a, engine)
    spectrum_b = transform_2d(plane_b, engine)

    # Construct swapped spectra
    swapped_ab = np.abs(spectrum_a) * unit_phase(spectrum_b)
    swapped_ba = np.abs(spectrum_b) * unit_phase(spectrum_a)

    # Inverse transform and keep real part
    result_ab = inverse_2d(swapped_ab, engine).real
    result_ba = inverse_2d(swapped_ba, engine).real
    return result_ab, result_ba


def swap_images(image_a, image_b, engine):
    """Apply the magnitude-phase swap to matching grayscale or RGB images."""
    image_a = np.asarray(image_a, dtype=np.float64)
    image_b = np.asarray(image_b, dtype=np.float64)
    if image_a.shape != image_b.shape:
        raise ValueError("the two images must have the same shape")
    if image_a.ndim == 2:
        return swap_plane_spectra(image_a, image_b, engine)
    if image_a.ndim == 3 and image_a.shape[2] == 3:
        pairs = [
            swap_plane_spectra(image_a[:, :, c], image_b[:, :, c], engine)
            for c in range(3)
        ]
        result_ab = np.stack([pair[0] for pair in pairs], axis=2)
        result_ba = np.stack([pair[1] for pair in pairs], axis=2)
        return result_ab, result_ba
    raise ValueError("images must be grayscale or RGB")


def _make_engine(name):
    """Provided command-line engine selection."""
    if name == "dft":
        return DFTAnalyzer()
    if name == "fft":
        return FFTTransformer()
    if name == "arbitrary":
        return ArbitraryLengthFFT()
    raise ValueError("unknown engine: %r" % name)


def _check_plane(result, target_magnitude, target_phase, engine):
    """Provided helper: confirm that result has the requested spectrum parts."""
    spectrum = transform_2d(result, engine)
    obtained_magnitude = np.abs(spectrum)
    obtained_phase = unit_phase(spectrum)
    mag_error = float(np.max(np.abs(obtained_magnitude - target_magnitude)))
    phase_error = float(np.max(np.abs(obtained_phase - target_phase)))
    return mag_error, phase_error


def run(image_a_path, image_b_path, engine_name, out_dir, color=False):
    """Provided runner: create outputs and verify reconstructed spectra."""
    engine = _make_engine(engine_name)
    image_a = load_image(image_a_path, as_gray=not color)
    image_b = load_image(image_b_path, as_gray=not color)

    result_ab, result_ba = swap_images(image_a, image_b, engine)

    # Verification: check magnitude and phase match the design
    plane_a = image_a if image_a.ndim == 2 else image_a[:, :, 0]
    plane_b = image_b if image_b.ndim == 2 else image_b[:, :, 0]
    plane_ab = result_ab if result_ab.ndim == 2 else result_ab[:, :, 0]
    plane_ba = result_ba if result_ba.ndim == 2 else result_ba[:, :, 0]

    spec_a = transform_2d(plane_a, engine)
    spec_b = transform_2d(plane_b, engine)
    mag_a, phase_a = np.abs(spec_a), unit_phase(spec_a)
    mag_b, phase_b = np.abs(spec_b), unit_phase(spec_b)

    mag_err_ab, phase_err_ab = _check_plane(plane_ab, mag_a, phase_b, engine)
    mag_err_ba, phase_err_ba = _check_plane(plane_ba, mag_b, phase_a, engine)

    maximum_error = max(mag_err_ab, phase_err_ab, mag_err_ba, phase_err_ba)
    verdict = "MATCH" if maximum_error <= 1e-9 else "MISMATCH"

    os.makedirs(out_dir, exist_ok=True)
    save_image(np.clip(result_ab, 0.0, 1.0), os.path.join(out_dir, "mag_a_phase_b.png"))
    save_image(np.clip(result_ba, 0.0, 1.0), os.path.join(out_dir, "mag_b_phase_a.png"))
    save_comparison(
        [image_a, image_b, np.clip(result_ab, 0.0, 1.0), np.clip(result_ba, 0.0, 1.0)],
        ["image A", "image B", "mag A + phase B", "mag B + phase A"],
        os.path.join(out_dir, "comparison.png"),
        suptitle="Magnitude-Phase Swap: engine=%s" % engine_name,
    )

    write_report(os.path.join(out_dir, "report.txt"), [
        "Lab evaluation -- magnitude-phase swap",
        "image A : %s" % image_a_path,
        "image B : %s" % image_b_path,
        "shape   : %s" % (image_a.shape,),
        "engine  : %s" % engine_name,
        "max |obtained - requested| : %.3e" % maximum_error,
        "verification               : %s" % verdict,
    ])
    print("verification:", verdict, "(max error %.3e)" % maximum_error)
    print("wrote outputs to", out_dir)
    if verdict != "MATCH":
        raise RuntimeError("swapped results did not match the specification")
    return result_ab, result_ba


def main():
    parser = argparse.ArgumentParser(description="Swap Fourier magnitude and phase")
    parser.add_argument("--image-a", default="images/sunset512.png")
    parser.add_argument("--image-b", default="images/skyline512.png")
    parser.add_argument("--engine", choices=["dft", "fft", "arbitrary"],
                        default="fft")
    parser.add_argument("--color", action="store_true")
    parser.add_argument("--out-dir", default="outputs/lab_phase_swap_student")
    args = parser.parse_args()
    run(args.image_a, args.image_b, args.engine, args.out_dir, color=args.color)


if __name__ == "__main__":
    main()
