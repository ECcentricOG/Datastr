from typing import List

def second_largest(nums: List[int]) -> int:
    n = len(nums)

    if n < 2:
        return -1

    m = max(nums[0], nums[1])
    s = min(nums[0], nums[1])
    
    for num in nums:
        if num > m:
            s = m
            m = num
            continue

        if m > num > s:
            s = num

    return s if s != m else -1
