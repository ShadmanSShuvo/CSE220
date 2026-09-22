# 04: Major Programming Assignments (Offlines)

This directory contains the major programming assignments (**Offlines**) completed for **CSE 220: Signals and Linear Systems Sessional**. Each offline involves implementing computational algorithms from scratch, verifying theoretical properties, and applying signal processing methods to real-world data (audio, 2D vector graphics, and images).

---

## Assignment Overview

| Offline | Topic | Core Deliverables | Techniques & Libraries |
| :--- | :--- | :--- | :--- |
| [**Offline 01: Convolution**](./Offline_01_Convolution/) | Discrete LTI Systems & 1D/2D Convolution | `DiscreteSignal` class, `LTISystem` simulation, 1D convolution, spatial 2D matrix convolution | NumPy, Matplotlib, OOP |
| [**Offline 02: FS & CFT**](./Offline_02_FS_and_CFT/) | Fourier Series Epicycles & 2D CFT Edge Detection | **Task 1:** Complex exponential Fourier Series animating SVG contours.<br>**Task 2:** 2D Continuous Fourier Transform edge detection on images. | Numerical integration (`np.trapezoid`), complex analysis, PIL |
| [**Offline 03: DFT & FFT**](./Offline_03_DFT_and_FFT/) | Fast Fourier Transform Algorithms & BigInt Mul | Radix-2 Cooley-Tukey FFT, Bluestein Arbitrary-Length FFT, $O(N \log N)$ Big Integer Multiplication, 2D Image frequency filtering | Custom FFT engines, bench testing, frequency domain convolution |

---

## Directory Conventions

Each offline folder is organized into clean functional workspaces:
- `starter/`: Original instructor-provided starter code and assignment PDF specifications.
- `submission/` or `v2_final/`: Official tested assignment submissions for Roll `2305025`.
- `archives/`: Packaged submission archives (`.zip`) and development drafts.
