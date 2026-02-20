from typing import List


def two_sum(nums:List[int], target:int) -> List[int]:
    tracker = {}

    for i, num in enumerate(nums):
        rem = target - num
        if rem in tracker:
            return [nums[rem], i]
        tracker[num] = i
    return [0, 0]
