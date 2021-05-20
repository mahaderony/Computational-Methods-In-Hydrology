# HW 05 Problem 05 : Temporal Convergence
import numpy as np
import math
L = 100
runtime = 90
D = 10
dx = 20
dt = 45
lamb = ((D * dt) / (dx ** 2))
print('Lambda', lamb)
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
C[(length - 1)] = 11
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
Im[(length - 1)][(length - 1)] = 1
Im[(length - 1)][(length - 2)] = 0
# After 90 min
count = int(runtime / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 16
    C[5] = 11
T90 = t
print('Implicit\n', T90[(len(T90) - 2)])

# Explicit Solution
C = np.zeros(length)
for n in range(length):
    C[n] = 16
C[(length - 1)] = 11
count = int(runtime / dt)
xn = np.zeros(length)
for m in range(count):
    for i in range(1, 5):
        xn[i] = (C[i] + (lamb * (C[i - 1] - 2 * C[i] + C[i + 1])))
    xn[0] = 16
    xn[5] = 11
    C = xn
    xn = np.zeros(length)
print('Explicit\n', C[(len(C)-2)])

# Analytical Solution
T1 = 16
T2 = 11
Time = []
t = 1
count = int(runtime / dt)
for h in range(count):
    for x in range(0, (L + dx), dx):
        k = T1 + (((T2 - T1) * x) / L) + (2 / math.pi) * (sum(((((T2 - T1) * math.cos(n * math.pi)) / n)
                                                               * (math.sin((n * math.pi * x) / L) * (
            math.exp(((-D * (math.pi ** 2) * (n ** 2) * t) / (L ** 2)))))
                                                               for n in range(1, 50))))
        t = t + dt
        Time.append(k)
Ta90 = Time[(len(Time) - 6):len(Time)]
print('Analytical\n', Ta90[(len(T90)-2)])
# Crank-Nicolson
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
C = np.zeros(length)
for n in range(length):
    C[n] = 16
C[(length - 1)] = 11
dx = 20
dt = 45
T = np.zeros(length)
for x in range(count):
    for q in range(1, 5):
        T[q] = ((lamb * (C[q - 1] - (2 * C[q]) + C[q + 1])) + (2 * C[q]))
    T[0] = 16
    T[5] = 11
    t = (np.linalg.solve(Cr_m, T))
    C = T

Tcn90 = t
print('Crank-Nicolson\n', Tcn90)
