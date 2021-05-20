# Problem 5 Cont.... (Using Eular method)
def f(L):
    return float(-Kd * L)
def g(L, O):
    return float((-Kd * L) + (Ka * (9.5 - Oi)))
# Initial Condition
Li = 12
Oi = 9.5
ti = 0
Kd = 0.1
Ka = 0.02
#Applying Eular Method
dt = float(input('interval size'))
n = int(30 / dt)
for i in range(0, n, 1):
    k1 = f(Li)
    k2 = g(Li, Oi)
    L = float(Li + (k1 * dt))
    Li = L
    O = float((Oi + (k2 * dt)))
    Oi = O
    ti = ti + dt
    print('@', ti, 'min')
    print('Numerical BOD', L)
    print('Numerical DO', O)