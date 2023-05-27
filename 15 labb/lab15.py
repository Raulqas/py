import math

def f(x):
    return (5 * x ** 2 - 8) / (x ** 3 + 1)

def g(x):
    return math.sqrt(x + 1) - math.sqrt(x) - (1 / 2)

m = 10000
n = 1000

A = [[f(i) + g(j) for j in range(1, m + 1)] for i in range(1, n + 1)]

N_A = math.sqrt(n * m) * max(abs(A[i][j]) for i in range(n) for j in range(m))

print(f'{N_A:.6f}')