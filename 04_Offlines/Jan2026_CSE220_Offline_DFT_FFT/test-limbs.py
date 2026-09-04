import numpy as np
BASE_DIGITS = 4
BASE = 10 ** BASE_DIGITS


def to_limbs(text, base_digits=BASE_DIGITS):
    """
    Convert a decimal string into polynomial coefficients.

    "123456789" with base_digits = 4 becomes the little-endian limb array
    [6789, 2345, 1] -- that is, 1*BASE^2 + 2345*BASE^1 + 6789*BASE^0.

    Parameters
    ----------
    text : str
        A decimal integer, possibly with a leading '+' or '-'.
    base_digits : int
        Decimal digits per limb.

    Returns
    -------
    (int, numpy.ndarray)
        The sign (+1 or -1) and the little-endian limb array (dtype int64).
        Handle the sign separately from the magnitude: the transform never
        sees it.
    """
    # TODO: implement this function
    text = str(text).strip()

    # Determine sign
    sign = 1

    if text.startswith("-"):
        sign = -1
        text = text[1:]
    elif text.startswith("+"):
        text = text[1:]

    # Make sure we actually have digits
    if not text:
        raise ValueError("Invalid decimal number")

    # Remove leading zeros
    text = text.lstrip("0")

    # Special case: zero
    if not text:
        return 1, np.array([0], dtype=np.int64)

    # Make sure the remaining characters are digits
    if not text.isdigit():
        raise ValueError("Invalid decimal number")

    # Split from the RIGHT into groups of base_digits.
    limbs = []

    for end in range(len(text), 0, -base_digits):
        start = max(0, end - base_digits)
        limbs.append(int(text[start:end]))

    return sign, np.array(limbs, dtype=np.int64)


if __name__ == "__main__":
    import sys

    # for arg in sys.argv[1:]:
    arg = "-0001234567890123456789012345678901234567890"
    sign, limbs = to_limbs(arg)
    print(f"{arg} -> sign={sign}, limbs={limbs}")

    print(to_limbs("123456789"))
    print(to_limbs("-123456789"))
    print(to_limbs("+123456789"))
    print(to_limbs("000012345"))
    print(to_limbs("0"))
    print(to_limbs("-0"))
