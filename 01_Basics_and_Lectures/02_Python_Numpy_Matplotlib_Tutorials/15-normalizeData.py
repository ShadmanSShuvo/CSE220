import numpy as np

def normalize(x):
    return (x-np.min(x))/(np.max(x)-np.min(x))


A = np.array([15,20,35,40,50])

print(normalize(A))