import numpy as np
import matplotlib.pyplot as plt

A = float(input("Amplitude: "))
f = float(input("Frequency: "))
duration = float(input("Duration: "))

t = np.linspace(0, duration, 1000)
signal = A * np.sin(2 * np.pi * f * t)

plt.plot(t, signal)
plt.title("Generated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
