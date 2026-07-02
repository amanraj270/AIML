import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# print(arr1.sum())
# print(arr2.sum())
# print(arr2[1].sum())
# print(arr2)
# print(arr2.sum(axis=0))
# print(arr2.sum(axis=1))

# print(np.square(arr1))
# print(np.square(arr1[3]))
# print(np.square(arr2[2][2]))

# arr3 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(arr3[2][3] + 10)
# print(arr3[2][3] - 10)
# print(arr3[2][3] * 10)
# print(arr3[2][3] // 10)

# arr3 = np.array([1,2,3,4,5])
# arr4 = np.array([10,20,30,40,50])
# arr5 = arr3 + arr4
# print(arr5)

# Indexing and Slicing in NumPy
# a1 = np.array([1,2,3,4,5,6,7,8])

a2 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [3,4,5,6],
    [7,8,9,0],
    [1,2,5,4],
    [5,6,7,8]
])

# Iteration in NumPy
# for i in a1:
#     print(i)

# for i in a2:
#     print(i)
#     for j in i:
#         print(j)

# Stacking in NumPy
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,21,32,40,50])

vertical = np.vstack((arr1, arr2))
horizontal = np.hstack((arr1, arr2))

# Concatenate
# concat = np.concatenate((arr1, arr2))