import numpy as np


def matmul(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")

    res = [[0 for x in range(len(b[0]))] for y in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
                # res[j][i] += a[i][k] * b[k][j]
    
    return res


def matmul2(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")

    res = np.matmul(a, b).tolist()
    
    return res