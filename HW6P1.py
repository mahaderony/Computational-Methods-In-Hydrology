#Problem 01:
import math 
Xold = 40
for i in range(23):
    Xnew = (-20/Xold) + 12
    Xold = Xnew
    print(Xnew)

Yold = 0
for j in range(59):
    Ynew = math.exp(-Yold)
    Yold = Ynew
    print(Ynew)