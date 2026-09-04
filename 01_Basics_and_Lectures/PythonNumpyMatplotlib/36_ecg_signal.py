import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 2000)
ecg = np.sin(2*np.pi*1*t) + 0.4*np.sin(2*np.pi*5*t) + 0.2*np.sin(2*np.pi*15*t)

plt.plot(t, ecg)
plt.title("Simple ECG Approximation")
plt.grid(True)
plt.show()
