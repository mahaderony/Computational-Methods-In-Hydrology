# Problem 01: Calculating Cosine of an angle with Maclaurine Series and comparing it with exact result
import math
x = int(input('Enter the angle in degree '))
xr = float(x * (math.pi / 180))
# Using Exact Formula
Exact_cos = math.cos(xr)
print('The Exact value of Cos', x, 'degree is', Exact_cos, )
# Using Maclaurine Series
Approx_cos_2 = float(1 - (xr ** 2 / math.factorial(2)))
Approx_cos_3 = float(1 - (xr ** 2 / math.factorial(2)) + (xr ** 4 / math.factorial(4)))
Approx_cos_4 = float(1 - (xr ** 2 / math.factorial(2)) + (xr ** 4 / math.factorial(4)) - (xr ** 6 / math.factorial(6)))
print('The Approximate value of Cos', x, 'Using 2 terms of Maclaurin is', Approx_cos_2, )
Err2 = float(((Exact_cos - Approx_cos_2) * 100) / Exact_cos)
print('the error is', Err2, 'percent')
print('The Approximate value of Cos', x, 'Using 3 terms of Maclaurin series is', Approx_cos_3, )
Err3 = float(((Exact_cos - Approx_cos_3) * 100) / Exact_cos)
print('the error is', Err3, 'percent')
print('The Approximate value of Cos', x, 'Using 4 terms of Maclaurin Series is', Approx_cos_4, )
Err4 = float(((Exact_cos - Approx_cos_4) * 100) / Exact_cos)
print('the error is', Err4, 'percent')
