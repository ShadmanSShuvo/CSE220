import os
import zipfile

folder_name = "CSE220_Sessional_Part4"
os.makedirs(folder_name, exist_ok=True)

problems = {
    "31_signal_statistics.py": """import numpy as np
import matplotlib.pyplot as plt

A = 2
f = 5
t = np.linspace(0, 2, 1000)
signal = A * np.sin(2 * np.pi * f * t)

print("Maximum =", np.max(signal))
print("Minimum =", np.min(signal))
print("Mean =", np.mean(signal))

rms = np.sqrt(np.mean(signal**2))
print("RMS =", rms)

plt.plot(t, signal)
plt.title("Sine Wave")
plt.grid(True)
plt.show()
""",

    "32_signal_scaling.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
x = np.sin(t)

plt.plot(t, x, label="sin(t)")
plt.plot(t, 2 * x, label="2sin(t)")
plt.plot(t, 0.5 * x, label="0.5sin(t)")

plt.legend()
plt.grid(True)
plt.show()
""",

    "33_signal_shifting.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
original = np.sin(t)
shifted = np.sin(t - np.pi / 4)

plt.plot(t, original, label="Original")
plt.plot(t, shifted, label="Shifted")

plt.legend()
plt.grid(True)
plt.show()
""",

    "34_user_controlled_signal.py": """import numpy as np
import matplotlib.pyplot as plt

A = float(input("Amplitude: "))
f = float(input("Frequency: "))
duration = float(input("Duration: "))

t = np.linspace(0, duration, 1000)
signal = A * np.sin(2 * np.pi * f * t)

plt.plot(t, signal)
plt.title("Generated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
""",

    "35_scientific_calculator.py": """import numpy as np
import matplotlib.pyplot as plt

def matrix_add():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A + B)

def matrix_multiply():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A @ B)

def plot_sine():
    t = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(t, np.sin(t))
    plt.grid(True)
    plt.show()

def plot_cosine():
    t = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(t, np.cos(t))
    plt.grid(True)
    plt.show()

def statistics():
    A = np.random.randint(1, 100, 20)
    print("Mean =", np.mean(A))
    print("Max =", np.max(A))
    print("Min =", np.min(A))

while True:
    print("\\n1.Matrix Addition\\n2.Matrix Multiplication\\n3.Plot Sine\\n4.Plot Cosine\\n5.Statistics\\n0.Exit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        continue
    if choice == 1: matrix_add()
    elif choice == 2: matrix_multiply()
    elif choice == 3: plot_sine()
    elif choice == 4: plot_cosine()
    elif choice == 5: statistics()
    elif choice == 0: break
""",

    "36_ecg_signal.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 2000)
ecg = np.sin(2*np.pi*1*t) + 0.4*np.sin(2*np.pi*5*t) + 0.2*np.sin(2*np.pi*15*t)

plt.plot(t, ecg)
plt.title("Simple ECG Approximation")
plt.grid(True)
plt.show()
""",

    "37_fourier_square_wave.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.zeros_like(t)

for n in [1, 3, 5, 7, 9]:
    y += (1 / n) * np.sin(n * t)

y = (4 / np.pi) * y

plt.plot(t, y)
plt.title("Fourier Square Wave")
plt.grid(True)
plt.show()
""",

    "38_random_walk.py": """import numpy as np
import matplotlib.pyplot as plt

steps = np.random.choice([-1, 1], 1000)
walk = np.cumsum(steps)

plt.plot(walk)
plt.title("Random Walk")
plt.grid(True)
plt.show()
""",

    "39_image_as_matrix.py": """import numpy as np
import matplotlib.pyplot as plt

image = np.random.randint(0, 256, (256, 256))

plt.imshow(image, cmap="gray")
plt.title("Random Grayscale Image")
plt.colorbar()
plt.show()
""",

    "40_digital_oscilloscope.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
print("1.Sine\\n2.Cosine\\n3.Square\\n4.Exponential")
choice = int(input("Choice: "))

if choice == 1: y = np.sin(2 * np.pi * 5 * t)
elif choice == 2: y = np.cos(2 * np.pi * 5 * t)
elif choice == 3: y = np.sign(np.sin(2 * np.pi * 5 * t))
elif choice == 4: y = np.exp(-t)
else: exit()

plt.plot(t, y)
plt.grid(True)
plt.show()
""",

    "README.md": "# CSE220 Lab Framework (Problems 31-40)"
}

for filename, content in problems.items():
    with open(os.path.join(folder_name, filename), "w") as f:
        f.write(content)

with zipfile.ZipFile(f"{folder_name}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(folder_name, '..')))