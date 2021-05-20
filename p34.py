import numpy as np
import matplotlib.pyplot as plt
L = 1500
T = 20
dx = 100
dt = 1
S = 0.15
w = 0.005479452
runtime = [100, 200, 500, 750, 1000, 1500, 2000, 2500, 4500]
recharge = (w * dt) / S
lamb = ((T * dt) / ((dx ** 2) * S))
# Implicit Matrix Coefficients
a = - lamb
b = (1 + (2 * lamb))
c = - lamb
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
# Boundary Condition
C = np.zeros(length)
for n in range(length):
    C[n] = 29 + recharge
C[(length - 1)] = 29 + recharge
C[0] = 29
C[(length - 1)] = 29
print(C)
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
# Data calculation
for i in range(len(runtime)):
    count = int(runtime[i] / dt)
    for x in range(count):
        t = (np.linalg.solve(Im, C))
        C = t
        C[0] =100
        C[(length - 1)] = 29
        H100 = t
print('Implicit\n', H100)
plt.plot(l, H100, marker='o')
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Head in m')  # Labeling of Y-axis
plt.title('Distance vs Head')
plt.legend(['Head after 10 days','Head after 20 days','Head after 40 days','Head after 80 days'])
plt.show()
