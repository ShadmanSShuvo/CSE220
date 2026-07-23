# Solution 1 (Boolean Indexing)
import numpy as np

A = np.arange(1, 101)

even = A[A % 2 == 0]

print(even)

# Using np.where
"""
even_indices = np.where(A % 2 == 0)
even_numbers = A[even_indices]
print(even_numbers)
"""
# Solution 2 (Slicing)
"""
import numpy as np

A = np.arange(1, 101)

print(A[1::2])

"""