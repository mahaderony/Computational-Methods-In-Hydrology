def matrix (length, a, b, c):
    import numpy as np
    Im = np.zeros((length**2)).reshape(length, length)
    for i in range(length):
        for j in range(length):
            if (i + 1) == j:
                Im[i][j] = c
            elif (i - 1) == j:
                Im[i][j] = a
            elif i == j:
                Im[i][j] = b
    Im[0][0] = 1
    Im[0][1] = 0
    Im[(length-1)][(length-1)] = 1
    Im[(length-1)][(length-2)] = 0
    return (Im)

m1 = matrix(3, 1, 2, 9)
print(m1)