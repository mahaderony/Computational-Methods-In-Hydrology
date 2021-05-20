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
# length discretization
l = np.arange(0, (L+dx), dx)
length = len(l)
# Matix Coefficient
a = (1+alpha)
b1 = - (2+(beta*R[0]))
b2 = - (2+(beta*R[1]))
b3 = - (2+(beta*R[2]))
b4 = - (2+(beta*R[3]))
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
count = int(Time / dt) # for time loop
Ci1 = np.zeros(length)
Ci1[0] = 100
Ci2 = np.zeros(length)
Ci3 = np.zeros(length)
Ci4 = np.zeros(length)
C1 = np.zeros(length)
C2 = np.zeros(length)
C3 = np.zeros(length)
C4 = np.zeros(length)
for i in range(count): # Time loop
    d1 = (-beta*R[0])*Ci1
    d1[0] = 100
    Csp1 = (np.linalg.solve(Im1, d1))
    #RK4 for species 1
    for j in range(length):
        k1 = -K[0]*Csp1[j]
        k2 = -K[0]*(Csp1[j] + k1*(dt/2))
        k3 = -K[0]*(Csp1[j] + k2*(dt/2))
        k4 = -K[0]*(Csp1[j] + k3*dt)
        kavg =(k1 + 2*k2 + 2*k3 + k4)/6
        C1[j] = Csp1[j] + (kavg*dt)    
    d2 = (-beta*R[1]*Ci2)
    d2[0] = 0
    Csp2 = (np.linalg.solve(Im2, d2))
    #RK4 for species 2
    for j in range(length):
        k1 =((K[0]*R[0]*C1[j])/R[1]) -K[1]*Csp2[j]
        k2 =((K[0]*R[0]*C1[j])/R[1]) -K[1]*(Csp2[j] + k1*(dt/2))
        k3 =((K[0]*R[0]*C1[j])/R[1]) -K[1]*(Csp2[j] + k2*(dt/2))
        k4 =((K[0]*R[0]*C1[j])/R[1]) -K[1]*(Csp2[j] + k3*dt)
        kavg =(k1 + 2*k2 + 2*k3 + k4)/6
        C2[j] = Csp2[j] + (kavg*dt)    
    d3 = (-beta*R[2]*Ci3)
    d3[0] = 0
    Csp3 = (np.linalg.solve(Im3, d3))
    #RK4 for species 3
    for j in range(length):
        k1 =((K[1]*R[1]*C2[j])/R[2]) -K[2]*Csp3[j]
        k2 =((K[1]*R[1]*C2[j])/R[2]) -K[2]*(Csp3[j] + k1*(dt/2))
        k3 =((K[1]*R[1]*C2[j])/R[2]) -K[2]*(Csp3[j] + k2*(dt/2))
        k4 =((K[1]*R[1]*C2[j])/R[2]) -K[2]*(Csp2[j] + k3*dt)
        kavg =((1/6)*(k1 + 2*k2 + 2*k3 + k4))
        C3[j] = Csp3[j] + (kavg*dt)     
    d4 = (-beta*R[3]*Ci4)
    d4[0] = 0
    Csp4 = (np.linalg.solve(Im4, d4))
    #RK4 for species 4
    for j in range(length):
        k1 =((K[2]*R[2]*C3[j])/R[3]) -K[3]*Csp4[j]
        k2 =((K[2]*R[2]*C3[j])/R[3]) -K[3]*(Csp4[j] + k1*(dt/2))
        k3 =((K[2]*R[2]*C3[j])/R[3]) -K[3]*(Csp4[j] + k2*(dt/2))
        k4 =((K[2]*R[2]*C3[j])/R[3]) -K[3]*(Csp4[j] + k3*dt)
        kavg =((1/6)*(k1 + 2*k2 + 2*k3 + k4))
        C4[j] = Csp4[j] + (kavg*dt)    
    Ci1 = C1
    Ci2 = C2
    Ci3 = C3
    Ci4 = C4
plt.plot(l, C1, linestyle = ':')
plt.plot(l, C2, linestyle = '--' )
plt.plot(l, C3, linestyle = '-.')
plt.plot(l, C4)
# Plotting
plt.axis('auto')
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Concentration (mM)')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.legend(['Species 1', 'Species 2', 'Species 3', 'Species 4'])
plt.show()