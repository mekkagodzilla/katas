from math import factorial

def easyline(n):
    res = 0
    for i in range(n +1):
        value = factorial(n) // (factorial(i)*factorial(n - i))
        res += value ** 2
    return res

print(easyline(4))
    