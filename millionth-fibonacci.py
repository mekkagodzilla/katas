import numpy as np
import decimal

def fib(n):
    """Calculates the nth Fibonacci number"""
    if n == 0:
        return 0
    fibomatrix = np.array([[1, 1], [1, 0]], dtype=np.float128)
    M = fibomatrix
    for i in range(n -2):
        M = M.dot(fibomatrix)

    return int(M[0][0])

print(fib(71))