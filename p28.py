# HW 05 : Problem 02
import numpy as np
import matplotlib.pyplot as plt
# Parameters
D = 0.49
dt = 6
dx = 2
lamb = ((D * dt) / dx**2)
a = - lamb
b = (1 + 2 * lamb)
c = - lamb
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
# After 6 seconds
for x in range(1):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T6 = t
print(T6)
plt.plot(l, T6, marker='o')
# After 12 seconds
for x in range(2):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T12 = t
print(T12)
plt.plot(l, T12, marker='x')
# After 18 seconds
for x in range(3):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T18 = t
print(T18)
plt.plot(l, T18, marker='v')
# After 24 seconds
for x in range(4):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T24 = t
print(T24)
plt.plot(l, T24, marker='^')
# After 30 seconds
for x in range(5):
    t = (np.linalg.solve(m, T))
    T = t
    T[0] = 100
    T[5] = 50
T30 = t
print(T30)
plt.plot(l, T30, marker='<')
# Plotting
plt.xlabel('Distance (m)') # Labeling of X-Axis
plt.ylabel('Temperature degC') # Labeling of Y-axis
plt.title('Distance vs Temperature')
plt.legend(['t = 6', 't = 12', 't = 18', 't = 24', 't = 30'])
plt.show()