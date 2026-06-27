import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
print("1.Sine\n2.Cosine\n3.Square\n4.Exponential")
choice = int(input("Choice: "))

if choice == 1: y = np.sin(2 * np.pi * 5 * t)
elif choice == 2: y = np.cos(2 * np.pi * 5 * t)
elif choice == 3: y = np.sign(np.sin(2 * np.pi * 5 * t))
elif choice == 4: y = np.exp(-t)
else: exit()

plt.plot(t, y)
plt.grid(True)
plt.show()
