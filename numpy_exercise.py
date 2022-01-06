import numpy as np
a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(b)

#dimension of n-d array
print(a.ndim)

#shape of numpy array
print(b.shape)
print(a.dtype)

#total size of array
print(a.nbytes)

#get total number of elements
print(a.nbytes)

##########
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

print(a[0, 1:-1:2])

a[1,5] = 20

a[:,2] = [1,2]
print(a)


#3-d example
# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)

# print(b[0,1,1])
# # b[:,1,:] = [[9,9,9],[8,8]]
# print(b)


#Different types of array
print(np.zeros((2,3)))
print(np.ones((4,2,2), dtype='int32'))

print(np.full((2,2), 99))

print(np.full_like(a, 4))

#random decimal numbers
print(np.random.rand(4,2))

print(np.identity(5,5))

#Repeating an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:-1,1:-1] = z
print(output)


#Mathematical and statistics functions
a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a,b)

# Find the determinant
c = np.identity(3)
np.linalg.det(c)

stats = np.array([[1,2,3],[4,5,6]])
stats

#Vertical stacking of vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v1,v2])

#horizontal stacking of vectors
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))



