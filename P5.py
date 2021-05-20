# Problem 05:  Bessel Function problem
import math
x = float(input('Enter x'))
n = float(input('Enter n'))
s = 0
# using for loop to run the equation.
for k in range(0, 3, 1):
    jn = float((((-1) ** k) * (x ** (n + 2 * k))) / (2 ** (n + (2 * k)) * math.factorial(k) * math.factorial(n + k)))
    s = s + jn
print('The value of jn for x =', x ,'& n =', n ,'is', s)
