import numpy as np

# 1D Array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
print(type(arr))
print(arr.dtype)
print(arr.itemsize)
print(arr.shape)
print(arr.size)

# 2D Array
arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr2)
print(arr2.dtype)
print(arr2.shape)
print(arr2.size)
print(arr2.itemsize)

# arange examples
arr3 = np.arange(10)
print(arr3)

arr3 = np.arange(1, 10)
print(arr3)

arr3 = np.arange(1, 10, 2)
print(arr3)

# NumPy array creation and manipulation methods

a1 = np.array([1,2,3,4,5,6,7,8,9])

a2 = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])

a3 = np.arange(10)

a4 = np.arange(1,10)

a5 = np.arange(1,10,2)

a6 = np.zeros(10)

a6 = np.zeros((3,4))
print(a6)

a7 = np.ones(10)

a7 = np.ones((2,3))
print(a7)

a8 = np.empty(6)
print(a8)