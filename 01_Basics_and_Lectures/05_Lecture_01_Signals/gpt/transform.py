import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 2000)

def signal(t):
    return np.where(
        (0 <= t) & (t <= 2),
        2 - t,
        np.where(
            (-2 <= t) & (t < 0),
            1,
            np.where(
                (2 < t) & (t <= 4),
                0.5 * (4 - t),
                0
            )
        )
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