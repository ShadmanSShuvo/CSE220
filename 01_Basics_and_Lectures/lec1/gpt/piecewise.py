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

"""
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
"""



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