import numpy as np

A = np.arange(1, 37)

A = A.reshape(6,6)

print("Matrix:")
print(A)

print("\nFirst Row:")
print(A[0])

print("\nLast Column:")
print(A[:, -1])

print("\nDiagonal:")
print(np.diag(A))