import numpy as np

def system_a(x):
    # Example: y[n] = x[n] + x[n-1] (Causal)
    return x + np.roll(x, 1)

def system_b(x):
    # Example: y[n] = x[n+1] (Non-Causal)
    return np.roll(x, -1)

def test_causality(system_func, N=10, split_point=5):
    # 1. Create two inputs that are identical up to split_point
    x1 = np.random.randn(N)
    x2 = x1.copy()
    x2[split_point:] = x2[split_point:] + 10.0 # Diverge in the future
    
    # 2. Pass both through the system
    y1 = system_func(x1)
    y2 = system_func(x2)
    
    # 3. Check if outputs match strictly before the split point
    # We slice up to split_point to see if future changes bled backward into the past
    is_causal = np.allclose(y1[:split_point], y2[:split_point])
    
    print(f"Outputs match in the past/present: {is_causal}")
    return is_causal

print("Testing System A (Causal):")
test_causality(system_a)

print("\nTesting System B (Non-Causal):")
test_causality(system_b)


def system_linear(x):
    return 3 * x  # y[n] = 3*x[n]

def system_nonlinear(x):
    return x ** 2  # y[n] = x^2[n]

def test_linearity(system_func, N=10):
    # 1. Generate random inputs and scaling constants
    x1 = np.random.randn(N)
    x2 = np.random.randn(N)
    a, b = 2.5, -1.8
    
    # 2. Path 1: Scale and mix inputs BEFORE the system
    y_path1 = system_func(a * x1 + b * x2)
    
    # 3. Path 2: Pass through system individually, then scale and mix AFTER
    y_path2 = a * system_func(x1) + b * system_func(x2)
    
    # 4. Compare the pathways
    is_linear = np.allclose(y_path1, y_path2)
    print(f"Superposition Holds: {is_linear}")
    return is_linear

print("Testing Linear System:")
test_linearity(system_linear)

print("\nTesting Non-Linear System:")
test_linearity(system_nonlinear)