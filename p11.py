# HW 02 Problem 2 : Falling body problem
import math
def f(t):
    return float(g - ((cd * g * t) / m))
def V(t):
    return float(((g * m) / cd) * (1 - math.exp(-cd * t) / m))
# Initial Condition
m = 1
cd = 0.6
g = 32.2
ti = 0
vi = 0
# Applying Eular Method
dt = float(input('interval size'))
n = int(1 / dt)
for i in range(0, n, 1):
    k = f(ti)
    v = float(vi + (k * dt))
    ti = ti + dt
    vi = v
    print('Numerical Velocity', v)
    print('Analytical Velocity',V(ti))
