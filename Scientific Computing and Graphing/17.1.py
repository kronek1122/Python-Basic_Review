import numpy as np

# Exercise 1
A = np.arange(3,12).reshape(3,3)
print(A)

# Exercise 2
print(A.min())
print(A.max())
print(A.mean())

# Exercise 3
B = A**2
print(B)

# Exercise 4
C = np.vstack([A,B])
print(C)

# Exercise 5
print(C@A)

# Exercise 6
D = C.reshape(3,3,2)
print(D)
