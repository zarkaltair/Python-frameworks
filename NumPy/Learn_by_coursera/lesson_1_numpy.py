import numpy as np


# generate random matrix size 1000 rows and 50 columns
# loc - mean normal distribution
# scale - normal distribution standard deviation
x = np.random.normal(loc=1, scale=10, size=(1000, 50))
print(x)


# axis=0 columns, axis=1 rows
# mean value to columns
m = np.mean(x, axis=0)
# std - standart deviation
std = np.std(x, axis=0)
# matrix normalization
x_norm = ((x - m) / std)
print(x_norm)


# operation on matrix elements
z = np.array([[4, 5, 0],
			 [1, 9, 3],
			 [5, 1, 1],
			 [3, 3, 3],
			 [9, 9, 9],
			 [4, 7, 1]])
# line numbers for a given matrix, the sum of elements in which > 10
r = np.sum(z, axis=1)
print(np.nonzero(r > 10))


# concatenate matrix
# generate single matrix
a = np.eye(3)
b = np.eye(3)
print(a)
print()
print(b)
print()
# function for vertical docking matrices
ab = np.vstack((a, b))
print(ab)