from typing import List

def max_consecutive_ones(nums:List[int]) -> int:
    max = 0
    count = 0

    for i in range(len(nums)):
        if nums[0] != 1:
            count = 0

        if nums[i] == 1:
            count += 1

        if count > max:
            max = count

    return max
