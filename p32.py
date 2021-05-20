# HW 05 problem 06 Spatial Convergence Study:
import numpy as np
L = 100
Time = 90
D = 10
dx = 2.5
dt = 5
lamb = ((D * dt) / (dx ** 2))
node = int(80/dx)
# Implicit Matrix Coefficients
a = - lamb
b = (1 + (2 * lamb))
c = - lamb
# Crank-Nicolson Matrix Coefficients
d = - lamb
e = (2 + (2 * lamb))
f = - lamb
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
# Boundary Condition
C = np.zeros(length)
for n in range(length):
    C[n] = 16
C[(length-1)] = 11
# Implicit Solution
# Implicit Matrix
elements = (length ** 2)
Im = np.zeros(elements).reshape(length, length)
for i in range(length):
    for j in range(length):
        if (i + 1) == j:
            Im[i][j] = c
        elif (i - 1) == j:
            Im[i][j] = a
        elif i == j:
            Im[i][j] = b
Im[0][0] = 1
Im[0][1] = 0
Im[(length-1)][(length-1)] = 1
Im[(length-1)][(length-2)] = 0
count = int(Time / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
T90 = C
print('Implicit\n', T90[node])

# Explicit Solution
C = np.zeros(length)
for n in range(length):
    C[n] = 16
C[(length-1)] = 11
xn = np.zeros(length)
for m in range(count):
    for i in range(1, (length-1)):
        xn[i] = (C[i] + (lamb * ((C[i - 1]) - (2 * C[i]) + (C[i + 1]))))
        xn[0] = 16
        xn[(length-1)] = 11
    C = xn
    xn = np.zeros(length)
print('Explicit\n', C[node])
# Crank-Nicolson
C = np.zeros(length)
for n in range(length):
    C[n] = 16
C[(length-1)] = 11
T = np.zeros(length)
for q in range(1, (length-1), 1):
    T[q] = ((((C[q - 1] - (2 * C[q]) + C[q + 1]) / (dx ** 2)) * (2 * dt)) + (2 * (C[q])))
T[0] = 16
T[(length-1)] = 11
# Matrix
Cr_m = np.zeros(elements).reshape(length, length)
for i in range(length):
    for j in range(length):
        if (i + 1) == j:
            Cr_m[i][j] = f
        elif (i - 1) == j:
            Cr_m[i][j] = d
        elif i == j:
            Cr_m[i][j] = e
Cr_m[0][0] = 1
Cr_m[0][1] = 0
Cr_m[(length-1)][(length-1)] = 1
Cr_m[(length-1)][(length-2)] = 0
for x in range(count):
    t = (np.linalg.solve(Cr_m, T))
Tcn90 = t
print('Crank-Nicolson\n', Tcn90[node])