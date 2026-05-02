import numpy as np

i_dim = int(input())
j_dim = int(input())

a = np.ones((i_dim, j_dim))
b = np.arange(1, i_dim+1).reshape((i_dim, 1))

c = a * b
print(c)