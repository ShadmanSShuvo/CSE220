Based on those two lectures, a CSE220 Sessional will likely test your ability to **write small scientific computing programs**, use **NumPy**, **matplotlib**, and apply **basic Python programming concepts** (conditions, loops, functions, user input).

Here are problems arranged by difficulty.

---

# Part A: Basic Python (Easy)

### 1. Calculator

Write a program that takes two numbers and an operator (`+`, `-`, `*`, `/`) from the user and prints the result.

**Concepts**

* input()
* if-elif-else
* arithmetic operators

---

### 2. Prime Number Checker

Take an integer from the user and determine whether it is prime.

---

### 3. Fibonacci Series

Generate the first `N` Fibonacci numbers.

Example:

```
Input:
10

Output:
0 1 1 2 3 5 8 13 21 34
```

---

### 4. Multiplication Table

Print the multiplication table of a given number up to 20.

---

### 5. Largest of Three Numbers

Find the largest among three numbers without using `max()`.

---

### 6. Factorial Using Function

Implement

```python
def factorial(n):
    ...
```

---

### 7. Temperature Converter

Create two functions

```
celsius_to_fahrenheit()
fahrenheit_to_celsius()
```

---

# Part B: NumPy Basics

### 8. Create Arrays

Create

* zeros array
* ones array
* identity matrix (5×5)
* random 4×4 matrix

Print all.

---

### 9. Matrix Operations

Take two 3×3 matrices.

Perform

* Addition
* Subtraction
* Element-wise multiplication
* Matrix multiplication

---

### 10. Statistics

Generate

```python
A = np.random.randint(1,100,20)
```

Find

* mean
* median
* maximum
* minimum
* standard deviation

---

### 11. Even Numbers

Generate

```
1 to 100
```

Extract only even numbers using NumPy.

---

### 12. Array Reshaping

Create

```
1 ... 36
```

Reshape into

```
6×6
```

Print

* first row
* last column
* diagonal

---

### 13. Matrix Transpose

Generate a random matrix.

Print

* original
* transpose

---

# Part C: Functions + NumPy

### 14. Signal Generator

Write

```python
def generate_signal(amplitude, frequency, t):
    ...
```

Return

```
A sin(2πft)
```

---

### 15. Normalize Data

Write

```python
def normalize(x):
    ...
```

Formula

[
\frac{x-\min(x)}{\max(x)-\min(x)}
]

---

### 16. Moving Average

Write a function

```python
moving_average(x, window)
```

---

# Part D: Matplotlib

### 17. Plot a Straight Line

Plot

[
y=2x+3
]

for

```
x=-10...10
```

Include

* title
* xlabel
* ylabel
* grid

---

### 18. Plot Multiple Graphs

Plot

```
sin(x)
cos(x)
```

on the same figure.

Include legend.

---

### 19. Quadratic Function

Plot

[
y=x^2
]

---

### 20. Exponential Function

Plot

[
y=e^x
]

---

### 21. Scatter Plot

Generate 100 random points.

Create a scatter plot.

---

### 22. Histogram

Generate

```
1000
```

random numbers from a normal distribution.

Plot histogram.

---

# Part E: Basic Signals

### 23. Unit Step Signal

Generate

[
u(t)
]

for

```
-5 ≤ t ≤ 5
```

Plot it.

---

### 24. Ramp Signal

Generate

[
r(t)=t,\quad t\ge0
]

otherwise 0.

---

### 25. Exponential Signal

Plot

[
e^{-t}
]

for

```
0≤t≤5
```

---

### 26. Sine Wave

Generate

```
Amplitude = 2

Frequency = 5 Hz

Time = 0 to 2 sec
```

Plot the signal.

---

### 27. Cosine Wave

Generate

```
A cos(2πft)
```

---

### 28. Square Wave (Without scipy)

Using

```python
np.sign(np.sin(...))
```

generate a square wave.

---

### 29. Compare Signals

Plot on the same graph

* sine
* cosine
* exponential

---

### 30. Noisy Signal

Generate

```
signal = sin(...)
noise = random noise
```

Plot

* original
* noisy

---

# Part F: Integrated Problems (Sessional Style)

### 31. Signal Statistics

Generate a sine wave.

Print

* maximum
* minimum
* average
* RMS value

Then plot it.

---

### 32. Signal Scaling

Generate

```
sin(t)
```

Also generate

```
2sin(t)

0.5sin(t)
```

Plot all together.

---

### 33. Signal Shift

Plot

```
sin(t)

sin(t−π/4)
```

---

### 34. User-Controlled Signal

Take from user

* amplitude
* frequency
* duration

Generate the signal.

Plot it.

---

### 35. Mini Scientific Calculator

Menu

```
1. Matrix Addition
2. Matrix Multiplication
3. Plot Sine
4. Plot Cosine
5. Statistics
```

Use functions for each option.

---

# Challenge Problems (Excellent Practice)

### 36. ECG-like Signal

Combine multiple sine waves with different frequencies to simulate a simple periodic waveform.

---

### 37. Fourier Approximation of a Square Wave

Approximate a square wave using the first few odd harmonics of a Fourier series.

---

### 38. Random Walk

Generate a 1D random walk and plot the path.

---

### 39. Image as Matrix

Create a random grayscale image using a 256×256 NumPy array and display it with `imshow()`.

---

### 40. Digital Oscilloscope Simulation

Allow the user to choose among sine, cosine, square, or exponential signals and display the selected waveform with proper labels and grid.

---

## Recommended Practice Order

1. Problems **1–7** (Python fundamentals)
2. Problems **8–16** (NumPy operations)
3. Problems **17–22** (Matplotlib basics)
4. Problems **23–30** (Signal generation and visualization)
5. Problems **31–35** (Integrated sessional-style programming)
6. Problems **36–40** (Advanced challenges)

If your course follows the typical CSE220 sessional pattern, being comfortable with problems **14, 17, 18, 23, 26, 31, 34, and 35** will prepare you well for most lab exams.
