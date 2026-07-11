Based on Lecture 1, the main coding concepts are: continuous/discrete signals, energy and power, amplitude scaling, time shifting, time reversal, time scaling, combined transformation , even/odd signals, and even–odd decomposition. 

Below is a reusable CSE 220 lab/online template using only NumPy and Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

1. General continuous-time signal template

Change only the signal(t) function for different questions.

import numpy as np
import matplotlib.pyplot as plt

# Time axis
t = np.linspace(-5, 5, 1000)

# Define x(t)
def signal(t):
    return np.sin(t)

# Calculate signal values
x = signal(t)

# Plot
plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.title("Continuous-Time Signal")
plt.xlabel("Time, t")
plt.ylabel("Amplitude")

plt.grid(True)
plt.legend()
plt.show()


---

2. Piecewise signal template

For example,

x(t)=
\begin{cases}
1, & -2\leq t<0\\
2-t, & 0\leq t\leq2\\
0, & \text{otherwise}
\end{cases}

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

def signal(t):
    return np.where(
        (-2 <= t) & (t < 0),
        1,
        np.where(
            (0 <= t) & (t <= 2),
            2 - t,
            0
        )
    )

x = signal(t)

plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Piecewise Signal")

plt.grid(True)
plt.legend()
plt.show()

A cleaner version using np.piecewise():

def signal(t):
    return np.piecewise(
        t,
        [
            (-2 <= t) & (t < 0),
            (0 <= t) & (t <= 2)
        ],
        [
            lambda t: 1,
            lambda t: 2 - t,
            0
        ]
    )


---

3. Amplitude scaling

For

y(t)=A x(t)

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

def signal(t):
    return np.sin(t)

A = 2

x = signal(t)
y = A * signal(t)

plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")
plt.plot(t, y, label=f"{A}x(t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.title("Amplitude Scaling")
plt.xlabel("Time, t")
plt.ylabel("Amplitude")

plt.grid(True)
plt.legend()
plt.show()

Remember:

y = 2 * signal(t)

means

y(t)=2x(t)

Only the vertical amplitude changes. Time does not change.


---

4. Time shifting: delay and advance

According to the slide:

x(t-t_0)

is delayed or shifted right, while

x(t+t_0)

is advanced or shifted left.

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2000)

def signal(t):
    return np.exp(-t**2)

t0 = 2

# Original
x = signal(t)

# Delay: shift right by 2
x_delay = signal(t - t0)

# Advance: shift left by 2
x_advance = signal(t + t0)

plt.figure(figsize=(10, 5))

plt.plot(t, x, label="x(t)")
plt.plot(t, x_delay, label="x(t - 2): right shift")
plt.plot(t, x_advance, label="x(t + 2): left shift")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Time Shifting")

plt.grid(True)
plt.legend()
plt.show()

Shortcut:

# Right shift by k
x_right = signal(t - k)

# Left shift by k
x_left = signal(t + k)

Memory rule:

> The sign appears opposite to the direction.



x(t-3)\rightarrow\text{right by 3}

x(t+3)\rightarrow\text{left by 3}


---

5. Time reversal

For

y(t)=x(-t)

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

# Use an asymmetric signal so reversal is visible
def signal(t):
    return np.where(
        (0 <= t) & (t <= 2),
        2 - t,
        0
    )

x = signal(t)

# Replace t with -t
x_reversed = signal(-t)

plt.figure(figsize=(8, 4))

plt.plot(t, x, label="x(t)")
plt.plot(t, x_reversed, label="x(-t)")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Time Reversal")

plt.grid(True)
plt.legend()
plt.show()

The important line is:

x_reversed = signal(-t)


---

6. Time scaling: compression and expansion

For

x(at)

: compression

: expansion/stretching


import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2000)

def signal(t):
    return np.exp(-t**2)

x = signal(t)

# x(2t): compressed
x_compressed = signal(2 * t)

# x(t/2): expanded
x_expanded = signal(t / 2)

plt.figure(figsize=(10, 5))

plt.plot(t, x, label="x(t)")
plt.plot(t, x_compressed, label="x(2t): compressed")
plt.plot(t, x_expanded, label="x(t/2): expanded")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("Time Scaling")

plt.grid(True)
plt.legend()
plt.show()

Shortcut:

# Compress by a
compressed = signal(a * t)

# Expand by a
expanded = signal(t / a)


---

7. General transformation: 

This is probably the most useful transformation template.

y(t)=x(\alpha t+\beta)

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2000)

def signal(t):
    return np.where(
        (0 <= t) & (t <= 2),
        2 - t,
        0
    )

# Change these values
alpha = -3
beta = 2

# Original
x = signal(t)

# Transformed signal
y = signal(alpha * t + beta)

plt.figure(figsize=(10, 5))

plt.plot(t, x, label="x(t)")
plt.plot(
    t,
    y,
    label=f"x({alpha}t + {beta})"
)

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("Time, t")
plt.ylabel("Amplitude")
plt.title("General Signal Transformation")

