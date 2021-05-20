#problem 3
import numpy as np
from scipy.sparse import diags
length = 25
a = np.ones(length) 
a[6:9] = 4
a[11:14] = 4
a[16:19] = 4
b = np.zeros(length) 
b[6:9] = -1
b[11:14] = -1
b[16:19] = -1
c = np.zeros(length) 
c[6:9] = -1
c[11:14] = -1
c[16:19] = -1
d = np.zeros(length) 
d[5:8] = -1
d[10:13] = -1
d[15:18] = -1
e = np.zeros(length)
e[1:4] = -1
e[6:9] = -1
e[11:14] = -1

diagonals = [a,b,c,d,e]

Im = diags(diagonals, [0,1,5,-1,-5]).toarray()

d = np.zeros(length)
d[:5] = 100
d[5] = 75
d[10] = 75
d[15] = 75
d[9] = 50
d[14] = 50
d[19] = 50

solution = np.linalg.solve(Im, d).reshape(5,5)
print(solution)
