# Problem 01
# Matrix function
def matrix (length, a, b, c):
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
    Im[0][0] = 1
    Im[0][1] = 0
    Im[(length-1)][(length-1)] = b
    Im[(length-1)][(length-2)] = 2
    return (Im)
import numpy as np
import matplotlib.pyplot as plt    # plotting
# Parameters
L = 3000 # m
dt = 10 # days
dx = 20 # m
Time = 3000 # days
R = [5.3, 1.9, 1.2, 1.3] # rates
K = [7e-4, 5e-4, 4.5e-4, 3.8e-4]
alpha = 1 # m
V = 1 # m/day
D = 10*V
beta = dx**2/(D*dt)
gamma1 = (K[0]* dx**2 * R[0]) / D
gamma2 = (K[1]* dx**2 * R[1]) / D
gamma3 = (K[2]* dx**2 * R[2]) / D
gamma4 = (K[3]* dx**2 * R[3]) / D
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Matix Coefficient
a = (1+alpha)
b1 = - (2+(beta*R[0])+gamma1)
b2 = - (2+(beta*R[1])+gamma2)
b3 = - (2+(beta*R[2])+gamma3)
b4 = - (2+(beta*R[3])+gamma4)
c = (1-alpha)
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Implicit Matrix for Sp1,2,3,4
Im1 = matrix(length, a, b1, c)
Im2 = matrix(length, a, b2, c)
Im3 = matrix(length, a, b3, c)
Im4 = matrix(length, a, b4, c)
# Implicit Solution
count = int(Time / dt)
Ci1 = np.zeros(length)
Ci1[0] = 100
Ci2 = np.zeros(length)
Ci3 = np.zeros(length)
Ci4 = np.zeros(length)
for i in range(count):
    d1 = (-beta*R[0])*Ci1
    d1[0] = 100
    Csp1 = (np.linalg.solve(Im1, d1))
    d2 = (-beta*R[1]*Ci2) -(gamma1*Csp1)
    d2[0] = 0
    Csp2 = (np.linalg.solve(Im2, d2))      
    d3 = (-beta*R[2]*Ci3) -(gamma2*Csp2)
    d3[0] = 0
    Csp3 = (np.linalg.solve(Im3, d3))      
    d4 = (-beta*R[3]*Ci4) -(gamma3*Csp3)
    d4[0] = 0
    Csp4 = (np.linalg.solve(Im4, d4))   
    Ci1 = Csp1
    Ci2 = Csp2
    Ci3 = Csp3
    Ci4 = Csp4
    
plt.plot(l, Csp1, linestyle = ':')
plt.plot(l, Csp2, linestyle = '--' )
plt.plot(l, Csp3, linestyle = '-.')
plt.plot(l, Csp4)
# Plotting
plt.axis('auto')
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Concentration (mM)')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.legend(['Species 1', 'Species 2', 'Species 3', 'Species 4'])
plt.show()