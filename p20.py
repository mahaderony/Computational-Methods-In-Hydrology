# HW 04: Problem 01
import matplotlib.pyplot as plt
import numpy as np
t = 0
dt = 0.1
lamb = 0.020875
# Initial Condition
x = [100, 0, 0, 0, 0, 50]
# Boundary Condition
xn = [100, 0, 0, 0, 0, 50]
# Applying Condition
# After 3 sec
for m in range(30):
    for i in range(1, 5):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    xn = x
x3 = x
x_a = np.linspace(0, 10, 6)
plt.plot(x_a, x3, marker = 'o')
# After 6 sec
for m in range(60):
    for i in range(1, 5):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
x6 = x
x_a = np.linspace(0, 10, 6)
plt.plot(x_a, x6, marker = 'x')
# After 9 sec
for m in range(90):
    for i in range(1, 5):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
x9 = x
x_a = np.linspace(0, 10, 6)
plt.plot(x_a, x9, marker = 'p')
# After 12 sec
for m in range(120):
    for i in range(1, 5):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    x = xn
x12 = x
x_a = np.linspace(0, 10, 6)
plt.plot(x_a, x12, marker = 'v')
# Plotting
plt.xlabel('Distance(m)') # X-Axis
plt.ylabel('Temp degC') # Y-axis
plt.title('Change of Temperature throughout the length')
plt.legend(['3 secs','6 secs','9 secs','12 secs'])
plt.grid('True')
plt.show()


