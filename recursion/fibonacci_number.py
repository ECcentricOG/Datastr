def fibonacci_number(n:int) -> int:
    if n <= 1:
        return n
    
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)
