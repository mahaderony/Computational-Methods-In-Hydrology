# HW 05 : Problem 01 Implicit code to solve the heat equation
import numpy as np
import matplotlib.pyplot as plt
# Parameters
D = 0.835
dt = 0.1
dx = 2
lamb = ((D * dt) / dx**2)
a = - lamb
print(a)
b = (1 + (2 * lamb))
print(b)
c = - lamb
print(c)
L = 10
l = np.arange(0, (L+dx), dx) # Length
# Boundary Condition
T = [100, 0, 0, 0, 0, 50] # Temperature
# Matrix
matrix = []
m = np.zeros(36).reshape(6, 6)
for i in range(6):
    for j in range(6):
        if (i+1) == j:
            m[i][j] = c
        elif (i-1) == j:
            m[i][j] = a
        elif i == j:
            m[i][j] = b
m[0][0] = 1
m[0][1] = 0
m[5][5] = 1
m[5][4] = 0
# After 3 seconds
for x in range(30):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T3 = t
print(T3)
plt.plot(l, T3, marker='o')
# After 6 seconds
for x in range(60):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T6 = t
print(T6)
plt.plot(l, T6, marker='x')
# After 9 seconds
for x in range(90):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T9 = t
print(T9)
plt.plot(l, T9, marker='v')
# After 120 seconds
for x in range(120):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T12 = t
print(T12)
plt.plot(l, T12, marker='^')
# Plotting
plt.xlabel('Distance (m)') # Labeling of X-Axis
plt.ylabel('Temperature degC') # Labeling of Y-axis
plt.title('Distance vs Temperature')
plt.legend(['t = 3', 't = 6', 't = 9', 't = 12'])
plt.show()