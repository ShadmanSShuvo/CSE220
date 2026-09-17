import numpy as np
import matplotlib.pyplot as plt

# =====================================
# 1. DEFINE TIME
# =====================================

t = np.linspace(-10, 10, 2000)


# =====================================
# 2. DEFINE ORIGINAL SIGNAL
# =====================================

def signal(t):

    return np.where(
        (0 <= t) & (t <= 2),
        2 - t,
        0
    )


# =====================================
# 3. ORIGINAL SIGNAL
# =====================================

x = signal(t)


# =====================================
# 4. SIGNAL TRANSFORMATIONS
# =====================================

# Shift right by 2
x_right = signal(t - 2)

# Shift left by 2
x_left = signal(t + 2)

# Time reversal
x_reverse = signal(-t)

# Time compression
x_compressed = signal(2 * t)

# Time expansion
x_expanded = signal(t / 2)

# Amplitude scaling
x_amplitude = 2 * signal(t)

# General transformation:
# x(alpha*t + beta)

alpha = -3
beta = 2

x_transformed = signal(
    alpha * t + beta
)


# =====================================
# 5. EVEN-ODD DECOMPOSITION
# =====================================

x_negative = signal(-t)

x_even = (
    x + x_negative
) / 2

x_odd = (
    x - x_negative
) / 2


# =====================================
# 6. ENERGY AND POWER
# =====================================

energy = np.trapezoid(
    np.abs(x)**2,
    t
)

power = energy / (
    t[-1] - t[0]
)

print("Energy =", energy)
print("Average power =", power)


# =====================================
# 7. PLOT
# =====================================

plt.figure(figsize=(10, 6))

plt.plot(
    t,
    x,
    label="Original x(t)"
)

plt.plot(
    t,
    x_transformed,
    label="Transformed signal"
)

plt.axhline(
    0,
    color="black",
    linewidth=0.8
)

plt.axvline(
    0,
    color="black",
    linewidth=0.8
)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")

plt.title(
    "Signal Transformation"
)

plt.grid(True)
plt.legend()

plt.show()