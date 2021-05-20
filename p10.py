# HW 02 Q 01 Continued:
def T1(t):
    return float((-0.4 * (t ** 3)) - (0.45 * (t ** 2)) - t - 0.25)
# Initial Condition
Ti = 1.2
ti = 0
# Applying Eular's method:
dt = float(input('interval size'))
n = int(1 / dt)
for i in range(0, n, 1):
    k = T1(ti)
    T = float(Ti + (k * dt))
    ti = ti + dt
    Ti = T
    print('The numerical value is', T)