plt.grid(True)
plt.legend()
plt.show()

For the slide example,

x(-3t+2)

use:

alpha = -3
beta = 2

y = signal(alpha * t + beta)

or directly:

y = signal(-3 * t + 2)


---

8. Even and odd signal decomposition

For any signal:

x_e(t)
=
\frac{x(t)+x(-t)}{2}

and

x_o(t)
=
\frac{x(t)-x(-t)}{2}

The original signal can be reconstructed:

x(t)=x_e(t)+x_o(t)

Full reusable code

import numpy as np
import matplotlib.pyplot as plt

# Symmetric time axis is important
t = np.linspace(-5, 5, 1000)

# Define the original signal
def signal(t):
    return np.exp(-t) * (t >= 0)

# Original and reversed signals
x = signal(t)
x_reversed = signal(-t)

# Even part
x_even = (x + x_reversed) / 2

# Odd part
x_odd = (x - x_reversed) / 2

# Reconstruction
x_reconstructed = x_even + x_odd

# Plot
plt.figure(figsize=(10, 8))

# Original
plt.subplot(2, 2, 1)
plt.plot(t, x)
plt.title("Original Signal: x(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)

# Even part
plt.subplot(2, 2, 2)
plt.plot(t, x_even)
plt.title("Even Part")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)

# Odd part
plt.subplot(2, 2, 3)
plt.plot(t, x_odd)
plt.title("Odd Part")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)

# Reconstruction
plt.subplot(2, 2, 4)
plt.plot(t, x, label="x(t)")
plt.plot(
    t,
    x_reconstructed,
    "--",
    label="x_even + x_odd"
)

plt.title("Verification")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

The only part you generally change is:

def signal(t):
    return np.exp(-t) * (t >= 0)

Everything else remains the same.


---

9. Short even–odd template for an exam

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)

# Define x(t)
def signal(t):
    return np.exp(-t) * (t >= 0)

# Calculate x(t) and x(-t)
x = signal(t)
x_negative = signal(-t)

# Even and odd decomposition
x_even = (x + x_negative) / 2
x_odd = (x - x_negative) / 2

# Plot
plt.plot(t, x, label="x(t)")
plt.plot(t, x_even, label="Even part")
plt.plot(t, x_odd, label="Odd part")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Even-Odd Decomposition")

plt.grid()
plt.legend()
plt.show()


---

10. Checking whether a signal is even or odd

import numpy as np

t = np.linspace(-5, 5, 1000)

def signal(t):
    return t**2

x = signal(t)
x_reversed = signal(-t)

if np.allclose(x, x_reversed):
    print("The signal is EVEN.")

elif np.allclose(x, -x_reversed):
    print("The signal is ODD.")

else:
    print("The signal is neither even nor odd.")

Examples:

def signal(t):
    return t**2

Output:

The signal is EVEN.

Because:

x(-t)=(-t)^2=t^2=x(t)

For:

def signal(t):
    return t**3

Output:

The signal is ODD.

because:

x(-t)=(-t)^3=-t^3=-x(t)


---

11. Continuous-time energy and average power

The slide defines:

E=
\int |x(t)|^2dt

Numerically, use np.trapezoid():

import numpy as np

t = np.linspace(0, np.pi, 10000)

x = np.sin(t)

# Numerical integration
energy = np.trapezoid(
    np.abs(x)**2,
    t
)

# Average power over the interval
power = energy / (t[-1] - t[0])

print("Energy =", energy)
print("Average power =", power)

Expected approximately:

Energy = 1.5708
Average power = 0.5

because:

E=\frac{\pi}{2}

and

P=\frac12


---

12. Discrete signal plotting

For discrete signals, use plt.stem() instead of plt.plot().

import numpy as np
import matplotlib.pyplot as plt

# Discrete indices
n = np.arange(0, 4)

# Signal samples
x = np.array([1, -2, 2, -1])

plt.figure(figsize=(8, 4))

plt.stem(n, x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlabel("Sample index, n")
plt.ylabel("x[n]")
plt.title("Discrete-Time Signal")

plt.grid(True)
plt.show()


---

13. Discrete signal energy and power

E=\sum_n|x[n]|^2

P=
\frac1N
\sum_n|x[n]|^2

import numpy as np

x = np.array([1, -2, 2, -1])

# Energy
energy = np.sum(
    np.abs(x)**2
)

# Average power
power = np.mean(
    np.abs(x)**2
)

print("Energy =", energy)
print("Average power =", power)

Output:

Energy = 10
Average power = 2.5


---

14. Master template for CSE 220 Online 1

This combines almost everything:

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

For the online, remember these four lines:

# Shift
y = signal(t - t0)

# Reversal
y = signal(-t)

# Scaling
y = signal(a * t)

# Even-odd decomposition
x_even = (signal(t) + signal(-t)) / 2
x_odd = (signal(t) - signal(-t)) / 2

These are the core templates most likely to be reusable directly.
