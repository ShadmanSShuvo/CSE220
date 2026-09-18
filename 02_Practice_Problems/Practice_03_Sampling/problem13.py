"""
Problem 13: Sampling Theorem Visualizer ⭐⭐⭐
=============================================

Problem Statement:
------------------
Build an interactive Python/Streamlit application with three inputs:
    Signal frequency:       [slider]
    Sampling frequency:     [slider]
    Observation duration:   [slider]

The application should display:
    1. Original signal
    2. Sampled signal
    3. FFT of the sampled signal
    4. Nyquist frequency
    5. Whether aliasing occurs
    6. Aliased frequency, if applicable

Example:
    Signal frequency: 35 Hz
    Sampling frequency: 50 Hz

    Nyquist frequency: 25 Hz
    Aliasing: YES
    Observed frequency: 15 Hz

How to Run:
-----------
1. Run as Streamlit Web App:
       streamlit run problem13.py

2. Run as Interactive Matplotlib GUI Application:
       python3 problem13.py
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def compute_sampling_metrics(f_sig, f_samp):
    """Computes Nyquist frequency, aliasing condition, and apparent frequency."""
    f_nyq = f_samp / 2.0
    f_alias = abs(f_sig - f_samp * np.round(f_sig / f_samp))
    is_aliased = f_sig > f_nyq
    return f_nyq, is_aliased, f_alias


# ==============================================================================
# STREAMLIT IMPLEMENTATION
# ==============================================================================
def run_streamlit_app():
    import streamlit as st

    st.set_page_config(page_title="Sampling Theorem Visualizer", layout="wide")
    st.title("🔬 CSE220 Lab — Sampling Theorem Visualizer")
    st.markdown(
        "Explore how sampling frequency affects signal representation, demonstrating "
        "**Nyquist Criterion**, **Spectral Aliasing**, and **Frequency Folding**."
    )

    col_ctrl, col_display = st.columns([1, 3])

    with col_ctrl:
        st.header("🎛️ Control Panel")
        f_sig = st.slider("Signal Frequency (Hz)", min_value=1.0, max_value=100.0, value=35.0, step=1.0)
        f_samp = st.slider("Sampling Frequency fs (Hz)", min_value=5.0, max_value=200.0, value=50.0, step=1.0)
        duration = st.slider("Observation Duration (s)", min_value=0.05, max_value=2.0, value=0.2, step=0.05)

        f_nyq, is_aliased, f_alias = compute_sampling_metrics(f_sig, f_samp)

        st.subheader("📊 Theoretical Metrics")
        st.metric("Nyquist Frequency (fs/2)", f"{f_nyq:.1f} Hz")
        if is_aliased:
            st.error("⚠️ Aliasing: **YES** (fs < 2 * f)")
            st.metric("Observed / Alias Frequency", f"{f_alias:.1f} Hz")
        else:
            st.success("✅ Aliasing: **NO** (fs >= 2 * f)")
            st.metric("Observed Frequency", f"{f_sig:.1f} Hz")

    with col_display:
        Ts = 1.0 / f_samp
        t_cont = np.linspace(0, duration, 2000)
        x_cont = np.sin(2 * np.pi * f_sig * t_cont)

        t_samp = np.arange(0, duration + Ts / 2, Ts)
        x_samp = np.sin(2 * np.pi * f_sig * t_samp)

        # FFT of sampled signal
        duration_fft = max(2.0, duration * 5)
        N_fft = int(f_samp * duration_fft)
        t_fft = np.arange(N_fft) * Ts
        x_fft = np.sin(2 * np.pi * f_sig * t_fft)

        X = np.fft.rfft(x_fft)
        freqs = np.fft.rfftfreq(N_fft, d=Ts)
        mag = np.abs(X) / (N_fft / 2)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

        # Time domain
        ax1.plot(t_cont, x_cont, label=f"Original Analog Wave ({f_sig:.0f} Hz)", color="royalblue", alpha=0.7)
        if is_aliased:
            # Apparent wave
            x_apparent = -np.sin(2 * np.pi * f_alias * t_cont)
            ax1.plot(t_cont, x_apparent, "--", color="coral", lw=1.8, label=f"Apparent Alias ({f_alias:.0f} Hz)")

        markerline, stemlines, baseline = ax1.stem(
            t_samp,
            x_samp,
            linefmt="crimson",
            markerfmt="ro",
            basefmt="gray",
            label=f"Sample Points (fs = {f_samp:.0f} Hz)",
        )
        plt.setp(markerline, markersize=5)
        ax1.set_title(f"Time Domain: Signal = {f_sig:.0f} Hz, Sampling = {f_samp:.0f} Hz")
        ax1.set_xlabel("Time (seconds)")
        ax1.set_ylabel("Amplitude")
        ax1.grid(True, linestyle="--", alpha=0.5)
        ax1.legend(loc="upper right", fontsize=9)

        # Frequency domain
        markerline2, stemlines2, baseline2 = ax2.stem(
            freqs,
            mag,
            linefmt="navy",
            markerfmt="bo",
            basefmt="gray",
            label="Sampled FFT Magnitude",
        )
        plt.setp(markerline2, markersize=4)
        ax2.axvline(f_nyq, color="red", linestyle="--", lw=1.5, label=f"Nyquist Limit ({f_nyq:.1f} Hz)")
        ax2.axvline(f_alias, color="crimson", linestyle=":", lw=2, label=f"Observed Peak ({f_alias:.1f} Hz)")
        ax2.set_xlim(0, max(f_nyq + 10, 60))
        ax2.set_title("Frequency Domain (FFT Magnitude Spectrum)")
        ax2.set_xlabel("Frequency (Hz)")
        ax2.set_ylabel("Normalized Magnitude")
        ax2.grid(True, linestyle="--", alpha=0.5)
        ax2.legend(loc="upper right", fontsize=9)

        plt.tight_layout()
        st.pyplot(fig)


# ==============================================================================
# MATPLOTLIB INTERACTIVE GUI IMPLEMENTATION (STANDALONE PYTHON)
# ==============================================================================
def run_matplotlib_gui():
    print("=" * 70)
    print("CSE220 Lab — Problem 13: Sampling Theorem Visualizer")
    print("=" * 70)
    print("Launching Interactive Visualizer...")
    print("Tip: You can also run the web version using: streamlit run problem13.py\n")

    # Initial slider settings
    init_fsig = 35.0
    init_fsamp = 50.0
    init_dur = 0.25

    fig, (ax_time, ax_freq) = plt.subplots(2, 1, figsize=(11, 8.5))
    plt.subplots_adjust(bottom=0.28, hspace=0.35)

    def draw_plots(f_sig, f_samp, duration):
        ax_time.clear()
        ax_freq.clear()

        f_nyq, is_aliased, f_alias = compute_sampling_metrics(f_sig, f_samp)
        Ts = 1.0 / f_samp

        # Continuous signal
        t_cont = np.linspace(0, duration, 2000)
        x_cont = np.sin(2 * np.pi * f_sig * t_cont)

        # Sample points
        t_samp = np.arange(0, duration + Ts / 2, Ts)
        x_samp = np.sin(2 * np.pi * f_sig * t_samp)

        # FFT
        duration_fft = max(2.0, duration * 5)
        N_fft = int(f_samp * duration_fft)
        t_fft = np.arange(N_fft) * Ts
        x_fft = np.sin(2 * np.pi * f_sig * t_fft)

        X = np.fft.rfft(x_fft)
        freqs = np.fft.rfftfreq(N_fft, d=Ts)
        mag = np.abs(X) / (N_fft / 2)

        # Time plot
        ax_time.plot(t_cont, x_cont, label=f"Original Signal ({f_sig:.0f} Hz)", color="royalblue", alpha=0.7)
        if is_aliased:
            x_apparent = -np.sin(2 * np.pi * f_alias * t_cont)
            ax_time.plot(t_cont, x_apparent, "--", color="coral", lw=1.8, label=f"Apparent Alias ({f_alias:.0f} Hz)")

        markerline, stemlines, baseline = ax_time.stem(
            t_samp,
            x_samp,
            linefmt="crimson",
            markerfmt="ro",
            basefmt="gray",
            label=f"Samples (fs = {f_samp:.0f} Hz)",
        )
        plt.setp(markerline, markersize=4)

        status_str = f"ALIASED! (Observed: {f_alias:.1f} Hz)" if is_aliased else f"CLEAN (Observed: {f_sig:.1f} Hz)"
        color_box = "mistyrose" if is_aliased else "honeydew"

        ax_time.set_title(
            f"Time Domain | Signal: {f_sig:.0f} Hz, fs: {f_samp:.0f} Hz | Nyquist: {f_nyq:.1f} Hz | Status: {status_str}",
            bbox=dict(boxstyle="round,pad=0.4", facecolor=color_box, edgecolor="gray"),
            fontsize=10,
        )
        ax_time.set_xlabel("Time (seconds)")
        ax_time.set_ylabel("Amplitude")
        ax_time.grid(True, linestyle="--", alpha=0.5)
        ax_time.legend(loc="upper right", fontsize=8)

        # Frequency plot
        markerline2, stemlines2, baseline2 = ax_freq.stem(
            freqs,
            mag,
            linefmt="navy",
            markerfmt="bo",
            basefmt="gray",
            label="Sampled FFT Spectrum",
        )
        plt.setp(markerline2, markersize=4)
        ax_freq.axvline(f_nyq, color="red", linestyle="--", lw=1.5, label=f"Nyquist Limit fn = {f_nyq:.1f} Hz")
        ax_freq.axvline(f_alias, color="crimson", linestyle=":", lw=2, label=f"Spectral Peak = {f_alias:.1f} Hz")
        ax_freq.set_xlim(0, max(f_nyq + 10, 60))
        ax_freq.set_title(f"Frequency Spectrum | Dominant Peak at {f_alias:.1f} Hz", fontsize=10)
        ax_freq.set_xlabel("Frequency (Hz)")
        ax_freq.set_ylabel("Magnitude")
        ax_freq.grid(True, linestyle="--", alpha=0.5)
        ax_freq.legend(loc="upper right", fontsize=8)

    draw_plots(init_fsig, init_fsamp, init_dur)

    # Add slider axes at bottom
    ax_slider_sig = plt.axes([0.22, 0.15, 0.65, 0.03])
    ax_slider_samp = plt.axes([0.22, 0.10, 0.65, 0.03])
    ax_slider_dur = plt.axes([0.22, 0.05, 0.65, 0.03])

    s_sig = Slider(ax_slider_sig, "Signal Freq (Hz)", 1.0, 100.0, valinit=init_fsig, valstep=1.0)
    s_samp = Slider(ax_slider_samp, "Sampling fs (Hz)", 5.0, 200.0, valinit=init_fsamp, valstep=1.0)
    s_dur = Slider(ax_slider_dur, "Duration (s)", 0.05, 1.0, valinit=init_dur, valstep=0.05)

    def update(val):
        draw_plots(s_sig.val, s_samp.val, s_dur.val)
        fig.canvas.draw_idle()

    s_sig.on_changed(update)
    s_samp.on_changed(update)
    s_dur.on_changed(update)

    print("Example Demonstration:")
    f_nyq, is_aliased, f_alias = compute_sampling_metrics(init_fsig, init_fsamp)
    print(f"  Signal frequency:   {init_fsig} Hz")
    print(f"  Sampling frequency: {init_fsamp} Hz")
    print(f"  Nyquist frequency:  {f_nyq} Hz")
    print(f"  Aliasing:           {'YES' if is_aliased else 'NO'}")
    print(f"  Observed frequency: {f_alias} Hz")
    print("=" * 70)

    plt.show()


if __name__ == "__main__":
    is_streamlit = False
    try:
        from streamlit.runtime import exists as streamlit_exists
        is_streamlit = streamlit_exists()
    except Exception:
        pass

    if is_streamlit:
        run_streamlit_app()
    else:
        run_matplotlib_gui()
