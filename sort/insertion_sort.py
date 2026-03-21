from typing import List


def sort(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(1, n):
        ele = nums[i]
        j = i - 1
        
        while j >= 0 and ele < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = ele

    return nums
