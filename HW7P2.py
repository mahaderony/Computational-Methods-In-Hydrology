# Problem 02
# (Implicit in time and backward in space)
import numpy as np
import matplotlib.pyplot as plt
import itertools
L = 100
Time = [5, 10, 15, 20]
dx = 0.5
dt = 0.1
V = 1
style = itertools.cycle((':', '--', '-.', '-'))
Cr = -(V * dt) / dx # Corund's Number
# Matix Coefficient
a = Cr
b = (1-Cr)
c = 0
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
# Implicit Solution for all time steps
for t in range(len(Time)):
    count = int(Time[t] / dt)
    for x in range(count):
        t = (np.linalg.solve(Im, C))
        C = t
        C[0] = 1
    plt.plot(l, t, linestyle = next(style))
    C = np.zeros(length)
    C[0] = 1
# Plotting
plt.axis([0, 30, 0, 1.2])
plt.xlabel('Distance (cm)')  # Labeling of X-Axis
plt.ylabel('Concentration (mg/L)')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.grid()
plt.legend(['5 days', '10 days', '15 days', '20 days'])
plt.show()