import os
import zipfile

# Define the directory name
dir_name = "CSE220_Sessional_Part3"
os.makedirs(dir_name, exist_ok=True)

# Dictionary containing filename and file content
problems = {
    "21_scatter.py": '''import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
''',

    "22_histogram.py": '''import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
''',

    "23_unit_step.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
u = np.where(t >= 0, 1, 0)

plt.plot(t, u)
plt.title("Unit Step Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "24_ramp.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 1000)
r = np.where(t >= 0, t, 0)

plt.plot(t, r)
plt.title("Ramp Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "25_exponential.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)
x = np.exp(-t)

plt.plot(t, x)
plt.title("Exponential Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "26_sine.py": '''import numpy as np
import matplotlib.pyplot as plt

A = 2
f = 5
t = np.linspace(0, 2, 1000)
x = A * np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "27_cosine.py": '''import numpy as np
import matplotlib.pyplot as plt

A = 3
f = 2
t = np.linspace(0, 2, 1000)
x = A * np.cos(2 * np.pi * f * t)

plt.plot(t, x)
plt.title("Cosine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "28_square.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
f = 5
square = np.sign(np.sin(2 * np.pi * f * t))

plt.plot(t, square)
plt.title("Square Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "29_compare.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)

plt.plot(t, np.sin(t), label="sin")
plt.plot(t, np.cos(t), label="cos")
plt.plot(t, np.exp(-t), label="exp(-t)")

plt.title("Signal Comparison")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
''',

    "30_noisy_signal.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1000)
signal = np.sin(2 * np.pi * 5 * t)
noise = 0.3 * np.random.randn(len(t))
noisy = signal + noise

plt.plot(t, signal, label="Original")
plt.plot(t, noisy, label="Noisy")
plt.legend()
plt.title("Original vs Noisy Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
''',

    "bonus_subplots.py": '''import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(t, np.sin(t))
plt.title("Sine")

plt.subplot(2, 1, 2)
plt.plot(t, np.cos(t))
plt.title("Cosine")

plt.tight_layout()
plt.show()
''',

    "README.md": '''# CSE220 Sessional Solutions – Part 3 (Problems 21–30)

## Important Signal Formulas
| Signal | Formula |
| :--- | :--- |
| **Sine** | `A * np.sin(2 * np.pi * f * t)` |
| **Cosine** | `A * np.cos(2 * np.pi * f * t)` |
| **Exponential** | `np.exp(-t)` |
| **Unit Step** | `np.where(t >= 0, 1, 0)` |
| **Ramp** | `np.where(t >= 0, t, 0)` |
| **Square** | `np.sign(np.sin(...))` |
'''
}

# Write files into the directory
for filename, content in problems.items():
    file_path = os.path.join(dir_name, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Zip the directory
zip_name = f"{dir_name}.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(dir_name, '..')))

print(f"✓ Created folder: '{dir_name}'")
print(f"✓ Generated archive: '{zip_name}' containing all 10 problems + bonus.")