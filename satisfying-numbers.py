'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Task:
Write

smallest(n)

that will find the smallest positive number that is evenly divisible by all of the numbers from 1 to n (n <= 40).
E.g

smallest(5) == 60 # 1 to 5 can all divide evenly into 60
smallest(10) == 2520
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

def smallest(n):

    return res           
    
 
print(smallest(10))