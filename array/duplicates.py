from typing import List

def remove_duplicates(nums: List[int]) -> int:
    n = len(nums)
    i = 0

    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


def contains_duplicate(nums:List[int]) -> bool:
    n = len(nums)
    m = len(set(nums))
    if n == m:
        return True
    return False
