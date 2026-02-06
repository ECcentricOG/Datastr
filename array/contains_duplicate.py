from typing import List


def contains_duplicate(nums:List[int]) -> bool:
    n = len(nums)
    m = len(set(nums))
    if n == m:
        return True
    return False
