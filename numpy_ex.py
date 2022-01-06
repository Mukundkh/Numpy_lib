import numpy as np

# numpy array
# 1d-array
a = np.array(23)

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

print(np.__version__)

# 2-d array
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# 3-d array
arr2 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]

    ]
])

print(arr1.ndim)
print(a.ndim)
print(arr2)

ab = np.array([1, 2, 3], ndmin=5)
print(ab)

#slicing

x = np.array([1,2,3,4,5])
print(x[2]+x[1])


y = np.array([
    [1,2,3],
    [4,5,6]
])
print(y[1,2])

arrx = np.array([
    [1,2,3],
    [4,5,6]
])
print(arrx[-1,-1])

first = np.array([1,2,3,4,5,6])
print(first[1::2])

second = np.array([1,2,3,4,5,66,7])
print(second[3:])
print(second[-3:-1])

sec_d = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(sec_d[1, 1:4])
