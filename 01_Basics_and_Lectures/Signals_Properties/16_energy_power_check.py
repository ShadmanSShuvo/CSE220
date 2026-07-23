import numpy as np

x = np.array([2, 4, 6, 8])
energy = np.sum(x**2)
power = np.mean(x**2)

print("Energy =", energy)
print("Power =", power)
