# Problem 08 : Matrix Multiplication
import numpy as np
# Initialize matrixA
R = int(input("Enter the number of rows for matA:"))
C = int(input("Enter the number of columns for matB:"))
matA = []
print("Enter the entries of matA row wise:")
# For user input matA
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matA.append(a)
# Initialize matrixB
P = int(input('Enter the number of rows of matB'))
Q = int(input('Enter the number of columns of matB'))
matB = []
print("Enter the entries of matB row wise:")
# For user input matB
for m in range(P):  # A for loop for row entries
    b = []
    for n in range(Q):  # A for loop for column entries
        b.append(int(input()))
    matB.append(b)
    print()
# Matrix Multiplication
if C == P:
    print('matA * matB =', np.dot(matA, matB))
else:
    print('Dimension error')