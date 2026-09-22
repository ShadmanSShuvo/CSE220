# CSE 220: Signals & Systems Coding Reference Library (Mahdi)

This directory contains senior student (Mahdi) reference code, Python & NumPy tutorials, beginner problem sets, and core signal coding challenges.

---

## Directory Organization

```text
CSE220_Signals_and_Systems_Codes/
├── README.md                            # Complete module guide & problem index
├── 01_Basic_Python/                     # Core Python & NumPy tutorials & notebooks
│   ├── basic.py                         # Language basics (conditionals, loops, functions)
│   ├── basic2.py                        # Array manipulation & math drills
│   ├── numpy_basic.py                   # Vectorized operations & matrix slicing
│   ├── matplotlib_basic.py              # 2D continuous & stem plotting
│   ├── signal_plotting.ipynb            # Jupyter notebook for signal visualization
│   └── basic_python_notebook.ipynb      # Interactive Python foundations notebook
│
├── 02_Beginner_Problems/                # 10 Beginner signal manipulation problems
│   ├── Beginner_Problems.pdf            # Problem specifications (P01–P10)
│   ├── Beginner_Solutions.pdf           # Detailed mathematical solutions
│   ├── templates/                       # Starter code templates (P01–P10)
│   ├── solutions/                       # Reference solutions (P01–P10)
│   └── my_solves/                       # Student implementations (solve_1–solve_10)
│
├── 03_Coding_Problems/                  # 10 Core CSE219/220 coding problems
│   ├── CSE219_Signals_Coding_Problems_with_Solutions.pdf
│   ├── templates/                       # Starter templates (P01–P10)
│   ├── solutions/                       # Reference solutions (P01–P10)
│   └── my_solutions/                    # Student implementations (solve_1–solve_8)
│
└── 04_Reference_PDFs/                   # Syntax cheatsheets & plot reference guides
    ├── NumPy_Matplotlib_Cheatsheet.pdf  # Quick reference table for NumPy & Matplotlib
    ├── NumPy_Matplotlib_Function_Reference.pdf # Comprehensive API function reference
    ├── matplotlib_plot_reference.pdf    # Plot styling, subplots, and colors reference
    └── Latex_Sources/                   # Source LaTeX (.tex) files
```

---

## Highlights of Problem Sets

### 1. `02_Beginner_Problems/`
Focuses on fundamental signal definitions and basic transformations:
- Unit step, unit impulse, continuous ramp signal.
- Basic signal arithmetic (addition, multiplication).
- Discrete time-shifting ($x[n - k]$) and scaling.

### 2. `03_Coding_Problems/`
Focuses on rigorous analytical & computational signal properties:
- Continuous & discrete even/odd decomposition.
- Numerical calculation of continuous signal energy ($E_\infty = \int |x(t)|^2 dt$) and cross-energy.
- Average power computation over one period and $K$ periods for periodic signals.
- Step-by-step composite transformations ($y(t) = x(\alpha t + \beta)$).
