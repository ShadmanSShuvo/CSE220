import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,500)

plt.plot(x,np.sin(x),label="sin(x)")

plt.plot(x,np.cos(x),label="cos(x)")

plt.title("Sine and Cosine")

plt.xlabel("Angle")

plt.ylabel("Amplitude")

plt.legend()

plt.grid()

plt.show()