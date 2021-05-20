# HW 05 : Problem 03
import numpy as np
import matplotlib.pyplot as plt
import math
# Parameters
D = 10
dt = 10
dx = 10
lamb = ((D * dt) / (dx**2))
a = - lamb
b = (1 + (2 * lamb))
c = - lamb
L = 100 # Length
l = np.arange(0, (L+dx), dx)
print(l) # Length
# Boundary Condition
T = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11] # Temperature
# Matrix
matrix = []
m = np.zeros(121).reshape(11, 11)
for i in range(11):
    for j in range(11):
        if (i+1) == j:
            m[i][j] = c
        elif (i-1) == j:
            m[i][j] = a
        elif i == j:
            m[i][j] = b
m[0][0] = 1
m[0][1] = 0
m[10][10] = 1
m[10][9] = 0
print(m)
# After 10 seconds (Numerical)
for x in range(1):
    t = (np.linalg.solve(m, T))
Tn10 = t
print(Tn10)
plt.plot(l, Tn10, marker='o')
# After 10 seconds (Analytical)
T1 = 16
T2 = 11
Time = []
for t in range(0, 510, 10):
    for x in range(0, 110, 10):
        k = T1 + (((T2-T1)*x)/L) + (2/math.pi) * (sum(((((T2 - T1) * math.cos(n * math.pi)) / n)
            * (math.sin((n * math.pi * x) / L) * (math.exp(((-D * (math.pi ** 2) * (n ** 2) * t) / (L ** 2)))))
                                                       for n in range(1, 50))))
        Time.append(k)
Ta10 = Time[0:11]
print(Ta10)
plt.plot(l, Ta10, marker='x')
# Plotting
plt.xlabel('Distance (m)') # Labeling of X-Axis
plt.ylabel('Temperature degC') # Labeling of Y-axis
plt.title('Distance vs Temperature')
plt.legend(['Implicit Numerical t = 10', 'Analytical t = 10'])
plt.show()