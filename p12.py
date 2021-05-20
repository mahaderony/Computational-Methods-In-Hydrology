# HW02 Problem 4
# Defining the differential equation
def f(y ,t):
    return float((-1.2 * (y**2)) + t)
# Initial Condition
ti = 0
yi = 3
# Applying Eular method
dt = float(input('interval size'))
n = int(2 / dt)
for i in range(0, n, 1):
    t = float(ti + dt)
    print(t)
    k = f(yi, ti)
    y = float(yi + (k * dt))
    yi = y
    ti = t
    print('The numerical value is', yi)
