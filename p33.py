# HW 05 Problem 07 : No Flow BC
import numpy as np
import matplotlib.pyplot as plt
L = 100
Time = [10, 20, 40, 80, 160, 250, 500]
D = 10
dx = 10
dt = 5
lamb = ((D * dt) / (dx ** 2))
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
C[0] = 100
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
Im[(length-1)][(length-1)] = (1+2*lamb)
Im[(length-1)][(length-2)] = (-2*lamb)
# After 10 min
count = int(Time[0] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T10 = t
plt.plot(l, T10, marker = 'v')
# After 20 min
count = int(Time[1] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T20 = t
plt.plot(l, T20, marker = '*')
# After 40 min
count = int(Time[2] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T40 = t
plt.plot(l, T40, marker = '+')
# After 80 min
count = int(Time[3] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T80 = t
plt.plot(l, T80, marker = 'D')
# After 160 min
count = int(Time[4] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T160 = t
plt.plot(l, T160, marker = 'o')
# After 250 min
count = int(Time[5] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T250 = t
plt.plot(l, T250, marker = '.')
# After 500 min
count = int(Time[6] / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T500 = t
plt.plot(l, T500, marker = 's')
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Temperature (degC)')  # Labeling of Y-axis
plt.title('Distance vs Temperature')
plt.legend(['t = 10', 't = 20', 't = 40', 't = 80', 't = 160', 't = 250', 't = 500'])
plt.show()