from typing import List


def divide_array(nums:List[int], start:int, end:int) -> List:
    if start >= end:
        print(nums[start])
        return nums
    mid = (start + end) // 2 
    divide_array(nums, start, mid)
    divide_array(nums, mid + 1, end)
    return nums
