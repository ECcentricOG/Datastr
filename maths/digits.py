def count_digit(n:int)-> int:
    count = 0
    while(n > 0):
        count = count + 1
        n = n // 10
    return count

def reverse_digit(n:int)->int:
    n = abs(n)
    reverse = 0
    while(n > 0):
        rem = n % 10
        reverse = (reverse * 10) + rem
        n = n // 10
    return reverse

def is_pallindrome(n:int)->bool:
    if n < 0:
        return False
    return n == reverse_digit(n)
