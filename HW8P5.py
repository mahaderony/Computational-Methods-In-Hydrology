#Problem5: Operate Split Method
import numpy as np
import matplotlib.pyplot as plt
import itertools
L = 100
Time = [5, 10, 20, 80]
dx = 0.5
dt = 0.1
V = 1
D = 0.3
Cr = (V * dt) / dx
lamb = D*dt/dx**2
style = itertools.cycle((':', '--', '-.', '-'))
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
C[0] = 1
# Matix Coefficient
a = -lamb
b = (1+2*lamb)
c = -lamb
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
C[0] = 1
# Implicit Matrix
Im = np.zeros((length**2)).reshape(length, length)
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
Im[(length-1)][(length-1)] = 1
Im[(length-1)][(length-2)] = 0
# Explicit Solution
for t in range(len(Time)): # time loop
    count = int(Time[t] / dt)
    Ci = np.zeros(length)
    for m in range(count): # iteration for time
        for i in range(1, (length-1)): # Concentration at each node
            Ci[0] = 1
            Ci[i] = C[i] - Cr*(C[i]-C[i-1])
        C = Ci
        Ci = np.zeros(length) # reset Ci
        Ci = (np.linalg.solve(Im, C))
    plt.plot(l, Ci, linestyle = next(style))
    C = np.zeros(length)
    C[0] = 1       
# Plotting
plt.axis([0, 100, 0, 1.3])
plt.xlabel('Distance (cm)')  # Labeling of X-Axis
plt.ylabel('Concentration (mg/L)')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.grid()
plt.legend(['5 days', '10 days', '20 days', '80 days'])
plt.show()