import os
import zipfile

# Define the folder name
folder_name = "CSE220_Signals_Properties"
os.makedirs(folder_name, exist_ok=True)

# Problem scripts content mapping
problems = {
    "01_continuous_time.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
x = 3 * np.sin(2 * np.pi * t)

plt.plot(t, x)
plt.title("Continuous-Time Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
""",

    "02_discrete_time.py": """import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11)
x = 2 * n

plt.stem(n, x)
plt.title("Discrete-Time Signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.show()
""",

    "03_signal_addition.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x1 = np.sin(t)
x2 = np.cos(t)
x3 = x1 + x2

plt.plot(t, x1, label="sin")
plt.plot(t, x2, label="cos")
plt.plot(t, x3, label="sum")
plt.legend()
plt.grid(True)
plt.show()
""",

    "04_signal_multiplication.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(t) * np.cos(t)

plt.plot(t, x)
plt.title("Signal Multiplication")
plt.grid(True)
plt.show()
""",

    "05_time_shifting.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
x = np.sin(t)
shifted = np.sin(t - 2)

plt.plot(t, x, label="Original")
plt.plot(t, shifted, label="Shifted")
plt.legend()
plt.grid(True)
plt.show()
""",

    "06_time_scaling.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
plt.plot(t, np.sin(t), label="sin(t)")
plt.plot(t, np.sin(2*t), label="sin(2t)")
plt.legend()
plt.grid(True)
plt.show()
""",

    "07_time_reversal.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 1000)
original = np.exp(-t)
reversed_signal = np.exp(t)

plt.plot(t, original, label="x(t)")
plt.plot(t, reversed_signal, label="x(-t)")
plt.legend()
plt.grid(True)
plt.show()
""",

    "08_amplitude_scaling.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
x = np.cos(t)

plt.plot(t, x, label="Original")
plt.plot(t, 3*x, label="Scaled")
plt.legend()
plt.grid(True)
plt.show()
""",

    "09_even_odd_components.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 1000)
x = t**3 + t
x_neg = (-t)**3 + (-t)

xe = (x + x_neg) / 2
xo = (x - x_neg) / 2

plt.plot(t, xe, label="Even Part")
plt.plot(t, xo, label="Odd Part")
plt.legend()
plt.grid(True)
plt.show()
""",

    "10_unit_step.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
u = np.where(t >= 0, 1, 0)

plt.plot(t, u)
plt.title("Unit Step Signal")
plt.grid(True)
plt.show()
""",

    "11_unit_impulse.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 1000)
impulse = np.zeros_like(t)
impulse[500] = 1

plt.stem(t, impulse)
plt.title("Unit Impulse Approximation")
plt.grid(True)
plt.show()
""",

    "12_ramp_signal.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
r = np.where(t >= 0, t, 0)

plt.plot(t, r)
plt.title("Ramp Signal")
plt.grid(True)
plt.show()
""",

    "13_exponential_signal.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
x = np.exp(-2*t)

plt.plot(t, x)
plt.title("Exponential Signal")
plt.grid(True)
plt.show()
""",

    "14_signal_energy.py": """import numpy as np

x = np.array([1, 2, 3, 4])
energy = np.sum(x**2)
print("Energy =", energy)
""",

    "15_average_power.py": """import numpy as np

x = np.array([1, 2, 3, 4])
power = np.mean(x**2)
print("Average Power =", power)
""",

    "16_energy_power_check.py": """import numpy as np

x = np.array([2, 4, 6, 8])
energy = np.sum(x**2)
power = np.mean(x**2)

print("Energy =", energy)
print("Power =", power)
""",

    "17_square_wave.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
x = np.sign(np.sin(2 * np.pi * 5 * t))

plt.plot(t, x)
plt.title("Square Wave")
plt.grid(True)
plt.show()
""",

    "18_signal_comparison.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)

plt.plot(t, np.sin(t), label="sin")
plt.plot(t, np.cos(t), label="cos")
plt.plot(t, np.exp(-t), label="exp")
plt.plot(t, t, label="ramp")

plt.legend()
plt.grid(True)
plt.show()
""",

    "19_signal_transformation.py": """import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
x = np.sin(t)

plt.figure(figsize=(10, 6))
plt.plot(t, x, label="x(t)")
plt.plot(t, np.sin(t-2), label="x(t-2)")
plt.plot(t, np.sin(2*t), label="x(2t)")
plt.plot(t, 2*np.sin(t), label="2x(t)")
plt.plot(t, np.sin(-t), label="x(-t)")

plt.title("Signal Transformations")
plt.legend()
plt.grid(True)
plt.show()
""",

    "README.md": """# CSE220 Practice Problems: Signals and Their Properties

This directory contains standalone implementations of fundamental signal concepts commonly encountered in sessional labs.

## Topics Covered
1. Continuous vs. Discrete Time Signal representation (`plt.plot` vs `plt.stem`)
2. Arithmetic Signal operations (Addition, Multiplication)
3. Domain Transformations (Shifting, Scaling, Reversal, Even/Odd Extraction)
4. Fundamental Standard Waves (Step, Impulse approximation, Ramp, Exponential, Square)
5. Signal Metrics (Energy, Average Power)
"""
}

# Create files inside the directory
for filename, content in problems.items():
    file_path = os.path.join(folder_name, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Package directory into a zip file
zip_filename = f"{folder_name}.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(folder_name, '..')))

print(f"✓ Local setup completed. Generated bundle archive: '{zip_filename}'")