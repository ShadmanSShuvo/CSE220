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