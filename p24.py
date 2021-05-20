# HW 04: Problem 05
import matplotlib.pyplot as plt
import numpy as np
t = 0
dt = 5
D = 10
dx = 10
lamb = (D * dt / (dx**2))
# Initial Condition
x = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
x_a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Boundary Condition
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
# Applying Condition
# After 10 min
for m in range(2):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='o')
# After 20 min
for m in range(4):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='v')
# After 40 min
for m in range(8):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='x')
# After 80 min
for m in range(16):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='^')
# After 160 min
for m in range(32):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='*')
# After 250 min
for m in range(50):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='<')
# After 500 min
for m in range(100):
    for i in range(1, 10):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
xp = xn
xn = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 11]
print(xp)
plt.plot(x_a, xp, marker='H')
# Plotting
plt.xlabel('Length (cm)') # X-axis label
plt.ylabel('Temperature (deg)') # Y-axis label
plt.title('Temperature Distribution with Time')
plt.legend(('time@10 min', 'time@20 min', 'time@40 min', 'time@80 min', 'time@160 min', 'time@250 min', 'time@500 min'))
plt.show()
