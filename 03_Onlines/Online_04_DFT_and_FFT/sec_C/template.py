import argparse
import os

import numpy as np

from image_utils import load_image, save_image, save_comparison
from transforms import DFTAnalyzer, FFTTransformer, ArbitraryLengthFFT
from image_conv import transform_2d, inverse_2d


def _make_engine(name):
    """Provided command-line engine selection."""

    if name == "dft":
        return DFTAnalyzer()

    if name == "fft":
        return FFTTransformer()

    if name == "arbitrary":
        return ArbitraryLengthFFT()

    raise ValueError("unknown engine: %r" % name)


def _pad_image(image, shape):
    """
    Place an image at the top-left corner of a larger complex array.
    """

    result = np.zeros(shape, dtype=np.complex128)

    height = min(image.shape[0], shape[0])
    width = min(image.shape[1], shape[1])

    result[:height, :width] = image[:height, :width]

    return result


def normalize_image(image):
    """
    Normalize an image to [0, 1].

    Provided helper.
    """

    image = np.real(image)

    minimum = np.min(image)
    maximum = np.max(image)

    if maximum - minimum < 1e-12:
        return np.zeros_like(image)

    return (image - minimum) / (maximum - minimum)

def create_frequency_mask(shape, cutoff_ratio):
    """
    Create a mask selecting the high-frequency region.

    Provided helper.

    Frequencies close to the centre are considered low frequency.
    Frequencies farther from the centre are considered high frequency.
    """

    height, width = shape

    yy, xx = np.mgrid[:height, :width]

    cy = height // 2
    cx = width // 2

    distance = np.sqrt(
        (yy - cy) ** 2 +
        (xx - cx) ** 2
    )

    cutoff = min(height, width) * cutoff_ratio

    mask = distance > cutoff

    return mask


def embed_secret(cover, secret, strength, engine):
    """
    Hide the secret image in selected frequency components of the
    cover image.

    Returns:
        stego image
        cover spectrum
        secret spectrum
        stego spectrum
    """

    cover = np.asarray(cover, dtype=np.float64)
    secret = np.asarray(secret, dtype=np.float64)

    if cover.ndim != 2 or secret.ndim != 2:
        raise ValueError("images must be grayscale 2D arrays")

    # The cover image determines the transform size.
    shape = cover.shape

    cover_padded = _pad_image(cover, shape)
    secret_padded = _pad_image(secret, shape)

    # ===============================================================
    # TODO 1:
    #
    # Compute the Fourier transform of both images using the supplied
    # transform implementation.
    #
    # cover_spectrum =
    # secret_spectrum =
    #
    # ===============================================================

    cover_spectrum =

    secret_spectrum =

    # ---------------------------------------------------------------
    # Select the high-frequency components.
    #
    # The mask is provided to the students.
    # ---------------------------------------------------------------

    high_frequency_mask = create_frequency_mask(
        shape,
        cutoff_ratio=0.20
    )

    # ===============================================================
    # TODO 2:
    #
    # Embed the secret information into the selected frequency
    # components of the cover spectrum.
    #
    # The embedding equation is:
    #
    # S = (1-a)C + aM
    #
    # where:
    #
    #     C = cover spectrum
    #     M = secret spectrum
    #     S = stego spectrum
    #     a = embedding strength
    #
    # Only the selected frequency components should be modified.
    #
    # ===============================================================

    stego_spectrum = cover_spectrum.copy()

    stego_spectrum[high_frequency_mask] =

    # ===============================================================
    # TODO 3:
    #
    # Perform the inverse transform on the modified spectrum.
    #
    # The final result should be a real-valued image.
    #
    # stego_image =
    #
    # ===============================================================

    stego_image = 

    stego_image = normalize_image(stego_image)

    return (
        stego_image,
        cover_spectrum,
        secret_spectrum,
        stego_spectrum,
    )


def run(
    cover_path,
    secret_path,
    strength,
    engine_name,
    out_dir,
):
    """
    Run the complete frequency-domain steganography experiment.
    """

    if not 0.0 < strength <= 1.0:
        raise ValueError(
            "strength must be in the range (0, 1]"
        )

    engine = _make_engine(engine_name)

    # ---------------------------------------------------------------
    # Load images.
    # ---------------------------------------------------------------

    cover = load_image(
        cover_path,
        as_gray=True
    )

    secret = load_image(
        secret_path,
        as_gray=True
    )

    if (
        secret.shape[0] > cover.shape[0]
        or secret.shape[1] > cover.shape[1]
    ):
        raise ValueError(
            "secret image must not be larger than the cover image"
        )

    # ---------------------------------------------------------------
    # Perform frequency-domain embedding.
    # ---------------------------------------------------------------

    (
        stego_image,
        cover_spectrum,
        secret_spectrum,
        stego_spectrum,
    ) = embed_secret(
        cover,
        secret,
        strength,
        engine,
    )

    # ---------------------------------------------------------------
    # Save outputs.
    # ---------------------------------------------------------------

    os.makedirs(
        out_dir,
        exist_ok=True
    )

    save_image(
        normalize_image(cover),
        os.path.join(
            out_dir,
            "cover.png"
        ),
    )

    save_image(
        normalize_image(secret),
        os.path.join(
            out_dir,
            "secret.png"
        ),
    )

    save_image(
        stego_image,
        os.path.join(
            out_dir,
            "stego.png"
        ),
    )

    # ---------------------------------------------------------------
    # Create a comparison image.
    # ---------------------------------------------------------------

    save_comparison(
        [
            cover,
            secret,
            stego_image,
        ],
        [
            "cover image",
            "secret image",
            "stego image",
        ],
        os.path.join(
            out_dir,
            "comparison.png"
        ),
        suptitle="Frequency-domain steganography",
    )

    # ---------------------------------------------------------------
    # Calculate how much the stego image differs from the cover.
    # ---------------------------------------------------------------

    cover_normalized = normalize_image(cover)

    difference = np.abs(
        stego_image - cover_normalized
    )

    mean_difference = float(
        np.mean(difference)
    )

    maximum_difference = float(
        np.max(difference)
    )

    print(
        "embedding strength:",
        strength
    )

    print(
        "mean cover/stego difference:",
        mean_difference
    )

    print(
        "maximum cover/stego difference:",
        maximum_difference
    )

    print(
        "wrote outputs to",
        out_dir
    )

    return stego_image


def main():

    parser = argparse.ArgumentParser(
        description="Frequency-domain image steganography"
    )

    parser.add_argument(
        "--cover-image",
        default="images/sunset512.png"
    )

    parser.add_argument(
        "--secret-image",
        default="images/skyline512.png"
    )

    parser.add_argument(
        "--strength",
        type=float,
        default=0.1
    )

    parser.add_argument(
        "--engine",
        choices=[
            "dft",
            "fft",
            "arbitrary"
        ],
        default="fft"
    )

    parser.add_argument(
        "--out-dir",
        default="outputs/lab_steganography_student"
    )

    args = parser.parse_args()

    run(
        args.cover_image,
        args.secret_image,
        args.strength,
        args.engine,
        args.out_dir,
    )


if __name__ == "__main__":
    main()
