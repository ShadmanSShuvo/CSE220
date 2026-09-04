import numpy as np

print(np.__version__)

arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)
print(arr4.shape)
print(type(arr4))
print(arr4.ndim)
print(arr4[0][0])
print(arr4[0, 0])

arr5 = np.array([[1, 2, 3], [4, 5, 6]], ndmin=3)
print(arr5)
print(arr5.shape)
print(type(arr5))
print(arr5.ndim)

arr6 = np.array([1, 2, 3], dtype=complex)
print(arr6)

arr7 = np.array([1, 2, 3], dtype=bool)
print(arr7)

arr8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr8)

tr = np.transpose(arr8)
print(tr)