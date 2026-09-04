import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Avoid Qt/OpenGL backend issues on some Linux setups.
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

print("\nChoose an even signal:\n")
for key, (name, values) in even_signal_options.items():
    print(f"{key}. {name}: {values}")

choice = int(input("\nEnter a number from 1 to 5: "))
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
# As per the problem definition, we can conclude that M must be the value of x_e(t) at t = 0

# TODO Set M as the value of x_e(t) at t = 0
# Replace the following line with the correct value of M
M = 0

print(f"\nM = {M:.1f}")


# =========================================================
# Construct the odd component
# =========================================================

# This following line is just a sample odd function so that the code is readily runnable
# You will need to comment out this line and construct the correct odd signal as required by the problem
x_odd = np.concatenate((-np.ones(N), [0], np.ones(N)))

# TODO Construct the required odd signal so that the right side is constant M for t>=0
# x_odd = None


PrintArray("Odd component x_o(t)", x_odd)

print("\nIs x_o(t) odd?")
print(FormatCheck(CheckOdd(x_odd)))


# =========================================================
# Construct the final signal
# =========================================================

x_total = x_even + x_odd

PrintArray("Final signal x(t)", x_total)

PrintArray("Right side of x(t), for t >= 0", x_total[t >= 0])

# We need this following output to be True
print("\nIs the right side constant M?")
print(FormatCheck(np.allclose(x_total[t >= 0], M)))


# =========================================================
# Plot results
# =========================================================

fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# TODO Generate 3 subplots showing the even part, odd part, and the final total signal 
# You may use the previously defined StemPlot function
# You may use the previously computed t array as the x-axis values while plotting the signals
# You may use any three different colors (e.g. red, green, blue) as you wish
StemPlot(axes[0], t, x_even, "Even Signal", "red")
#
#


plt.suptitle("Constructing a Signal from Its Even Part", fontsize=14, fontweight="bold")
plt.tight_layout()

plt.savefig("output.png", dpi=150, bbox_inches="tight")
plt.show()
