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