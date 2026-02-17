from typing import List


def find_missing_no(nums:List[int]) -> int: 
    n = len(nums)

    sum = n * (n + 1) // 2

    total = 0
    for num in nums:
        total += num

    return sum - total
