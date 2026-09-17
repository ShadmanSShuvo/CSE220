import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

print("Addition:")
print(A+B)

print("\nSubtraction:")
print(A-B)

print("\nElement-wise Multiplication:")
print(A*B)

print("\nMatrix Multiplication:")
print(A@B)

print("\nTranspose of A:")
print(A.T)

print("\nTranspose of B:")
print(B.T)