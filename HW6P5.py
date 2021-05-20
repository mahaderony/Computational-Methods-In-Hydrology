# Problem 05:
import numpy as np
import matplotlib.pyplot as plt
import itertools
# Parameters
L = 50
dx = 2
dt = .1
Sy = .33
w = 2.13
k = 6.41
h1 = 15
h2 = 18.9
beta = ((2 * Sy * dx ** 2) / (k * dt))
eeta = ((2 * dx ** 2 * w) / k)
marker = itertools.cycle(('o', 'v', 's', '^'))
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
for n in range(length):
    C[n] = float(h1 - (((h1 - h2) / 1500) * dx))
    dx = dx + 50
C[0] = h1
C[(length-1)] = h2
Hm = C
PHi = C
Hi = np.zeros(length)
d = np.zeros(length)
p = int(len(C))
# Picard method
days = [0.30,0.80,1.80,3.30]
for t in range(len(days)):
    count = int(days[t] / dt)
    for t in range(count):
        for v in range(p):  # RHS
            d[v] = (beta * PHi[v]) + eeta
        d[0] = h1
        d[(p-1)] = h2
        A = np.zeros(length**2).reshape(length, length)
        for P in range(5):  # Picard Iteration
            for k in range(1, p-1): # Tridiag_Coeff
                a = -Hm[(k - 1)]
                b = ((2 * Hm[k]) + beta)
                c = -Hm[(k + 1)]
                A[k,k-1] = a
                A[k,k]=b
                A [k, k+1] = c
            A[0,0]=1
            A[length-1,length-1]=1
            Hi = (np.linalg.solve(A, d)) # Linear Solver
            Hm = Hi
        PHi = Hi
        print(Hi)
    plt.plot(l, Hi, marker=next(marker))
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Head (m)')  # Labeling of Y-axis
plt.title('Distance vs Head')
plt.legend(['0.30 min', '0.80 min', '1.80 min', '3.30 min'])
plt.show()


