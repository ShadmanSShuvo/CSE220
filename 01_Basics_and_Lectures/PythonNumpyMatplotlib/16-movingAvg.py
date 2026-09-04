import numpy as np

def moving_average(x, window):

    result = []

    for i in range(len(x)-window+1):

        avg = np.mean(x[i:i+window])

        result.append(avg)

    return np.array(result)


A = np.array([2,4,6,8,10])

print(moving_average(A,3))