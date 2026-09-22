import numpy as np

print(np.__version__)

arr = np.array(10)
arr2 = np.array([0,1,2,3,4,5,6,7,8,9,10])

lst = [12,34,45,21] # ei list contiguos memory te thake na

arr3 = np.array(lst) # numpy er list contiguous memory te thake
arr4 = np.array([ [12,13,14], [25,24,26] ]) #First row three element, second row must have three
print(arr4.shape)
arr5 = np.array([ [12,13,14], [25,24,26] ], ndmin=3)
print(arr5.shape)
print(arr4)
print(type(arr))
print(arr4.ndim) #How many dimension
print(arr5[0][0][1])
print(arr5[0,0,2]) #Comma can be used to access as well
print(arr5[-1,-1,-1])
print("Array 2 from 3 to 8: ")
print(arr2[3:8:2])

arr6 = np.array([[4,5,6],[6,7,8],[10,11,12]])
print(arr6[::,1])
print(arr6[-1,1:3])
print(arr6[:2, 1:3])

arr7 = np.array([1,2,3] , dtype='S') #String data type
print(arr7)

arr6 = arr6.astype(float)
print(arr6)

arr8 = arr6.copy() #array 8 and array 6 will have different memory address
print(arr8)

arr9 = arr6.view() #Duijon eki memory address e point
arr6[0,0]=90
print(arr9[0,0])

print("Base of array 8" , arr8.base)
print("Base of array 9", arr9.base)

print(arr8.shape)

arr10 = arr8.reshape(1,3,1,3)
print(arr10)

arr11 = arr9.flatten() #Comma diyeo one dimension e jawa jay, eta extra function
print(arr11)

for r in np.nditer(arr10):
    print(r)

ones = np.ones(10)
print(ones)
zeros = np.zeros(10)
empty = np.empty(10) #random value diye hbe
arr11 = arr6.transpose()
print(arr11)
arr12 = arr6.T
tr = np.transpose(arr6)

arr13 = np.concatenate((arr6,arr12))
print(arr13)
print('------------------------------------------')
arr14 = np.vstack((arr6,arr12))
print(arr14)

arr15 = (arr2>=4)
print(arr15)

arr16 = arr2[arr15]
print(arr16)
