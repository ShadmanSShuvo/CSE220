import numpy as np

fs = 1000
t = np.arange(0, 1, 1/fs)

x = (
    2 * np.sin(2*np.pi*50*t)
    + 0.5 * np.sin(2*np.pi*120*t)
)

X = np.fft.rfft(x)
f = np.fft.rfftfreq(len(x), 1/fs)

magnitude = np.abs(X)

# Find index of largest frequency component
peak_index = np.argmax(magnitude)

dominant_frequency = f[peak_index]

print("Dominant frequency:", dominant_frequency, "Hz")
