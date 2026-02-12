from typing import List

def binary_value(n:int) -> int:
    i:int = 1
    nums:List[int] = []
    while n >= 1:
        print(n)
        while i <= n:
            if n // i <= 1:
                nums.append(i)
                n = n % i
                i = 1
                print(i)
                break;
            i *= i
    print(nums)
    return n
