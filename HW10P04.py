#HW10_Problem04
def matrix (length, a, b, c, d, e, f, g):
    import numpy as np
    Im = np.zeros((length**2)).reshape(length, length)
    for i in range(length):
        for j in range(length):
            if (i + 1) == j:
                Im[i][j] = c
            elif (i - 1) == j:
                Im[i][j] = a
            elif i == j:
                Im[i][j] = b
    Im[0][0] = d
    Im[0][1] = e
    Im[(length-1)][(length-1)] = f
    Im[(length-1)][(length-2)] = g
    return (Im)
import numpy as np
# Parameters
Time = 50
L = 1500
dx = 50
dt = 50
S = 0.15
w = (2/365)
K = 1.2
h1 = 31
h2 = 29
B = 29
T = B * K
recharge = (w * dt) / S
lamb = ((T * dt) / ((dx ** 2) * S))
# Length discretization
l = np.arange(0, (L + dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
for n in range(length):
    C[n] = -0.3936
    dx = dx + 50
C[0] = h1
C[(length-1)] = h2
print(C)
# matrix coeff
a = 1
b = -2
c = 1
# A Matrix
M = matrix(length,a, b, c, 1, 0, 1, 0)
#Solver
h = (np.linalg.solve(M, C))
C[0] = h1
C[(length-1)] = h2
print(h)