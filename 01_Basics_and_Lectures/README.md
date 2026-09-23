# 01: Basics and Lecture Demonstrations

Foundational Python notebooks, NumPy drills, Matplotlib tutorials, and classroom lecture demonstrations for **CSE 220: Signals and Linear Systems Sessional**.

---

## Directory Architecture

| Folder | Focus Area | Description |
| :--- | :--- | :--- |
| [`01_Python_Basics/`](./01_Python_Basics/) | **Language & Environment Basics** | Python syntax, lists, dicts, NumPy array introduction, and Online 1 experiment setups. |
| [`02_Numpy_Matplotlib_Tutorials/`](./02_Numpy_Matplotlib_Tutorials/) | **Progressive Numerical Computing** | 45+ structured, numbered scripts covering Fibonacci, matrix operations, statistical calculations, ECG simulation, random walks, and digital oscilloscope simulations. |
| [`03_Numpy_Class_Demos/`](./03_Numpy_Class_Demos/) | **Classroom Demonstrations** | Live interactive plotting scripts: bar charts, scatter plots, square waves, and sampling rate visualizers. |
| [`04_Signals_Properties/`](./04_Signals_Properties/) | **Core Signal Operations** | 20 self-contained implementations of fundamental continuous and discrete signal properties (time shift, scale, reversal, unit step, ramp, energy, average power). |
| [`05_Lecture_01_Signals/`](./05_Lecture_01_Signals/) | **Lecture 1 Notes & Masks** | Advanced piecewise signal construction, manual and vectorized interpolation functions, and masking routines. |

---

## Key Learning Outcomes

1. **Vectorized Computing**: Replacing Python `for` loops with vectorized NumPy array broadcasting for maximum efficiency in signal calculations.
2. **Dual-Domain Plotting**: Using `matplotlib.pyplot.plot` for continuous signals and `matplotlib.pyplot.stem` for discrete sequences.
3. **Signal Operations**: Implementing standard signal transformations:
   $$y(t) = A \cdot x(\alpha t + \beta)$$
4. **Energy & Power**: Calculating total energy $E_\infty = \int |x(t)|^2 dt$ or $\sum |x[n]|^2$ and average power $P_\infty$.
