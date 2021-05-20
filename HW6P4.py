# Problem 04:
import numpy as np
import matplotlib.pyplot as plt
import itertools
# Parameters
L = 1500
dx = 50
dt = 50
S = 0.15
w = 0.005479452
k = 1.2
h1 = 31
h2 = 29
B = 29
K = 1.2
T = B * K
recharge = (w * dt) / S
lamb = ((T * dt) / ((dx ** 2) * S))
marker = itertools.cycle(('o', 'v', 's', '^', 'd', 'v', '2', '1'))
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
for n in range(length):
    C[n] = float(h1 - (((h1 - h2) / L) * dx))
    dx = dx + 50
C[0] = h1
C[(length-1)] = h2
Hm = C
PHi = C
Hi = np.zeros(length)
d = np.zeros(length)
p = int(len(C))
# Picard method
days = [100, 200, 500, 750, 1000, 1500, 2000, 2500]
for t in range(len(days)):
    count = int(days[t] / dt)
    for t in range(count):
        for v in range(p):  # RHS
            d[v] = (PHi[v]) + recharge
        d[0] = h1
        d[(p-1)] = h2
        A = np.zeros(length**2).reshape(length, length)
        for k in range(1, p-1): # Tridiag_Coeff
            a = -lamb
            b = (1 + (2 * lamb))
            c = -lamb
            A[k,k-1] = a
            A[k,k]=b
            A [k, k+1] = c
        A[0,0]=1
        A[length-1,length-1]=1
        Hi = (np.linalg.solve(A, d)) # Linear Solver
        PHi = Hi
    plt.plot(l, Hi, marker=next(marker))
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Head (m)')  # Labeling of Y-axis
plt.title('Distance vs Head')
plt.legend(['100 days', '200 days', '500 days', '750 days', '1000 days', '1500 days', '2000 days', '2500 days'])
plt.show()


