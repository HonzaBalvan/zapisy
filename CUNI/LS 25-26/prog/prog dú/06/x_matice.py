import numpy as np

i_dim = int(input())
j_dim = int(input())
cislo = int(input())

a = np.ones((i_dim, j_dim))

print(a * cislo)