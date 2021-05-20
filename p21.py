# HW 04: Problem 02
import matplotlib.pyplot as plt
import numpy as np
t = 0
dt = 6
lamb = 0.735
mark = ['o', 'v', '*', '+', 's']
# Initial Condition
x = [100, 0, 0, 0, 0, 50]
# Boundary Condition
xn = [100, 0, 0, 0, 0, 50]
# Applying Condition
for m in range(5):
    for i in range(1, 5):
        xn[i] = (x[i] + (lamb * (x[i-1] - 2 * x[i] + x[i+1])))
    xp = xn
    print(xp)
    x_a = np.linspace(0, 10, 6)
    plt.plot(x_a, xp, marker=mark[m])
    x = xp
    xn = [100, 0, 0, 0, 0, 50]
# Plotting
plt.xlabel('Distance(m)') # X-Axis
plt.ylabel('Temp degC') # Y-axis
plt.title('Change of Temperature throughout the length')
plt.legend(['6 sec','12 sec','18 sec','24 sec', '30 sec'])
plt.grid('True')
plt.show()








