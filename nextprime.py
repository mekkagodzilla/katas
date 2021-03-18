'''
Get the next prime number!

You will get a numbern (>= 0) and your task is to find the next prime number.

Make sure to optimize your code: there will numbers tested up to about 10^12.
'''
def is_a_prime(n):
    ''' takes a positive integer as argument. 
    Returns True if it's a prime number, False if it's not a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5 + 1
    i = 3

    while i <= max:
        if n % i == 0:
            return False
        i = i + 2
    return True

def next_prime(n):
    while not is_a_prime(n):
        n +=1
    return n