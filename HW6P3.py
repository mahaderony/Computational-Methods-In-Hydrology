# Problem 03:
import numpy as np
import matplotlib.pyplot as plt
import math
# Parameters
L = 1500
dx = 50
dt = 50
Sy = 0.15
w = 0.005479452
k = 1.2
h1 = 31
h2 = 29
beta = ((2 * Sy * dx ** 2) / (k * dt))
eeta = ((2 * dx ** 2 * w) / k)
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
for n in range(length):
    C[n] = float(31 - (((31 - 29) / 1500) * dx))
    dx = dx + 50
C[0] = h1
C[(length-1)] = h2
Hm = C
PHi = C
Hi = np.zeros(length)
d = np.zeros(length)
p = int(len(C))
# Picard method
days = [2500]
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
    plt.plot(l, Hi, marker='v')
# Analytical
hx = np.zeros(length)
x = np.arange(0,1550,50)
for i in range(length):
    hx[i] = math.sqrt((h1**2) - ((x[i]*((h1**2) - (h2**2)))/L) + ((w*x[i]*(L-x[i]))/k))
print (hx)
plt.plot(l, hx, marker='o')
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Head (m)')  # Labeling of Y-axis
plt.title('Distance vs Head')
plt.legend(['Numerical 2500 days', 'Analytical Steady state'])
plt.show()

