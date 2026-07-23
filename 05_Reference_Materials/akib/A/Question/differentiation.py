import numpy as np
import matplotlib.pyplot as plt

# 1. Setup a dense continuous-time grid
t = np.linspace(0, 2, 1000)
dt = t[1] - t[0]  # The time step

# 2. Define a test signal: x(t) = sin(2 * pi * t)
x = np.sin(2 * np.pi * t)

# 3. Differentiate using np.gradient
# Passing 'dt' tells NumPy the physical spacing between points
dx_dt = np.gradient(x, dt)

# 4. Analytical verification: derivative of sin(2*pi*t) is 2*pi*cos(2*pi*t)
analytical_derivative = 2 * np.pi * np.cos(2 * np.pi * t)

# Plotting to verify they match perfectly
plt.plot(t,x,label='Original',linewidth=2,color='red')
plt.plot(t, dx_dt, label="Numerical (np.gradient)", linewidth=2)
plt.plot(t, analytical_derivative, '--', label="Analytical (Exact)", linewidth=2)
plt.title("Differentiation via np.gradient")
plt.legend()
plt.grid(True)
plt.show()