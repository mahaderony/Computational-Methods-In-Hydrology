# HW 02 Q 01 : Decrease of temperature of a cooling body
import math
def T(t):
    return float((-0.1 * (t ** 4)) - (0.15 * (t ** 3)) - (0.5 * (t ** 2)) - (0.25 * t) + 1.2)
def T1(t):
    return float((-0.4 * (t ** 3)) - (0.45 * (t ** 2)) - t - 0.25)
def T2(t):
    return float((-1.2 * (t ** 2)) - (0.9 * t) - 1)
def T3(t):
    return float((-2.4 * t - .9))
def T4(t):
    return float(-2.4)
# Calculating Temperature at 0, 1 and 2 hours
print('The value of the function at t = 0 is', (T(0)))
print('The value of the function at t = 1 is', (T(1)))
print('The value of the function at t = 2 is', (T(2)))
# Using Taylor Series
To = 1.2
t = 0
for dx in range(1, 3, 1):
    T = float(
        (To + (T1(t) * dx) + (T2(t) * ((dx ** 2) / math.factorial(2))) + (T3(t) * ((dx ** 3) / math.factorial(3))))) + (
                    T4(t) * (dx ** 4) / math.factorial(4))
    print('The value of the function using taylor series is', T)
# Using the first derivative alone to find T after 1 hour
dx = 1
Tn1 = (To + (T1(t) * dx))
print('the numerical value of the function at x = 1 is', Tn1)
err1 = ((To - Tn1) / To) * 100
print('the error is', err1)