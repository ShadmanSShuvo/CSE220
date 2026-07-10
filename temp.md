Here is the complete implementation for Question Set 6, providing the mathematical energy/power metrics, system definitions, a clean property classification table, and automated computational checks to verify the properties.
Part A — Energy and Power Implementation
Python
import numpy as np

def energy(x: np.ndarray) -> float:
    """Returns the total energy of the signal: sum(|x[n]|^2)."""
    return float(np.sum(np.abs(x) ** 2))

def average_power(x: np.ndarray) -> float:
    """Returns the average power: total energy divided by the number of samples."""
    return energy(x) / len(x)

# Quick verification test
x_sample = np.array([-2.0, 1.0, 3.0, 0.5])
expected_energy = (-2.0)**2 + (1.0)**2 + (3.0)**2 + (0.5)**2  # 4 + 1 + 9 + 0.25 = 14.25
assert np.isclose(energy(x_sample), expected_energy), "Energy calculation error!"
print(f"Part A Verification passed. Energy: {energy(x_sample)}, Power: {average_power(x_sample):.4f}\n")
Part B — System Classifications & Justifications
System	Linear / Nonlinear	Time-Invariant / Time-Varying	Causal / Non-causal	One-Line Justification
y[n]=x[n]−x[n−1]	Linear	Time-Invariant	Causal	Depends strictly on present and past inputs with constant weights.
y[n]=n⋅x[n]	Linear	Time-Varying	Causal	The time index scaling factor n explicitly alters behavior over time.
y[n]=x[n] 
2
 	Nonlinear	Time-Invariant	Causal	Squaring elements violates scaling: T{a⋅x}=a 
2
 x 
2
 

=a⋅T{x}.
y[n]=x[n]+5	Nonlinear	Time-Invariant	Causal	Fails the zero-input requirement: a zero input produces a non-zero output (5).
y[n]= 
2
1
​	
 (x[n−1]+x[n]+x[n+1])	Linear	Time-Invariant	Non-causal	Look-ahead property: calculating y[n] requires the future input sample x[n+1].
y[n]=x[−n]	Linear	Time-Varying	Non-causal	Time-reversed mapping relies on future indices for all negative time slots (n<0).
Python Code & Computational Verification
This architecture defines the six systems and runs mathematical tests to verify the verdicts.
Note: For boundary consistency in shifting operations, arrays are padded with zeros or sliced symmetrically to prevent out-of-bounds mapping errors.
Python
import numpy as np

# --- 1. System Definitions ---

def system_1(x: np.ndarray, n: np.ndarray) -> np.ndarray:
    # y[n] = x[n] - x[n-1]. (Safe manual shift, filling index -1 with 0)
    x_minus_1 = np.concatenate(([0.0], x[:-1]))
    return x - x_minus_1

def system_2(x: np.ndarray, n: np.ndarray) -> np.ndarray:
    # y[n] = n * x[n]
    return n * x

def system_3(x: np.ndarray, n: np.ndarray) -> np.ndarray:
    # y[n] = x[n]^2
    return x ** 2

def system_4(x: np.ndarray, n: np.ndarray) -> np.ndarray:
    # y[n] = x[n] + 5
    return x + 5.0

def system_5(x: np.ndarray, n: np.ndarray) -> np.ndarray:
    # y[n] = 0.5 * (x[n-1] + x[n] + x[n+1])
    x_minus_1 = np.concatenate(([0.0], x[:-1]))
    x_plus_1 = np.concatenate((x[1:], [0.0]))
    return 0.5 * (x_minus_1 + x + x_plus_1)

def system_6(x: np.ndarray, n: np.ndarray) -> np.ndarray:
    # y[n] = x[-n] (Assumes symmetric window centered at index 8)
    return x[::-1]


# --- 2. Computational Verification Engine ---

def verify_properties(sys_func, name):
    # Setup test vectors over symmetric domain n = -8...8 (length 17)
    n = np.arange(-8, 9)
    x1 = np.sin(n)
    x2 = np.cos(n)
    a, b = 2.0, -3.5
    
    # Check Linearity: T{a*x1 + b*x2} == a*T{x1} + b*T{x2}
    out_combined = sys_func(a * x1 + b * x2, n)
    out_separated = a * sys_func(x1, n) + b * sys_func(x2, n)
    is_linear = np.allclose(out_combined, out_separated, atol=1e-7)
    
    # Check Time-Invariance (Approximate check using center region to minimize window boundaries)
    # Shifting input by 1 slot right:
    x_shifted = np.concatenate(([0.0], x1[:-1]))
    out_of_shifted = sys_func(x_shifted, n)
    # Shifting original output by 1 slot right:
    out_original = sys_func(x1, n)
    shifted_out = np.concatenate(([0.0], out_original[:-1]))
    # Compare inner window segments to ignore boundary padding variations
    is_time_invariant = np.allclose(out_of_shifted[2:-2], shifted_out[2:-2], atol=1e-7)
    
    print(f"[{name}] Linearity Check passed: {is_linear} | Time-Invariance Check passed: {is_time_invariant}")

# Run Verifications
systems = [
    (system_1, "System 1: x[n] - x[n-1]"),
    (system_2, "System 2: n * x[n]      "),
    (system_3, "System 3: x[n]^2         "),
    (system_4, "System 4: x[n] + 5       "),
    (system_5, "System 5: Centered Avg   "),
    (system_6, "System 6: x[-n]          ")
]

print("--- Executing Verifications ---")
for sys, name in systems:
    verify_properties(sys, name)