import math

def is_prime(n:int) -> bool:
    if n == 0:
        return False 
    if n == 1:
        return False 
    if n % 2 == 0:
        return False 

    i:int = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True
