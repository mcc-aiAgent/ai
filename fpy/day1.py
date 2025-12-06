import numpy as np

L = [[1, 2], [3, 4]]
A = np.array(L)
print(A)
z1 = np.ones((3, 3))
print(z1)
z2 = np.zeros((3, 4))
print(z2)
z3 = np.arange(10)
print(z3)
z4 = np.arange(2, 10)
print(z4)
z5 = np.arange(2, 10, 2)
print(z5)
del L, A

d1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
d11 = np.array(d1)
s1 = d11.shape
print(s1)
