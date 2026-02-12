from typing import List

def binary_value(n:int) -> int:
    i:int = 1
    nums:List[int] = []
    while n >= 1:
        while i <= n:
            if n % i < i:
                nums.append(i)
                n = n % i
                i = 1
            i *= i
    print(nums)
    return n
