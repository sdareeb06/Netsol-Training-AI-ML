# Numpy Arrays creating array

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# zeroes = np.zeros((2, 3))
# print(zeroes)

# rand = np.random.randint(1, 10, 5)
# print(rand)


# arr = np.array([6, 8 , 4, 7, 9])
# print(arr)

# ones = np.ones((3, 3))
# print(ones)

# rand = np.random.randint(1, 100, 4)
# print(rand)



# Array Attributes(shape, dtype, size, ndim)

# a = np.array([1, 2, 3], [4, 5, 6])

# print(a.shape)
# print(a.dtype)
# print(a.size)
# print(a.ndim)


n = np.array([[1, 2, 3], [4, 5, 6]])

print(n.shape)
print(n.dtype)
print(n.size)
print(n.ndim)

# n = np.array([[1.0, 0.2, 3.0], [4, 5, 6]] )

# print(n.dtype)


# Array Method(shap, max/min, argmax/argmin)

# b = np.array([3, 7, 1, 9, 4])

# print(b.reshape(5, 1))
# print(b.max(), b.min())
# print(b.argmax(), b.argmin())


# c = np.array([4, 5, 9, 2, 8, 3])
# print(c.reshape(2, 3))

# c = np.array([4, 5, 9, 2, 8, 3, 1, 7])
# print(c.max(), c.min())
# print(c.argmax(), c.argmin())


# Coping, Appending and inserting

# c = np.array([1, 2, 3])
# c_copy = c.copy()
# c_copy[0] = 99
# print(c, c_copy)


# d = np.array([1, 2, 3])
# print(np.append(d, [4, 5]))
# print(np.insert(d, 1, 100))


# v = np.array([1, 2, 3, 4, 5])
# v_copy = v.copy()
# v_copy[2] = 67
# print(v, v_copy)

# a = np.array([1,2,3,4,5])
# print(np.append(a, [6,5,9]))
# print(np.insert(a, 2, 88))


# Sorting, Delting, Combining and Splitting

# e = np.array([5,2,8,1])
# print(np.sort(e))
# print(np.delete(e,0))

# f1, f2 = np.array([1,2]), np.array([3,4])
# print(np.concatenate((f1, f2)))
# print(np.array_split(np.arange(1, 7), 3))

# z = np.array([4,5,2,6,9,1])
# print(np.sort(z))
# print(np.delete(z, 2))

# q1, q2 = np.array([1,2,3]), np.array([4,5,6])
# print(np.concatenate((q1,q2)))
# print(np.array_split(np.arange(1,7), 2))


# Data Loading and Saving

# arr = np.array([1,2,3,4])
# np.save('my_array.npy', arr)

# loaded = np.load('my_array.npy')
# print(loaded)

# Indexing and Selection (2D ,Logical)

# g = np.array([[1,2,3,], [4,5,6], [7,8,9]])

# print(g[1,2])
# print(g[g>5])

# g = np.array([[1,2,3,], [4,5,6],[7,8,9]])
# print(g)


# Broadcasting

# h = np.array([1,2,3])
# print(h + 10)

# d = np.array([3,4,5,6,7])

# print(d + 100)
# a = d * 3
# print(a - 1)


# i = np.array([1.5, 2.7, 3.1])
# print(i.astype(int))

# j = np.array([1,2,3])
# k =np.array([4,5,6])
# print(j+k, j-k, j*k)
# print(j/k, j**2)


# Typecasting

# i = np.array([4.5, 3.1, 6.8])
# print(i.astype(int))

# j = np.array([1,2,3,4])
# k =np.array([5,6,7,8])
# print(j+k, j-k, j*k)
# print(j/k, j**2)


# q = np.array([1,4,9,16])
# print(np.sqrt(q))

# m = np.array([45,60,90,180])
# print(np.sin(m))
