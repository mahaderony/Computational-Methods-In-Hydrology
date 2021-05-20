#HW02 Problem 6
import math
def A(t):
    return float(Ai * math.exp(-k1 * t))
def B(t):
    return float(Ai * ((k1 / (k2 - k1)) * (math.exp(-k1 * t) - (math.exp(-k2 * t)))))
def C(t):
    return float(Ai - A(t) - B(t))
# Initial Conditions
Ai = 10
Bi = 0
Ci = 0
k1 = 100
k2 = 75
print('Analytical Value of A is', A(2))
print('Analytical Value of B is', B(2))
print('Analytical Value of C is', C(2))
# Using Eular Method
dt = float(input('interval size'))
n = int(2 / dt)
for i in range(0, n, 1):
    ka = (-k1 * Ai)
    kb = ((k1 * Ai) - (k2 * Bi))
    kc = (k2 * Bi)
    A = Ai + (ka * dt)
    Ai = A
    B = Bi + (kb * dt)
    Bi = B
    C = Ci + (kc * dt)
    Ci = C
    print('Numerical A', A)
    print('Numerical B', B)
    print('Numerical C', C)
