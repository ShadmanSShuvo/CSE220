# Section C: Frequency-Domain Image Steganography

> **Topic:** 2D DFT Steganography, Circular Frequency Masking, and Watermark Embedding
> **Source Specification:** [`CSE220_Online.pdf`](./CSE220_Online.pdf)

---

## Overview

Image steganography is the practice of concealing a secret message or payload image within a host "cover" image such that the modified "stego" image is visually indistinguishable from the original.

While spatial-domain methods (e.g. LSB modification) are fragile against noise and compression, **frequency-domain steganography** leverages the human visual system's insensitivity to high spatial frequencies:
1. Compute the 2D DFT of the cover image: $F_{\text{cover}}(u, v)$.
2. Create a high-frequency circular mask selecting coefficients outside a cutoff radius $R_{\text{cutoff}}$ from the center:
   $$M(u, v) = \begin{cases} 1, & \sqrt{(u - c_u)^2 + (v - c_v)^2} > R_{\text{cutoff}} \\ 0, & \text{otherwise} \end{cases}$$
3. Modulate the secret image into the masked high-frequency band scaled by an embedding strength $\alpha$:
   $$F_{\text{stego}}(u, v) = F_{\text{cover}}(u, v) + \alpha \cdot M(u, v) \cdot F_{\text{secret}}(u, v)$$
4. Compute the 2D Inverse DFT to yield the stego image. Because the modification is restricted to high spatial frequencies, the visual appearance of the cover image is preserved with imperceptible distortion.

---

## Output Visualizations

Outputs stored in `outputs/lab_steganography_student/`:
- `cover.png`: Original host image.
- `secret.png`: Secret payload image to conceal.
- `stego.png`: Watermarked stego image looking identical to cover.
- `comparison.png`: Comprehensive visual report and difference map.

---

## How to Run

```bash
python3 solution.py
```
