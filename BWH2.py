#FEM without Mass Lumping
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
import matplotlib.pyplot as plt
import math
L = 104
Time = 10
alpha = 2.5
dx = 2
dt = 1
V = 4
D = (alpha * V)
l = np.arange(0, L, dx)
length = len(l)
count = int(Time / dt)
C = np.zeros(length)
C[0]= 100
# matrix coeff
a = D/dx
b = V/2
c = (dx/6)/dt
# A Matrix
A1 = matrix(length,-a, 2*a, -a, a, -a, 2*a, -a)
# A' Matrix
A2 = matrix(length,-b, 0*b, b, b, b ,-b ,-b)
# B/dt Matrix
B1 = matrix(length, c, 4*c, c, 2*c, c, 2*c, c)
B1[0][0]=1
B1[0][1] = 0
B1[length-1][length-1] = 4*c
# LHS Constant Matrix
Im = A1 + A2 + B1
Im[0][0] = 1
Im[0][1] = 0
Im[length-1][length-1] = 11.3333
# RHS Matrix d
d = np.matmul(B1, C)
d[0] = 100
#Solver
count = int(Time / dt)
for x in range(count):
    t = (np.linalg.solve(Im, d))
    t[0] = 100
    d = np.matmul(B1, t)
WMS = t
print(WMS)
plt.plot(l, WMS, marker='<')
# Analytical Solution
Co = 100
C = []
t = 10
for x in range(0, L, dx):
        A = math.erfc((x - V * t) / (2 * math.sqrt(D * t)))
        B = ((math.exp(((x * V) / D))) * (math.erfc((x + (V * t)) / 2 * math.sqrt(D * t))))
        n = (0.5 * Co * (A + B))
        C.append(n)
plt.plot(l, C, marker='.')
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Contaminant Concentration')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.grid()
plt.legend(['FEM','Analytical'])
plt.show()