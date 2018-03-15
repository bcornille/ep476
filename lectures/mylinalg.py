import numpy as np

def multiply_matvec(A, x):

    b = np.zeros(A.shape[0])
    for i in range(A.shape[1]):
        for j in range(x.size):
            b[i] += A[i, j]*x[j]

    return b

def multiply_matmat(A, B):

    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        assert A.shape[1] == B.shape[0]
        for k in range(B.shape[0]):
            for j in range(B.shape[1]):
                C[i, j] += A[i, k]*B[k, j]

    return C