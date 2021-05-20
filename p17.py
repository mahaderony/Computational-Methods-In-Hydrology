# HW 03/ Q01 (a)
import math
def f(t, y):
    return float((4 * math.exp(0.8 * t)) - (0.5 * y))
def Analytical(t):
    return float(((4 * math.exp(0.8 * t)) - (1.4 * math.exp(-0.5 * t))) / 1.3)
# Initial Condition
ti = 0
yi = 2
# Applying Huen's Method
dt = float(input('interval size'))
n = int(20 / dt)
for i in range(0, n, 1):
    k1 = f(ti, yi)
    ye = (yi + (k1 * dt))
    ti = ti + dt
    k2 = f(ti, ye)
    ka = ((k1 + k2)/2)
    yh = (yi + (ka * dt))
    #print('Time', ti)
    #rint('Analytical', Analytical(ti))
    print(yh)
    yi = yh



