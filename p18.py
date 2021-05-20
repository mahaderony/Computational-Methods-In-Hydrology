# HW 03/ Q01 (b)
import math
def f(t, y):
    return float((4 * math.exp(0.8 * t)) - (0.5 * y))
# Initial Condition
ti = 0
yi = 2
# Applying Eular's Method
dt = float(input('interval size'))
n = int(20 / dt)
for i in range(0, n, 1):
    k1 = f(ti, yi)
    ye = (yi + (k1 * dt))
    ti = (ti + dt)
    yi = ye
    #print('Time', ti)
    print(ye)
