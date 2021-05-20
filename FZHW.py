# Problem 04:
import numpy as np
import matplotlib.pyplot as plt
import itertools
L = 1500
B = 29
K = 1.2
T = B * K
dx = 50
dt = 50
S = 0.15
w = 0.005479452
h1 = 31
h2 = 29
marker = itertools.cycle(('o', 'v', 's', '^', 'd', 'v', '2', '1'))
recharge = (w * dt) / S
lamb = ((T * dt) / ((dx ** 2) * S))
# Implicit Matrix Coefficients
a = - lamb
b = (1 + (2 * lamb))
c = - lamb
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
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
# Initial Condition
d = np.zeros(length)
for n in range(1, (length-1)):
    d[n] = ((h1 - ((h1 - h2) / L) * dx)) + recharge
    dx = dx + 50
d[0] = h1
d[(length-1)] = h2
# Implicit Solution
days = [100, 200, 500, 750, 1000, 1500, 2000, 2500]
for t in range(len(days)):
    count = int(days[t] / dt)
    for x in range(count):
        t = (np.linalg.solve(Im, d))
        d = t
    d[0] = h1
    d[(length-1)] = h2
    plt.plot(l, t, marker=next(marker))
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Head (m)')  # Labeling of Y-axis
plt.title('Distance vs Head')
plt.legend(['100 days', '200 days', '500 days', '750 days', '1000 days', '1500 days', '2000 days', '2500 days'])
plt.show()


