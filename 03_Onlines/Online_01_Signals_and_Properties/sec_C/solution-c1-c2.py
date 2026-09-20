import sys
import numpy as np
import matplotlib
# Use Agg backend for reliable headless execution; fallback if interactive
try:
    matplotlib.use("Agg")
except Exception:
    pass
import matplotlib.pyplot as plt


# =========================================================
# Helper functions
# =========================================================

def BuildEvenSignalFromRightSide(right_side_values):
    right_side_values = np.array(right_side_values, dtype=float)
    left_side_values = right_side_values[1:][::-1]
    return np.concatenate([left_side_values, right_side_values])


def StemPlot(ax, t, values, title, color):
    markerline, stemlines, baseline = ax.stem(t, values)

    plt.setp(markerline, marker="o", markersize=5, color=color)
    plt.setp(stemlines, linewidth=2, color=color)
    plt.setp(baseline, linewidth=1, color="black")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8, linestyle="--")
    ax.grid(True, alpha=0.25)

    ax.set_title(title)
    ax.set_xlabel("t")
    ax.set_ylabel("amplitude")


def CheckEven(values):
    return np.allclose(values, values[::-1])


def CheckOdd(values):
    return np.allclose(values, -values[::-1])


def PrintArray(name, values, decimals=1):
    formatted_values = ", ".join(f"{value:.{decimals}f}" for value in values)
    print(f"\n{name}:")
    print(f"[{formatted_values}]")


def PrintIntArray(name, values):
    formatted_values = ", ".join(f"{value:d}" for value in values)
    print(f"\n{name}:")
    print(f"[{formatted_values}]")


def FormatCheck(result):
    symbol = "✅" if result else "❌"
    return f"{symbol} {result}"


# =========================================================
# Choose one even signal
# =========================================================
# We use 15 samples: t = -7, -6, ..., 0, ..., 6, 7.
# So we only define the right side: t = 0, 1, ..., 7.
# Thus each array below defines x_e[0], x_e[1], x_e[2], ... etc.

even_signal_options = {
    1: ("Smooth hill-shaped even signal", [4.0, 3.6, 3.0, 2.2, 1.4, 0.8, 0.3, 0.0]),
    2: ("Triangular even signal",        [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]),
    3: ("Valley-shaped even signal",     [1.0, 1.2, 1.5, 2.0, 2.6, 3.2, 3.7, 4.0]),
    4: ("Oscillatory even signal",       [3.0, 2.2, 0.8, 1.4, 2.6, 1.8, 0.9, 2.1]),
    5: ("Flat-top even signal",          [4.0, 4.0, 4.0, 3.2, 2.2, 1.2, 0.5, 0.0]),
}

def solve_for_choice(choice=1, save_plots=True):
    print(f"\nProcessing Option {choice}: {even_signal_options[choice][0]}")
    right_side_even = even_signal_options[choice][1]

    # =========================================================
    # Build time axis and even component
    # =========================================================

    x_even = BuildEvenSignalFromRightSide(right_side_even)
    N = (len(x_even) - 1) // 2
    t = np.arange(-N, N + 1)

    PrintIntArray("Time axis", t)
    PrintArray("Even component x_e(t)", x_even)

    print("\nIs x_e(t) even?")
    print(FormatCheck(CheckEven(x_even)))

    # =========================================================
    # Find suitable M
    # =========================================================
    # Condition: x(t) = x_e(t) + x_o(t) = M for t >= 0.
    # At t = 0, since x_o is odd, x_o(0) = 0.
    # Therefore, M = x_e(0).
    M = float(x_even[t == 0][0])
    print(f"\nM = {M:.1f}")

    # =========================================================
    # Construct the odd component
    # =========================================================
    # For t >= 0: x(t) = x_e(t) + x_o(t) = M  ==>  x_o(t) = M - x_e(t)
    # Since x_o(t) is odd, x_o(-t) = -x_o(t)  ==>  for t < 0: x_o(t) = -(M - x_e(-t)) = x_e(t) - M
    x_odd = np.zeros_like(x_even)
    x_odd[t >= 0] = M - x_even[t >= 0]
    x_odd[t < 0] = x_even[t < 0] - M

    PrintArray("Odd component x_o(t)", x_odd)

    print("\nIs x_o(t) odd?")
    odd_check = CheckOdd(x_odd)
    print(FormatCheck(odd_check))

    # =========================================================
    # Construct the final signal
    # =========================================================

    x_total = x_even + x_odd

    PrintArray("Final signal x(t)", x_total)
    PrintArray("Right side of x(t), for t >= 0", x_total[t >= 0])

    # We need this following output to be True
    print("\nIs the right side constant M?")
    const_check = np.allclose(x_total[t >= 0], M)
    print(FormatCheck(const_check))

    # =========================================================
    # Plot results
    # =========================================================
    if save_plots:
        fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

        StemPlot(axes[0], t, x_even, f"Even Signal $x_e(t)$ (Option {choice})", "red")
        StemPlot(axes[1], t, x_odd, "Odd Signal $x_o(t)$", "green")
        StemPlot(axes[2], t, x_total, f"Total Signal $x(t) = x_e(t) + x_o(t)$ (Constant M={M:.1f} for t >= 0)", "blue")

        plt.suptitle("Constructing a Signal from Its Even Part", fontsize=14, fontweight="bold")
        plt.tight_layout()

        out_name = f"output_case_{choice}.png" if len(sys.argv) > 1 and sys.argv[1] == "--all" else "output.png"
        plt.savefig(out_name, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved plot to {out_name}")

    return odd_check and const_check


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        # Test all options
        all_passed = True
        for k in even_signal_options:
            passed = solve_for_choice(k, save_plots=True)
            if not passed:
                all_passed = False
        print("\nAll cases passed:", all_passed)
    else:
        # Check if choice is passed as CLI argument or prompt
        if len(sys.argv) > 1 and sys.argv[1].isdigit():
            choice = int(sys.argv[1])
        else:
            print("\nChoose an even signal:\n")
            for key, (name, values) in even_signal_options.items():
                print(f"{key}. {name}: {values}")
            try:
                choice = int(input("\nEnter a number from 1 to 5: "))
            except (EOFError, ValueError):
                choice = 1
        solve_for_choice(choice, save_plots=True)


if __name__ == "__main__":
    main()
