import random
import math

## method 1 - brute force - O(n)
def prime_brute(n):
    if n < 4:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

## method 2 - mini brute force - O(n)
def prime_mini_brute(n):
    if n < 4:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

## method 3 - fermat
def prime_fermat(n):
    for a in range(2,n):
        if pow(a,n-1,n) != 1:
            return False
    return True


n1 = random.randint(0,100)
print(n1)
print(prime_brute(n1))
print(prime_mini_brute(n1))
print(prime_fermat(n1))
