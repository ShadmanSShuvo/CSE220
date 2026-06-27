# x(t)=Asin(2πft)
import numpy as np

def generate_signal(amplitude, frequency, t):
    return amplitude * np.sin(2*np.pi*frequency*t)


t = np.linspace(0,1,1000)

signal = generate_signal(2,5,t)

print(signal)