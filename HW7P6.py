# Problem 06
# (Implicit in time and centered in space)
import numpy as np
import matplotlib.pyplot as plt
L = 100
Time = 200
dx = 0.5
dt = 0.1
V = 1
D = 0.3
alpha = (V*dx)/(2*D)
beta = ((dx**2) / (D*dt))
Conc = []
t = np.arange(0, (Time+dt), dt)
# Matix Coefficient
a = 1 + alpha
b = -(2 + beta)
c = 1 - alpha
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
C[0] = 10000
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
Im[(length-1)][(length-1)] = -(2 * alpha + beta)
Im[(length-1)][(length-2)] = 2 * alpha
# Implicit Solution for all time steps
count = int(Time / dt)
for x in range(count+1):
    Ci = (np.linalg.solve(Im, C))
    Conc.append(Ci[(length-1)] * 10)
    C = - beta * Ci
    if count <= 1:
        C[0] = 10000
    else:
        C[0] = 0
plt.plot(t, Conc)
# Plotting
plt.axis('auto')
plt.xlabel('Time,day')  # Labeling of X-Axis
plt.ylabel('Concentration (mg/L)')  # Labeling of Y-axis
plt.title('Breakthrough Curve')
plt.show()