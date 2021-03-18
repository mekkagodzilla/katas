


def strange_math(n, k):
    alphaRange = [ str(i) for i in range(n +1) ]
    alphaRange.sort()
    print(alphaRange)
    return alphaRange.index(str(k))



print(strange_math(11, 2))