# (Implicit in time and centered in space)
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
a = (1 + ((2 * D * dt) / (dx**2)))
b = (((V * dt) / (2 * dx)) - ((D * dt) / (dx**2)))
c = (-((V * dt) / (2 * dx)) - ((D * dt) / (dx**2)))
l = np.arange(0, (L+dx), dx)
length = len(l)
count = int(Time / dt)
C = np.zeros(length)
C[0] = 100
T10C = np.zeros(length)
# Implicit Matrix
Im = np.zeros((length**2)).reshape(length, length)
for i in range(length):
    for j in range(length):
        if (i + 1) == j:
            Im[i][j] = b
        elif (i - 1) == j:
            Im[i][j] = c
        elif i == j:
            Im[i][j] = a
Im[0][0] = 1
Im[0][1] = 0
Im[(length-1)][(length-1)] = 1
Im[(length-1)][(length-2)] = 0
count = int(Time / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T10C = t
print('Central\n', T10C)
plt.plot(l, T10C, marker='*')
#%%
# (Implicit in time and forward in space)
a = -2.5
b = 4
c = -0.5
l = np.arange(0, L, dx)
length = len(l)
count = int(Time / dt)
C = np.zeros(length)
C[0] = 100
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
count = int(Time / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T10F = t
plt.plot(l, T10F, marker='>')
print('Forward\n', T10F)
# (Implicit in time and backward in space)
a = -4.5
b = 8
c = -2.5
l = np.arange(0, L, dx)
length = len(l)
count = int(Time / dt)
C = np.zeros(length)
C[0] = 100
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
count = int(Time / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
T10B = t
plt.plot(l, T10B, marker='<')
print('Backwards\n', T10B)
#%%
# Analytical Solution
Co = 100
C = []
t = 10
for x in range(0, 104, 2):
        A = math.erfc((x - V * t) / (2 * math.sqrt(D * t)))
        B = ((math.exp(((x * V) / D))) * (math.erfc((x + (V * t)) / 2 * math.sqrt(D * t))))
        n = (0.5 * Co * (A + B))
        C.append(n)
plt.plot(l, C, marker='.')
print('Analytical\n', C)
# (Implicit in time and backward in space with numerical disoersion)
a = -1.5
b = 2
c = 0.5
l = np.arange(0, L, dx)
length = len(l)
count = int(Time / dt)
C = np.zeros(length)
C[0] = 100
#%%
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
print(Im)
count = int(Time / dt)
for x in range(count):
    t = (np.linalg.solve(Im, C))
    C = t
    C[0] = 100
TND = t
plt.plot(l, TND, marker='<')
print('With ND\n', TND)
#%%
# Plotting
plt.xlabel('Distance (m)')  # Labeling of X-Axis
plt.ylabel('Contaminant Concentration')  # Labeling of Y-axis
plt.title('Distance vs Contaminant Concentration')
plt.grid()
plt.legend(['centered@10','Forward@10','Backward@10','Analytical@10','Model with numerical dispersion'])
plt.show()