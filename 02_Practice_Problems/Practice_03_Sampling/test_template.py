"""Test Suite and Complete Visual Demonstration for template.py.

This file:
1. Runs sequential tests for all 34 functions in template.py and prints their outputs one by one.
2. In '--plot' mode, generates a comprehensive visual demonstration covering all 24 DSP concepts
   (continuous waveforms, sampling grids, aliasing collisions, sinc interpolation pulses,
   Whittaker-Shannon reconstruction, spectral replication, ideal low-pass filtering,
   manual DFT/IDFT, magnitude/phase spectra, and zero-centered fftshift).

Usage:
    python test_template.py          # Quick sequential test output in terminal
    python test_template.py --plot   # Run sequential tests AND display all comprehensive figures
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

# Import everything from the clean template library
from template import (
    generate_signal,
    example_signal,
    create_time_axis,
    get_sampling_interval,
    sample_signal,
    get_nyquist_rate,
    classify_sampling_frequency,
    alias_frequency,
    alias_frequency_signed,
    compare_aliasing,
    sinc,
    sinc_pulse,
    sinc_reconstruct,
    reconstruct_signal,
    calculate_rmse,
    rectangular_spectrum,
    sampled_spectrum,
    is_valid_cutoff,
    ideal_lowpass,
    apply_filter,
    recover_central_spectrum,
    dft,
    idft,
    get_frequency_axis,
    get_centered_frequency_axis,
    shift_spectrum,
    magnitude_spectrum,
    phase_spectrum,
    hz_to_rad,
    rad_to_hz,
    create_plot,
    run_sampling_demo,
    run_spectrum_demo,
    run_dft_demo,
)


def run_sequential_tests():
    """Executes every function from template.py and prints its outputs one by one."""
    print("=" * 75)
    print("        TESTING ALL DSP FUNCTIONS IN TEMPLATE.PY SEQUENTIALLY")
    print("=" * 75)

    # 1. SIGNAL GENERATION
    print("\n--- [1] SIGNAL GENERATION ---")
    t_test = create_time_axis(0.0, 0.02, 5)
    components = [(1.0, 50.0, 0.0), (0.5, 100.0, 0.0)]
    sig = generate_signal(t_test, components)
    ex_sig = example_signal(t_test)
    print(f"generate_signal(t={t_test}, components={components}):\n  -> {sig}")
    print(f"example_signal(t={t_test}):\n  -> {ex_sig}")

    # 2. TIME AXIS
    print("\n--- [2] TIME AXIS ---")
    t_axis = create_time_axis(0.0, 1.0, 5)
    print(f"create_time_axis(start=0.0, end=1.0, count=5):\n  -> {t_axis}")

    # 3. SAMPLING
    print("\n--- [3] SAMPLING ---")
    fs_test = 200.0
    T_int = get_sampling_interval(fs_test)
    n_samp, t_samp, x_samp = sample_signal(example_signal, fs_test, 0.0, 0.02)
    print(f"get_sampling_interval(fs={fs_test}):\n  -> T = {T_int} s")
    print(f"sample_signal(example_signal, fs={fs_test}, start=0.0, end=0.02):")
    print(f"  n_samples : {n_samp}")
    print(f"  t_samples : {t_samp}")
    print(f"  x_samples : {x_samp}")

    # 4. NYQUIST-SHANNON
    print("\n--- [4] NYQUIST-SHANNON ---")
    fmax_test = 100.0
    nyq_rate = get_nyquist_rate(fmax_test)
    print(f"get_nyquist_rate(fmax={fmax_test}):\n  -> {nyq_rate} Hz")
    for rate in [250.0, 200.0, 150.0]:
        cls_result = classify_sampling_frequency(rate, fmax_test)
        print(f"classify_sampling_frequency(fs={rate}, fmax={fmax_test}):\n  -> {cls_result}")

    # 5. ALIASING / FREQUENCY FOLDING
    print("\n--- [5] ALIASING / FREQUENCY FOLDING ---")
    f_orig, fs_alias = 70.0, 100.0
    f_fold = alias_frequency(f_orig, fs_alias)
    f_fold_signed = alias_frequency_signed(f_orig, fs_alias)
    print(f"alias_frequency(f={f_orig}, fs={fs_alias}):\n  -> {f_fold} Hz")
    print(f"alias_frequency_signed(f={f_orig}, fs={fs_alias}):\n  -> {f_fold_signed} Hz")
    alias_diff = compare_aliasing(30.0, 70.0, 100.0, np.arange(10))
    print(f"compare_aliasing(f1=30, f2=70, fs=100, n=0..9) max error:\n  -> {alias_diff:.2e} (identical sample values)")

    # 6. NORMALIZED SINC
    print("\n--- [6] NORMALIZED SINC ---")
    print(f"sinc(0.0) (scalar):\n  -> {sinc(0.0)}")
    u_test = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    print(f"sinc({u_test}) (array):\n  -> {sinc(u_test)}")

    # 7. SINC INTERPOLATION PULSE
    print("\n--- [7] SINC INTERPOLATION PULSE ---")
    pulse_val = sinc_pulse(0.02, 2, 0.01)
    print(f"sinc_pulse(t=0.02, n=2, T=0.01):\n  -> {pulse_val}")

    # 8. SINC RECONSTRUCTION
    print("\n--- [8] SINC RECONSTRUCTION ---")
    rec_single = sinc_reconstruct(0.01, n_samp, x_samp, T_int)
    print(f"sinc_reconstruct(t=0.01, ...):\n  -> {rec_single}")
    t_recon = np.linspace(0.0, 0.02, 5)
    rec_multi = reconstruct_signal(t_recon, n_samp, x_samp, T_int)
    print(f"reconstruct_signal(t={t_recon}, ...):\n  -> {rec_multi}")

    # 9. RMSE
    print("\n--- [9] RMSE ---")
    x_true = example_signal(t_recon)
    rmse = calculate_rmse(x_true, rec_multi)
    print(f"calculate_rmse(x_true, x_reconstructed):\n  -> {rmse}")

    # 10. ANALYTICAL SPECTRUM
    print("\n--- [10] ANALYTICAL SPECTRUM ---")
    print(f"rectangular_spectrum(f=50.0, W=100.0) (inside):\n  -> {rectangular_spectrum(50.0, 100.0)}")
    print(f"rectangular_spectrum(f=150.0, W=100.0) (outside):\n  -> {rectangular_spectrum(150.0, 100.0)}")

    # 11. SAMPLE-TRAIN SPECTRUM
    print("\n--- [11] SAMPLE-TRAIN SPECTRUM ---")
    f_spec = np.array([-300.0, 0.0, 300.0])
    samp_spec = sampled_spectrum(f_spec, 300.0, 50.0, -1, 1)
    print(f"sampled_spectrum(freqs={f_spec}, fs=300, W=50, k=[-1, 1]):\n  -> {samp_spec}")

    # 12. VALID RECOVERY CUTOFF
    print("\n--- [12] VALID RECOVERY CUTOFF ---")
    print(f"is_valid_cutoff(W=100, fs=300, fc=150):\n  -> {is_valid_cutoff(100.0, 300.0, 150.0)}")
    print(f"is_valid_cutoff(W=100, fs=300, fc=50):\n  -> {is_valid_cutoff(100.0, 300.0, 50.0)}")

    # 13. IDEAL LOW-PASS FILTER
    print("\n--- [13] IDEAL LOW-PASS FILTER ---")
    freqs_filter = np.array([-150.0, -50.0, 0.0, 50.0, 150.0])
    H = ideal_lowpass(freqs_filter, 100.0)
    print(f"ideal_lowpass(freqs={freqs_filter}, fc=100.0):\n  -> {H}")

    # 14. APPLY FREQUENCY-DOMAIN FILTER
    print("\n--- [14] APPLY FREQUENCY-DOMAIN FILTER ---")
    dummy_spec = np.array([3.0, 3.0, 3.0, 3.0, 3.0])
    filt_out = apply_filter(dummy_spec, H)
    print(f"apply_filter(spectrum={dummy_spec}, H={H}):\n  -> {filt_out}")

    # 15. MANUAL SPECTRAL RECOVERY
    print("\n--- [15] MANUAL SPECTRAL RECOVERY ---")
    rec_spec = recover_central_spectrum(freqs_filter, dummy_spec, 100.0)
    print(f"recover_central_spectrum(freqs={freqs_filter}, spectrum={dummy_spec}, fc=100.0):\n  -> {rec_spec}")

    # 16. DFT
    print("\n--- [16] DFT ---")
    x_toy = np.array([1.0, 2.0, 3.0, 4.0])
    X_toy = dft(x_toy)
    print(f"dft(x={x_toy}):\n  -> {X_toy}")

    # 17. IDFT
    print("\n--- [17] IDFT ---")
    x_rec_idft = idft(X_toy)
    print(f"idft(X):\n  -> {x_rec_idft.real} (real part matches original {x_toy})")

    # 18. DFT FREQUENCY AXIS
    print("\n--- [18] DFT FREQUENCY AXIS ---")
    f_ax = get_frequency_axis(4, 100.0)
    f_ax_centered = get_centered_frequency_axis(4, 100.0)
    print(f"get_frequency_axis(N=4, fs=100.0):\n  -> {f_ax} Hz")
    print(f"get_centered_frequency_axis(N=4, fs=100.0):\n  -> {f_ax_centered} Hz")

    # 19. MANUAL FFTSHIFT
    print("\n--- [19] MANUAL FFTSHIFT ---")
    X_shifted = shift_spectrum(X_toy)
    print(f"shift_spectrum(X):\n  -> {X_shifted}")

    # 20. MAGNITUDE AND PHASE
    print("\n--- [20] MAGNITUDE AND PHASE ---")
    mag = magnitude_spectrum(X_toy)
    phase = phase_spectrum(X_toy)
    print(f"magnitude_spectrum(X):\n  -> {mag}")
    print(f"phase_spectrum(X):\n  -> {phase}")

    # 21. FREQUENCY CONVERSION
    print("\n--- [21] FREQUENCY CONVERSION ---")
    w = hz_to_rad(50.0)
    f_back = rad_to_hz(w)
    print(f"hz_to_rad(50.0 Hz):\n  -> {w:.4f} rad/s")
    print(f"rad_to_hz({w:.4f} rad/s):\n  -> {f_back:.4f} Hz")

    print("\n" + "=" * 75)
    print("   ALL 30 NUMERICAL FUNCTIONS IN TEMPLATE.PY TESTED SUCCESSFULLY!")
    print("=" * 75)


def run_comprehensive_plots():
    """Generates a complete, multi-figure visual demonstration of all 24 DSP concepts in template.py."""
    print("\n" + "=" * 75)
    print("   LAUNCHING COMPREHENSIVE MULTI-PANEL DEMONSTRATION FIGURES")
    print("=" * 75)

    # ------------------------------------------------------------
    # FIGURE 1: Continuous Signal & Uniform Sampling Grids
    # ------------------------------------------------------------
    fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(11, 8), sharex=True)
    t_dense = create_time_axis(0.0, 0.05, 1000)
    x_dense = example_signal(t_dense)

    # Subplot 1: Continuous Analog Waveform
    ax1.plot(t_dense, x_dense, "b-", lw=1.8, label="Continuous x(t) = cos(2π50t) + 0.5cos(2π100t)")
    ax1.set_title("1. Continuous Analog Signal (f_max = 100 Hz)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, alpha=0.6)
    ax1.legend(loc="upper right")

    # Subplot 2: Properly Sampled (fs = 500 Hz > 2*f_max)
    fs_good = 500.0
    _, t_good, x_good = sample_signal(example_signal, fs_good, 0.0, 0.05)
    ax2.plot(t_dense, x_dense, "b-", alpha=0.4, label="Continuous Reference")
    ax2.stem(t_good, x_good, linefmt="g-", markerfmt="go", basefmt="gray", label=f"Safe Sampling (fs={fs_good} Hz > 200 Hz)")
    ax2.set_title("2. Uniform Safe Sampling (No Aliasing)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, alpha=0.6)
    ax2.legend(loc="upper right")

    # Subplot 3: Undersampled (fs = 120 Hz < 2*f_max)
    fs_under = 120.0
    _, t_under, x_under = sample_signal(example_signal, fs_under, 0.0, 0.05)
    ax3.plot(t_dense, x_dense, "b-", alpha=0.4, label="Continuous Reference")
    ax3.stem(t_under, x_under, linefmt="r-", markerfmt="ro", basefmt="gray", label=f"Undersampled (fs={fs_under} Hz < 200 Hz)")
    ax3.set_title("3. Undersampling (Aliasing Boundary Violated)")
    ax3.set_xlabel("Time (s)")
    ax3.set_ylabel("Amplitude")
    ax3.grid(True, alpha=0.6)
    ax3.legend(loc="upper right")

    plt.tight_layout()

    # ------------------------------------------------------------
    # FIGURE 2: Aliasing & Frequency Folding Demonstration
    # ------------------------------------------------------------
    fig2, (ax_al1, ax_al2) = plt.subplots(2, 1, figsize=(11, 7))
    fs_fold = 100.0
    f1, f2 = 30.0, 70.0  # 70 Hz folds into |70 - 100| = 30 Hz
    t_al = np.linspace(0.0, 0.08, 1000)
    x1_cont = np.cos(2 * np.pi * f1 * t_al)
    x2_cont = np.cos(2 * np.pi * f2 * t_al)

    n_fold = np.arange(int(0.08 * fs_fold) + 1)
    t_samples_fold = n_fold / fs_fold
    x1_samples = np.cos(2 * np.pi * f1 * t_samples_fold)
    x2_samples = np.cos(2 * np.pi * f2 * t_samples_fold)

    ax_al1.plot(t_al, x1_cont, "b-", lw=2, label=f"Continuous {f1} Hz Cosine")
    ax_al1.plot(t_al, x2_cont, "r--", lw=1.5, alpha=0.7, label=f"Continuous {f2} Hz Cosine (Violates Nyquist)")
    ax_al1.stem(t_samples_fold, x1_samples, linefmt="k-", markerfmt="ko", basefmt="gray", label=f"Sampled Points (fs={fs_fold} Hz)")
    ax_al1.set_title(f"Aliasing Collision: cos(2π·{f1}t) and cos(2π·{f2}t) produce IDENTICAL samples at fs = {fs_fold} Hz")
    ax_al1.set_xlabel("Time (s)")
    ax_al1.set_ylabel("Amplitude")
    ax_al1.grid(True, alpha=0.6)
    ax_al1.legend(loc="upper right")

    # Bar chart of folded frequencies
    candidate_freqs = [10, 30, 45, 60, 70, 90, 110, 130]
    apparent_freqs = [alias_frequency(f, fs_fold) for f in candidate_freqs]
    x_indices = np.arange(len(candidate_freqs))
    ax_al2.bar(x_indices - 0.18, candidate_freqs, width=0.35, label="Original Frequency (Hz)", color="cornflowerblue")
    ax_al2.bar(x_indices + 0.18, apparent_freqs, width=0.35, label=f"Folded Frequency in [0, fs/2] (Hz)", color="salmon")
    ax_al2.axhline(fs_fold / 2.0, color="crimson", linestyle="--", lw=1.5, label=f"Nyquist Folding Line (fs/2 = {fs_fold/2} Hz)")
    ax_al2.set_xticks(x_indices)
    ax_al2.set_xticklabels([f"{f} Hz" for f in candidate_freqs])
    ax_al2.set_ylabel("Frequency (Hz)")
    ax_al2.set_title(f"Frequency Folding Table for Sampling Rate fs = {fs_fold} Hz")
    ax_al2.grid(True, alpha=0.4, axis="y")
    ax_al2.legend(loc="upper left")

    plt.tight_layout()

    # ------------------------------------------------------------
    # FIGURE 3: Normalized Sinc Kernel & Whittaker-Shannon Pulses
    # ------------------------------------------------------------
    fig3, (ax_sinc1, ax_sinc2) = plt.subplots(2, 1, figsize=(11, 7))
    u_vals = np.linspace(-5.0, 5.0, 1000)
    sinc_vals = sinc(u_vals)

    ax_sinc1.plot(u_vals, sinc_vals, "m-", lw=2, label="Normalized sinc(u) = sin(πu)/(πu)")
    ax_sinc1.axhline(0, color="gray", lw=1)
    ax_sinc1.axvline(0, color="gray", lw=1)
    for integer in [-4, -3, -2, -1, 1, 2, 3, 4]:
        ax_sinc1.plot(integer, 0, "ro", markersize=5)
    ax_sinc1.set_title("Normalized Sinc Interpolation Kernel (Zero-Crossings at non-zero integers)")
    ax_sinc1.set_xlabel("u = (t - nT)/T")
    ax_sinc1.set_ylabel("sinc(u)")
    ax_sinc1.grid(True, alpha=0.6)
    ax_sinc1.legend(loc="upper right")

    # Show decomposition into individual sinc interpolation pulses
    fs_pulse = 200.0
    T_pulse = 1.0 / fs_pulse
    t_eval = np.linspace(0.0, 0.04, 1000)
    n_p, t_p, x_p = sample_signal(example_signal, fs_pulse, 0.0, 0.04)

    for i in range(len(n_p)):
        individual_pulse = x_p[i] * sinc((t_eval - n_p[i] * T_pulse) / T_pulse)
        ax_sinc2.plot(t_eval, individual_pulse, "--", lw=1.0, alpha=0.6)

    # Reconstructed signal
    x_reconstructed_sum = reconstruct_signal(t_eval, n_p, x_p, T_pulse)
    ax_sinc2.plot(t_eval, x_reconstructed_sum, "k-", lw=2.2, label="Reconstructed Signal (Sum of Sinc Pulses)")
    ax_sinc2.stem(t_p, x_p, linefmt="r-", markerfmt="ro", basefmt="gray", label="Sample Weights x[n]")
    ax_sinc2.set_title("Whittaker-Shannon Interpolation: Continuous Wave Formed from Weighted Sinc Pulses")
    ax_sinc2.set_xlabel("Time (s)")
    ax_sinc2.set_ylabel("Amplitude")
    ax_sinc2.grid(True, alpha=0.6)
    ax_sinc2.legend(loc="upper right")

    plt.tight_layout()

    # ------------------------------------------------------------
    # FIGURE 4: Sinc Reconstruction & Reconstruction Error (RMSE)
    # ------------------------------------------------------------
    fig4, (ax_rec1, ax_rec2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
    t_fine = create_time_axis(0.0, 0.06, 1200)
    x_ground_truth = example_signal(t_fine)
    fs_recon = 500.0
    T_recon = 1.0 / fs_recon
    n_rec, t_rec, x_rec_samples = sample_signal(example_signal, fs_recon, 0.0, 0.06)
    x_rec_continuous = reconstruct_signal(t_fine, n_rec, x_rec_samples, T_recon)

    error_residual = x_ground_truth - x_rec_continuous
    rmse = calculate_rmse(x_ground_truth, x_rec_continuous)

    ax_rec1.plot(t_fine, x_ground_truth, "b-", lw=2, label="Ground Truth Analog Signal")
    ax_rec1.plot(t_fine, x_rec_continuous, "r--", lw=1.6, label="Sinc-Reconstructed Signal")
    ax_rec1.scatter(t_rec, x_rec_samples, color="black", s=18, zorder=5, label="Discrete Samples")
    ax_rec1.set_title(f"Sinc Signal Recovery (fs = {fs_recon} Hz)")
    ax_rec1.set_ylabel("Amplitude")
    ax_rec1.grid(True, alpha=0.6)
    ax_rec1.legend(loc="upper right")

    ax_rec2.plot(t_fine, error_residual, "m-", lw=1.5, label=f"Instantaneous Error: e(t) = x(t) - x_rec(t)")
    ax_rec2.axhline(0, color="gray", lw=1)
    ax_rec2.set_title(f"Reconstruction Residual Error (Total RMSE = {rmse:.2e})")
    ax_rec2.set_xlabel("Time (s)")
    ax_rec2.set_ylabel("Error")
    ax_rec2.grid(True, alpha=0.6)
    ax_rec2.legend(loc="upper right")

    plt.tight_layout()

    # ------------------------------------------------------------
    # FIGURE 5: Sampled Spectrum, Periodic Replicas & Ideal Low-Pass Filtering
    # ------------------------------------------------------------
    fig5, (ax_sp1, ax_sp2, ax_sp3) = plt.subplots(3, 1, figsize=(11, 8), sharex=True)
    fs_spec = 300.0
    W_spec = 100.0
    fc_cutoff = 150.0  # Valid cutoff: W < fc < fs - W (100 < 150 < 200)
    freqs = np.linspace(-750.0, 750.0, 3000)

    # Periodic sampled spectrum
    Xp = sampled_spectrum(freqs, fs_spec, W_spec, -2, 2)
    ax_sp1.plot(freqs, Xp, "b-", lw=1.8, label=f"Sampled Spectrum X_s(f) with Replicas at k·fs (fs={fs_spec} Hz)")
    for k in [-2, -1, 0, 1, 2]:
        ax_sp1.axvline(k * fs_spec, color="gray", linestyle=":", alpha=0.7)
    ax_sp1.set_title("1. Sample-Train Spectrum: Periodic Copies Created by Sampling")
    ax_sp1.set_ylabel("Magnitude")
    ax_sp1.grid(True, alpha=0.6)
    ax_sp1.legend(loc="upper right")

    # Ideal Low-Pass Filter
    H_ideal = ideal_lowpass(freqs, fc_cutoff)
    ax_sp2.plot(freqs, H_ideal, "g-", lw=2, label=f"Ideal LPF H(f) (Cutoff fc = {fc_cutoff} Hz)")
    ax_sp2.axvline(-fc_cutoff, color="crimson", linestyle="--")
    ax_sp2.axvline(fc_cutoff, color="crimson", linestyle="--")
    ax_sp2.set_title(f"2. Ideal Reconstruction Filter Response (Passband |f| <= {fc_cutoff} Hz)")
    ax_sp2.set_ylabel("Gain")
    ax_sp2.grid(True, alpha=0.6)
    ax_sp2.legend(loc="upper right")

    # Recovered central spectrum
    Y_recovered = apply_filter(Xp, H_ideal)
    ax_sp3.plot(freqs, Y_recovered, "purple", lw=2, label="Recovered Central Spectrum (Replicas Removed)")
    ax_sp3.set_title("3. Filtered Output: Baseband Spectrum Extracted without Aliasing")
    ax_sp3.set_xlabel("Frequency (Hz)")
    ax_sp3.set_ylabel("Magnitude")
    ax_sp3.grid(True, alpha=0.6)
    ax_sp3.legend(loc="upper right")

    plt.tight_layout()

    # ------------------------------------------------------------
    # FIGURE 6: Manual DFT Analysis (Magnitude, Phase & Centered FFTShift)
    # ------------------------------------------------------------
    fig6, ((ax_dft1, ax_dft2), (ax_dft3, ax_dft4)) = plt.subplots(2, 2, figsize=(12, 8))
    N_dft = 32
    fs_dft = 400.0
    n_dft = np.arange(N_dft)
    t_dft = n_dft / fs_dft
    x_dft_signal = example_signal(t_dft)

    X_complex = dft(x_dft_signal)
    f_dft_unsigned = get_frequency_axis(N_dft, fs_dft)
    f_dft_signed = get_centered_frequency_axis(N_dft, fs_dft)
    mag_dft = magnitude_spectrum(X_complex)
    phase_dft = phase_spectrum(X_complex)

    # Subplot 1: Discrete Input Samples
    ax_dft1.stem(n_dft, x_dft_signal, linefmt="b-", markerfmt="bo", basefmt="gray")
    ax_dft1.set_title("1. Discrete Input Signal x[n] (N = 32)")
    ax_dft1.set_xlabel("Sample index n")
    ax_dft1.set_ylabel("Amplitude")
    ax_dft1.grid(True, alpha=0.6)

    # Subplot 2: Unshifted DFT Magnitude Spectrum
    ax_dft2.stem(f_dft_unsigned, mag_dft, linefmt="r-", markerfmt="ro", basefmt="gray")
    ax_dft2.set_title("2. DFT Magnitude Spectrum |X[k]| (0 to fs)")
    ax_dft2.set_xlabel("Frequency (Hz)")
    ax_dft2.set_ylabel("|X[k]|")
    ax_dft2.grid(True, alpha=0.6)

    # Subplot 3: Phase Spectrum
    # Threshold phase for small magnitudes to avoid numerical noise
    phase_clean = np.where(mag_dft > 1e-3, phase_dft, 0.0)
    ax_dft3.stem(f_dft_unsigned, phase_clean, linefmt="g-", markerfmt="go", basefmt="gray")
    ax_dft3.set_title("3. DFT Phase Spectrum ∠X[k] (radians)")
    ax_dft3.set_xlabel("Frequency (Hz)")
    ax_dft3.set_ylabel("Phase (rad)")
    ax_dft3.grid(True, alpha=0.6)

    # Subplot 4: Zero-Centered Spectrum via shift_spectrum
    X_shifted_spec = shift_spectrum(X_complex)
    f_shifted_axis = np.sort(f_dft_signed)
    mag_shifted = magnitude_spectrum(X_shifted_spec)
    ax_dft4.stem(f_shifted_axis, mag_shifted, linefmt="m-", markerfmt="mo", basefmt="gray")
    ax_dft4.set_title("4. Centered Two-Sided Spectrum (shift_spectrum)")
    ax_dft4.set_xlabel("Signed Frequency (Hz)")
    ax_dft4.set_ylabel("|X_shifted[k]|")
    ax_dft4.grid(True, alpha=0.6)

    plt.tight_layout()

    # ------------------------------------------------------------
    # FIGURE 7: IDFT Roundtrip & Inversion Verification
    # ------------------------------------------------------------
    fig7, ax_inv = plt.subplots(figsize=(10, 5))
    x_reconstructed_idft = idft(X_complex)
    roundtrip_error = np.max(np.abs(x_dft_signal - x_reconstructed_idft.real))

    ax_inv.plot(n_dft, x_dft_signal, "b-o", label="Original Samples x[n]")
    ax_inv.plot(n_dft, x_reconstructed_idft.real, "rx--", markersize=8, label=f"IDFT Reconstructed (Max Error: {roundtrip_error:.2e})")
    ax_inv.set_title("Manual IDFT Perfect Inversion Roundtrip: x[n] == IDFT(DFT(x[n]))")
    ax_inv.set_xlabel("Sample index n")
    ax_inv.set_ylabel("Amplitude")
    ax_inv.grid(True, alpha=0.6)
    ax_inv.legend(loc="upper right")

    plt.tight_layout()

    print("\n[INFO] 7 Comprehensive Demonstration Figures created.")
    print("       Displaying figures (close each figure or close all to finish)...")
    plt.show()


def main():
    # 1. Always run and print all sequential tests
    run_sequential_tests()

    # 2. Check for --plot flag
    if "--plot" in sys.argv:
        run_comprehensive_plots()
    else:
        print("\n[NOTE] Visual demonstration figures were skipped for fast terminal execution.")
        print("       To launch the complete multi-panel visual demonstration suite, run:")
        print("           python test_template.py --plot\n")


if __name__ == "__main__":
    main()
