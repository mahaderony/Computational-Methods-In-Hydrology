def matrix (length, a, b, c, d, e, f, g):
    import numpy as np
    a = np.ones(length)
    a[6:9] = 4
    a[11:14] = 4
    a[16:19] = 4
    b = np.zeros(length)
    b[6:9] = -1
    b[11:14] = -1
    b[16:19] = -1
    c = b
    e = b
    Im = np.zeros((length**2)).reshape(length, length)
    for i in range(length):
        for j in range(length):
            if (i + 1) == j:
                Im[i][j] = c
            elif (i - 1) == j:
                Im[i][j] = a[i]
            elif i == j:
                Im[i][j] = b
    Im[0][0] = d
    Im[0][1] = e
    Im[(length-1)][(length-1)] = f
    Im[(length-1)][(length-2)] = g
    return (Im)
length=25
