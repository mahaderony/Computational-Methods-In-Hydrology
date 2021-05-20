# Problem 01
import numpy as np
import matplotlib.pyplot as plt
import itertools
L = 100
Time = [5, 10, 15, 20]
dx = .5
dt = .25
V = 1
Cr = (V * dt) / dx
style = itertools.cycle((':', '--', '-.', '-'))
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Initial Condition
C = np.zeros(length)
C[0] = 1
# Explicit Solution
for t in range(len(Time)):
    count = int(Time[t] / dt)
    Ci = np.zeros(length)
    for m in range(count):
        for i in range(1, (length-1)):
            fip = V*C[i]
            fim = V*C[i-1]
            Ci[i] = C[i] -((dt/dx)*(fip-fim))
        Ci[0] = 1
        C = Ci
        Ci = np.zeros(length)
    plt.plot(l, C, linestyle = next(style))
    C = np.zeros(length)
    C[0] = 1        
# Plotting
plt.axis([0, 25, 0, 1.2])
plt.xlabel('Distance (cm)')  # Labeling of X-Axis
plt.ylabel('Concentration (mg/L)')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.grid()
plt.legend(['5 days', '10 days', '15 days', '20 days'])
plt.show()