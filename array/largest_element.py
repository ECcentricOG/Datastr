from typing import List


def largest_element(nums:List[int])-> int:
    if len(nums) < 1:
        return -1
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max
