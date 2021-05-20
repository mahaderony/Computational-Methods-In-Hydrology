# HW03 : RK4
import math
import numpy as np
import matplotlib.pyplot as plt
def dy1(y1, y2):
    return float((998 * y1) + (1998 * y2))
def dy2(y1, y2):
    return float((-999 * y1) - (1999 * y2))
def ay1(t):
    return float((2 * math.exp(-t)) - (math.exp(-1000 * t)))
def ay2(t):
    return float((-math.exp(-t)) + (math.exp(-1000 * t)))
# Initial Conditions
y1 = 1
y2 = 0
dt = 0.001
dt2 = dt/2
T = 0.01
n = int(T / dt)
y1_n = np.zeros(n)
y2_n = np.zeros(n)
y1_n[0] = 1
y2_n[0] = 0
time = [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01]
# Numerical Solution
for i in range(n):
    k1_y1 = dy1(y1, y2)
    k1_y2 = dy2(y1, y2)
    k2_y1 = dy1((y1 + (k1_y1 * dt2)), (y2 + (k1_y2 * dt2)))
    k2_y2 = dy2((y1 + (k1_y1 * dt2)), (y2 + (k1_y2 * dt2)))
    k3_y1 = dy1((y1 + (k2_y1 * dt2)), (y2 + (k2_y2 * dt2)))
    k3_y2 = dy2((y1 + (k2_y1 * dt2)), (y2 + (k2_y2 * dt2)))
    k4_y1 = dy1((y1 + (k3_y1 * dt)), (y2 + (k3_y2 * dt)))
    k4_y2 = dy1((y1 + (k3_y1 * dt)), (y2 + (k3_y2 * dt)))
    kav_y1 = float((k1_y1 + (2 * k2_y1) + (2 * k3_y1) + k4_y1) / 6)
    kav_y2 = float((k1_y2 + (2 * k2_y2) + (2 * k3_y2) + k4_y2) / 6)
    y1_n[i] = (y1 + (kav_y1 * dt))
    y2_n[i] = (y2 + (kav_y2 * dt))
    y1 = y1_n[i]
    y2 = y2_n[i]
print('Numerical y1', y1_n)
print('Numerical y2', y2_n)
# Analytical solution
AY1 = np.zeros(n)
AY2 = np.zeros(n)
t = 0
for i in range(n):
    t = t + dt
    AY1[i] = ay1(t)
    AY2[i] = ay2(t)
print('Analytical y1', AY1)
print('Analytical y2', AY2)
# Plotting
plt.plot(time, y1_n, linestyle='dotted', marker='^')
plt.plot(time, AY1, linestyle='dashdot', marker='<')
plt.plot(time, y2_n, linestyle='dashed', marker='>')
plt.plot(time, AY2, marker='o')
plt.xlabel('Time') # Labeling of X-Axis
plt.ylabel('Y1 and Y2') # Labeling of Y-axis
plt.title('Time vs Y')
plt.legend(['y1 numerical','y1 analytical', 'y2 numerical','y2 analytical'])
plt.show()