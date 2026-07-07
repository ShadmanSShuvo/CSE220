For an **Online 1: Signals and their Properties** exam, Python is excellent for generating, transforming, and analyzing signals. Below are progressively challenging problem ideas that cover **causality, linearity, time invariance, time/phase shift, reversal, scaling, even/odd decomposition, energy/power, and periodicity**.

---

# 1. Signal Generation (Easy)

### Problem

Generate the following signals for
[
n=-10,\ldots,10
]

* Unit impulse
* Unit step
* Ramp
* Exponential
* Sinusoid

### Python Concepts

* NumPy
* matplotlib

### Learning Outcome

Understanding basic signal definitions.

---

# 2. Time Shift

### Problem

Given

[
x[n]=\sin(0.3\pi n)
]

Plot

* (x[n])
* (x[n-3])
* (x[n+2])

Explain which is delay and which is advance.

### Extension

Take shift value from user input.

---

# 3. Time Reversal

### Problem

Given

[
x[n]=n,\quad -5\le n\le5
]

Generate

[
x[-n]
]

Plot both.

---

# 4. Time Scaling

### Problem

Given discrete signal

[
x[n]
]

Generate

* (x[2n])
* (x[n/2])

Discuss why interpolation is required.

(Useful for conceptual understanding.)

---

# 5. Amplitude Scaling

### Problem

Generate

[
y[n]=3x[n]
]

Compare original and scaled signal.

---

# 6. Even and Odd Decomposition

### Problem

Given any signal,

Find

[
x_e[n]=\frac{x[n]+x[-n]}2
]

and

[
x_o[n]=\frac{x[n]-x[-n]}2
]

Verify

[
x=x_e+x_o
]

---

# 7. Signal Energy and Power

### Problem

Compute

Energy

[
E=\sum |x[n]|^2
]

Power

[
P=\frac1N\sum |x[n]|^2
]

Test on

* finite pulse
* sine wave
* exponential

---

# 8. Periodicity Check

### Problem

Generate

[
x[n]=\sin(0.2\pi n)
]

Determine experimentally whether it is periodic.

Then test

[
x[n]=\sin(\sqrt2,n)
]

Discuss why it is not periodic.

---

# 9. Phase Shift

### Problem

Plot

[
\sin(\omega n)
]

and

[
\sin(\omega n+\pi/4)
]

Observe phase difference.

---

# 10. Linear Combination

### Problem

Generate

[
y[n]=2x_1[n]-3x_2[n]
]

where

* (x_1=\sin())
* (x_2=\cos())

Plot all signals.

---

# 11. Causality Test (Theory + Python)

### Problem

Consider

[
y[n]=x[n]+x[n-2]
]

Is it causal?

Now consider

[
y[n]=x[n+1]
]

Is it causal?

Write Python code to simulate outputs.

---

# 12. Linearity Verification

### Problem

Let

[
T(x)=2x
]

Verify

[
T(ax_1+bx_2)=aT(x_1)+bT(x_2)
]

using random signals.

Then test

[
T(x)=x^2
]

Show that it is not linear.

---

# 13. Time Invariance Verification

### Problem

Given

[
T(x[n])=x[n]+x[n-1]
]

Verify

[
T(x[n-k])=y[n-k]
]

using Python.

Then test

[
T(x[n])=nx[n]
]

Show that it is time-varying.

---

# 14. Build a Signal Transformation Tool

### Problem

User enters

```
1. Shift
2. Reverse
3. Scale
4. Phase Shift
5. Amplitude Scale
```

Program displays transformed signal.

Good mini-project.

---

# 15. Interactive Signal Playground

### Problem

Use sliders (matplotlib widgets or ipywidgets) for

* amplitude
* frequency
* phase
* shift

Update signal in real time.

Excellent visualization exercise.

---

# 16. Compare Multiple Operations

### Problem

Given

[
x[n]
]

Generate all of these:

* Original
* Delayed
* Advanced
* Reversed
* Scaled
* Shifted + Reversed
* Shifted + Scaled

Display all in one figure for comparison.

---

# 17. Random Signal Property Quiz (Fun Practice)

Generate a random transformation and ask the user:

```
Operation performed:

x[n] → x[n-5]

Answer:

A. Delay
B. Advance
C. Reversal
D. Scaling
```

Python checks the answer automatically.

---

# 18. System Property Checker (Best Practice Problem)

### Problem

Given a system definition, determine whether it is:

* Causal
* Linear
* Time Invariant

Examples:

| System             | Causal | Linear | Time Invariant |   |   |
| ------------------ | ------ | ------ | -------------- | - | - |
| (y[n]=x[n]+x[n-1]) | ✔      | ✔      | ✔              |   |   |
| (y[n]=x[n+1])      | ✘      | ✔      | ✔              |   |   |
| (y[n]=nx[n])       | ✔      | ✔      | ✘              |   |   |
| (y[n]=x^2[n])      | ✔      | ✘      | ✔              |   |   |
| (y[n]=             | x[n]   | )      | ✔              | ✘ | ✔ |
| (y[n]=x[-n])       | ✘      | ✔      | ✘              |   |   |

Write Python functions to numerically verify linearity and time invariance for sample input signals, then compare the computed results with the theoretical classification.

---

## Recommended progression for an Online 1

1. Signal generation
2. Time shift
3. Time reversal
4. Amplitude scaling
5. Phase shift
6. Even/odd decomposition
7. Energy and power
8. Causality test
9. Linearity verification
10. Time invariance verification
11. Combined signal transformations
12. Interactive signal transformation tool (mini project)

This sequence builds from basic signal manipulation to system-property verification and is well suited for an introductory **Signals and Systems** programming assignment using Python.
