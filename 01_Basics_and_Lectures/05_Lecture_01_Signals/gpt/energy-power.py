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