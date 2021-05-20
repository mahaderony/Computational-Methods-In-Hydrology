# Problem 05
# (Implicit in time and centered in space)
import numpy as np
import matplotlib.pyplot as plt
import itertools
L = 100
Time = 200
dx = 0.5
dt = 0.1
V = 1
D = 0.3
xxx = np.arange(0, 2000)
style = itertools.cycle((':', '--', '-.', '-'))
alpha = (V*dx)/(2*D)
beta = ((dx**2) / (D*dt))
temp = np.zeros(2000)
# Matix Coefficient
a = 1 + alpha
b = -(2 + beta)
c = 1 - alpha
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
C[0] = 1
# RHS
d  = -beta * C
d[0] = 10000
d[(length-1)] = 0 
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
for t in range(0 ,2000):
    if t*dt > 1:
        d[0] = 0  
    count = int(Time / dt)
    if t*dt > 1:
        d[0]
    for x in range(count-1):
        Ci = (np.linalg.solve(Im, d))
        d = - beta * Ci
        #plt.plot(l, t, linestyle = next(style))
        
        temp[t]=Ci[length-1]
plt.plot (temp,xxx) 
# Plotting
plt.axis([0, 100, 0, 1.2])
plt.xlabel('Distance (cm)')  # Labeling of X-Axis
plt.ylabel('Concentration (mg/L)')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.grid()
plt.legend(['5 days', '10 days', '20 days', '80 days', 'Analytical'])
plt.show()